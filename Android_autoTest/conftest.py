import os
import shutil
import time

import pytest
import uiautomator2 as u2
from typing import Generator

APP_CONFIGS = {
    "app1": "com.scores.tfz",
    "app2": "com.halo.fkkq"
}


@pytest.fixture
def device_factory(request):
    """设备工厂fixture，用于创建device实例"""

    def _create_device(app_key="app1"):
        """
        创建device实例
        :param device_key: 设备配置键，默认为device1
        :param app_key: 应用配置键，默认为app1
        """

        # 获取应用包名
        app_package = APP_CONFIGS.get(app_key, "com.scores.tfz")

        # 连接设备
        d = u2.connect("")

        # 清理目录（只在第一次调用时执行）
        if not hasattr(request.config, 'allure_cleaned'):
            if os.path.exists("./allure-results"):
                shutil.rmtree("./allure-results", ignore_errors=True)
            os.makedirs("./allure-results", exist_ok=True)
            request.config.allure_cleaned = True

        # 启动应用
        d.app_stop(app_package)
        d.app_start(app_package)

        # 返回设备实例
        return d

    return _create_device

# @pytest.fixture(scope="session",autouse=True)
# def d() -> Generator[u2.Device, None, None]:
#     # 连接设备
#     d = u2.connect("")
#     #清理目录
#     if os.path.exists("./allure-results"):
#         shutil.rmtree("./allure-results",ignore_errors=True)
#     os.makedirs("./allure-results", exist_ok=True)
#     # 启动
#     app_package = APP_CONFIGS.get(app_key, "com.scores.tfz")
#     d.app_start("com.scores.tfz")
#     yield d
#
#     # 测试结束后清理
#     d.app_stop("com.scores.tfz")


def logout():
    d = u2.connect("")
    time.sleep(2)
    d(resourceId="com.scores.tfz:id/image_header").click()
    time.sleep(2)
    d(resourceId="com.scores.tfz:id/image_header").wait(timeout=10)
    d(resourceId="com.scores.tfz:id/image_header").click()
    time.sleep(2)
    d(text="Log Out").click()
    time.sleep(2)
    assert d(text="Login").exists()
    time.sleep(2)
    d(resourceId="com.scores.tfz:id/sc_close_btn").click()
    time.sleep(2)




