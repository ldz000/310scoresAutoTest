import os
import time
from pydoc import classname

import allure
import pytest
import uiautomator2 as u2

from Android_autoTest.conftest import logout


@allure.feature("deom测试")
def test_login(d, self=None):
    if d(resourceId="com.scores.tfz:id/image_cancel").wait(timeout=30):
        d(resourceId="com.scores.tfz:id/image_cancel").click()


