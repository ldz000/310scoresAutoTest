import os
import time
from pydoc import classname

import allure
import pytest
import uiautomator2 as u2

from Android_autoTest.conftest import logout


@allure.feature("deom测试")
def test_login(d, self=None):
    with allure.step("搜索进入联赛主页"):
        time.sleep(5)
        d(resourceId="com.scores.tfz:id/sc_home_search_icon").wait(timeout=10)
        d(resourceId="com.scores.tfz:id/sc_home_search_icon").click()
        d(resourceId="com.scores.tfz:id/sc_search_edit_layout").wait(timeout=10)
        d(resourceId="com.scores.tfz:id/sc_search_et").send_keys("Premier League")
        time.sleep(2)
        d.press("enter")
        d(resourceId="com.scores.tfz:id/sc_tv_text", text="Leagues").wait(timeout=10)
        d(resourceId="com.scores.tfz:id/sc_tv_text", text="Leagues").click()

        d(resourceId="com.scores.tfz:id/sc_name2", text = "England").wait(timeout=10)
        d(resourceId="com.scores.tfz:id/sc_name2", text = "England").click()
        time.sleep(3)
        if d(resourceId="com.scores.tfz:id/sc_close_btn").exists():
                d(resourceId="com.scores.tfz:id/sc_close_btn").click()
        d(resourceId="com.scores.tfz:id/sc_league_match_location", text = "England").wait(timeout=10)
        with allure.step("判断联赛图标和地区是否展示"):
            assert d(resourceId="com.scores.tfz:id/sc_league_match_location", text = "England").exists()
            assert d(resourceId="com.scores.tfz:id/sc_country_logo").exists()
        with allure.step("验证tab是否可滑动"):
            time.sleep(2)
            assert d(text="Fixtures").exists()
            d.swipe(0.914, 0.233, 0.253, 0.233)
            d(text="Players").wait(timeout=10)
            assert d(text="Players").exists()
        with allure.step("通过页面是否加载成功"):
            d.swipe(0.5, 0.9, 0.914, 0.08)
            assert d(text="News").exists()
            d.swipe(0.5, 0.9, 0.914, 0.08)
            assert d(text="Top Scorers").exists()
            assert d(text="Goal Ranking").exists()








    time.sleep(5)



