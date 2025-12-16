
pipeline {
    agent any

    parameters {
        choice(
            name: 'TEST_TYPE',
            choices: ['smoke', 'all'],
            description: '310ui自动化'
        )
        choice(
            name: 'DEVICE_TYPE',
            choices: ['emulator', 'real-device'],
            description: '安卓'
        )
    }

    environment {
        PROJECT_DIR = "${WORKSPACE}"
        TEST_DIR = "${PROJECT_DIR}"
        REPORT_DIR = "${PROJECT_DIR}/reports"
        ALLURE_RESULTS = "${PROJECT_DIR}/allure-results"
        SCREENSHOT_DIR = "${PROJECT_DIR}/screenshots"
        PYTHON_PATH = 'C://Users/EDY/AppData/Local/Programs/Python/Python313/python.exe'

        // 你的 APK 文件路径（根据实际情况修改）
        APP_APK = "${PROJECT_DIR}/APP_APK/310Scores_4.7.25.apk"
        APP_PACKAGE = "com.scores.tfz"  // 你的应用包名
    }

    stages {
        stage('拉取代码') {
            steps {
                echo "从 GitHub 拉取最新代码..."
                git branch: 'master',
                    url: 'https://github.com/ldz000/310scoresAutoTest.git',
                    credentialsId: 'android-test-github'
            }
        }

        stage('环境准备') {
            steps {
                bat '''
                    echo "=== 准备测试环境 ==="
                    echo "工作目录: ${WORKSPACE}"
                    echo "Python环境:"
                    python3 --version
                    pip3 --version

                    # 创建测试目录
                    mkdir -p ${WORKSPACE}/reports
                    mkdir -p ${WORKSPACE}/allure-results
                    mkdir -p ${WORKSPACE}/screenshots
                    mkdir -p ${WORKSPACE}/logs

                    # 安装依赖
                    echo "安装Python依赖..."
                    python -m pip install --upgrade pip
                    pip install allure-pytest pytest -i https://pypi.tuna.tsinghua.edu.cn/simple


                    # 检查设备连接
                    echo "检查Android设备..."
                    adb devices -l
                '''
            }
        }

        stage('设备准备') {
            steps {
                script {
                    if (params.DEVICE_TYPE == 'emulator') {
                        bat '''
                            echo "启动模拟器..."
                            # 启动模拟器（根据你的模拟器配置调整）
                            emulator -avd Pixel_4_API_30 -no-audio -no-snapshot &
                            sleep 60

                            # 等待设备就绪
                            adb wait-for-device
                            echo "设备已就绪"
                        '''
                    } else {
                        bat '''
                            echo "使用真机测试..."
                            adb devices | grep -w device || {
                                echo "错误：未找到已授权的Android设备"
                                exit 1
                            }
                        '''
                    }
                }
            }
        }

        stage('可靠的APK安装') {
            steps {
                script {

                    bat """
                        echo "🔧 开始可靠的APK安装流程"

                        echo "步骤1: 基础检查"
                        if not exist "${APP_APK}" (
                            echo "❌ 错误: ${APP_APK} 不存在"
                            exit 1
                        )

                        echo "步骤2: 重启ADB"
                        adb kill-server
                        timeout /t 2 /nobreak
                        adb start-server
                        timeout /t 5 /nobreak

                        echo "步骤3: 等待设备"
                        adb wait-for-device
                        echo "✅ 设备已连接"

                        echo "步骤4: 卸载旧版本"
                        adb uninstall ${APP_PACKAGE} >nul 2>&1 && echo "旧版本已卸载" || echo "无需卸载"

                        echo "步骤5: 安装APK"
                        echo "正在安装 ${APP_APK} ..."
                        adb install -r -g "${APP_APK}"

                        if !errorlevel! equ 0 (
                            echo "✅ APK安装成功"
                            adb shell pm list packages | findstr "${APP_PACKAGE}" && echo "✅ 验证: 应用已安装"
                        ) else (
                            echo "❌ 安装失败，错误码: !errorlevel!"
                            echo "尝试替代方案..."
                        )
                    """
                }
            }
        }

        stage('执行自动化脚本') {
            steps {
                script {
                    // 1. 诊断环境
                    bat '''
                        echo "环境诊断..."
                        "%PYTHON_PATH%" --version
                        dir
                    '''

                    // 2. 执行主业务脚本
                    bat '"%PYTHON_PATH%" Android_autoTest/test_auto_310scores.py'
                }
            }
        }

        stage('收集结果') {
            steps {
                bat '''
                    echo "收集测试结果..."

                    # 收集设备日志
                    adb logcat -d > ${REPORT_DIR}/logcat.log || true

                '''

                // 归档测试产物
                archiveArtifacts artifacts: "reports/*.html, reports/*.log, screenshots/*.png", allowEmptyArchive: true
            }
        }

        stage('生成报告') {
            steps {
                // Allure 报告
                allure([
                    includeProperties: false,
                    jdk: '',
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: "${ALLURE_RESULTS}"]]
                ])

                // HTML 报告
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: "${REPORT_DIR}",
                    reportFiles: 'report.html',
                    reportName: 'HTML Test Report'
                ])
            }
        }
    }

    post {
        always {
            echo "测试执行完成"
            bat '''
                # 清理工作
                adb shell pm clear ${APP_PACKAGE} || true
            '''
        }
        success {
            emailext(
                subject: "✅ Android UI自动化测试通过: ${env.JOB_NAME}",
                body: "测试执行成功！报告: ${env.BUILD_URL}allure",
                to: "liudazhao@halomobi.com"
            )
        }
        failure {
            emailext(
                subject: "❌ Android UI自动化测试失败: ${env.JOB_NAME}",
                body: "测试执行失败！详情: ${env.BUILD_URL}console",
                to: "liudazhao@halomobi.com"
            )
        }
    }
}