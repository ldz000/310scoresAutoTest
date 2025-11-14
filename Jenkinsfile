pipeline {
    agent any

    parameters {
        choice(
            name: 'TEST_TYPE',
            choices: ['smoke', 'regression', 'all'],
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

        // 你的 APK 文件路径（根据实际情况修改）
        APP_APK = "${PROJECT_DIR}/APP_APK/310Scores_4.7.25.apk"
        APP_PACKAGE = "com.scores.tfz"  // 你的应用包名
    }

    stages {
        stage('拉取代码') {
            steps {
                echo "从 GitHub 拉取最新代码..."
                git branch: 'main',
                    url: 'https://github.com/ldz000/310scoresAutoTest.git',
                    credentialsId: 'android-test-github'
            }
        }

        stage('环境准备') {
            steps {
                sh '''
                    echo "=== 准备测试环境 ==="
                    echo "工作目录: ${WORKSPACE}"
                    echo "Python环境:"
                    python3 --version
                    pip3 --version

                    # 创建测试目录
                    mkdir -p ${REPORT_DIR} ${ALLURE_RESULTS} ${SCREENSHOT_DIR}

                    # 安装依赖
                    echo "安装Python依赖..."
                    pip3 install -r requirements.txt

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
                        sh '''
                            echo "启动模拟器..."
                            # 启动模拟器（根据你的模拟器配置调整）
                            emulator -avd Pixel_4_API_30 -no-audio -no-snapshot &
                            sleep 60

                            # 等待设备就绪
                            adb wait-for-device
                            echo "设备已就绪"
                        '''
                    } else {
                        sh '''
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

        stage('安装测试应用') {
            steps {
                sh """
                    echo "安装测试APK..."
                    if [ -f "${APP_APK}" ]; then
                        adb install -r "${APP_APK}"
                        echo "APK安装成功"
                    else
                        echo "警告: APK文件不存在: ${APP_APK}"
                        echo "继续执行测试（假设应用已安装）"
                    fi
                """
            }
        }

        stage('执行UI自动化') {
            steps {
                script {
                    echo "开始执行 pytest + u2 自动化测试..."

                    // 构建 pytest 命令
                    def pytestCmd = "cd ${TEST_DIR} && python3 -m pytest"

                    // 添加测试类型过滤
                    if (params.TEST_TYPE == 'smoke') {
                        pytestCmd += " -m smoke"
                    } else if (params.TEST_TYPE == 'regression') {
                        pytestCmd += " -m regression"
                    }

                    // 添加参数（根据你的 pytest 配置调整）
                    pytestCmd += " --alluredir=${ALLURE_RESULTS}"
                    pytestCmd += " --html=${REPORT_DIR}/report.html"
                    pytestCmd += " --self-contained-html"
                    pytestCmd += " -v"

                    echo "执行命令: ${pytestCmd}"

                    try {
                        sh pytestCmd
                    } catch (Exception e) {
                        echo "测试执行出现异常: ${e}"
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }

        stage('收集结果') {
            steps {
                sh '''
                    echo "收集测试结果..."

                    # 收集设备日志
                    adb logcat -d > ${REPORT_DIR}/logcat.log || true

                    # 收集测试截图
                    adb pull /sdcard/DCIM/Screenshots ${SCREENSHOT_DIR} || true
                    adb pull /sdcard/Pictures/Screenshots ${SCREENSHOT_DIR} || true

                    # 如果使用 u2 的截图功能，可能还需要拉取其他目录
                    adb shell "ls /sdcard/" > ${REPORT_DIR}/sdcard_contents.log || true
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
            sh '''
                # 清理工作
                adb shell pm clear ${APP_PACKAGE} || true
            '''
        }
        success {
            emailext(
                subject: "✅ Android UI自动化测试通过: ${env.JOB_NAME}",
                body: "测试执行成功！报告: ${env.BUILD_URL}allure",
                to: "team@example.com"
            )
        }
        failure {
            emailext(
                subject: "❌ Android UI自动化测试失败: ${env.JOB_NAME}",
                body: "测试执行失败！详情: ${env.BUILD_URL}console",
                to: "team@example.com"
            )
        }
    }
}