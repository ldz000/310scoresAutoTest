import os
import shutil
import time

import pytest
import uiautomator2 as u2
from typing import Generator


@pytest.fixture(scope="session",autouse=True)
def d() -> Generator[u2.Device, None, None]:
    # 连接设备
    d = u2.connect("")
    #清理目录
    if os.path.exists("./allure-results"):
        shutil.rmtree("./allure-results",ignore_errors=True)
    os.makedirs("./allure-results", exist_ok=True)
    # 启动
    d.app_start("com.scores.tfz",)
    yield d

    # 测试结束后清理
    d.app_stop("com.scores.tfz")


#失败自动截图
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call, pytest_html=None):
    outcome = yield
    report = outcome.get_result()
    if report.failed and "device" in item.funcargs:
        d = item.funcargs["device"]
        d.screenshot(f"reports/fail_{item.name}.png")
        # 将截图链接添加到HTML报告
        if hasattr(report, "extra"):
            report.extra.append(pytest_html.extras.image(f"reports/fail_{item.name}.png"))

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




