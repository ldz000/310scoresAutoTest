import os
import time

import allure
import pytest
import uiautomator2 as u2

from Android_autoTest.conftest import logout

@allure.epic("球讯 自动化测试报告")
@allure.feature("页面的展示和点击")
def test_zhuanjia(device_factory):
        d = device_factory(app_key="app2")
        d.sleep(3)
        with allure.step("处理弹窗"):
                d(resourceId = "com.halo.fkkq:id/check_pro").wait(timeout=10)
                d(resourceId = "com.halo.fkkq:id/check_pro").click()
                d(text="同意").wait(timeout=10)
                d(text="同意").click()
                for i in range(2):
                        d.swipe(0.9, 0.5, 0.1, 0.5)
                d(text="立即体验").wait(timeout=10)
                d(text="立即体验").click()


        with allure.step("界面butter是否展示出来"):
                d(text = "专家").wait(timeout=10)
                d(text="专家").click()
                d(text="推荐").wait(timeout=10)
                assert d(text = "推荐").exists()
                d(text="私享").wait(timeout=10)
                assert d(text = "私享").exists()
                d(text="直播").wait(timeout=10)
                assert d(text = "直播").exists()
                d(text="榜单").wait(timeout=10)
                assert d(text = "榜单").exists()
                d(text="关注").wait(timeout=10)
                assert d(text = "关注").exists()
                d(text="足球").wait(timeout=10)
                assert d(text = "足球").exists()
                d(text="篮球").wait(timeout=10)
                assert d(text = "篮球").exists()
        with allure.step("点击验证"):
                d(text = "免费专区").wait(timeout=10)
                d(text = "免费专区").click()
                d(text = "每日公推专题").wait(timeout=10)
                assert d(text = "每日公推专题").exists()
                d.press("back")
                d(text="数据模型").wait(timeout=10)
                d(text="数据模型").click()
                d(text="模型").wait(timeout=10)
                assert d(text="模型").exists()
                d(text="专家").click()
                d(text="独家密报").wait(timeout=10)
                d(text="独家密报").click()
                d(text="密报").wait(timeout=10)
                assert d(text="情报").exists()
                d(text="专家").click()
                d(text="奖金计算").wait(timeout=10)
                d(text="奖金计算").click()
                d(text="竞足计算器").wait(timeout=10)
                assert d(text="竞足计算器").exists()
                d.press("back")
                d.sleep(2)

        with allure.step("比赛tab"):
                d(text = "比赛").click()
                d(text = "重要").wait(timeout=10)
                assert d(text = "重要").exists()
                d(text="足球").wait(timeout=10)
                assert d(text="足球").exists()
                d(text="篮球").wait(timeout=10)
                assert d(text="篮球").exists()
                d(text="全部").wait(timeout=10)
                assert d(text="全部").exists()
                d(text="重要").click()
                d(resourceId="com.halo.fkkq:id/image_left_icon").wait(timeout=10)
                assert d(resourceId="com.halo.fkkq:id/image_left_icon").exists()
                d(text="篮球").click()
                d(text="赛程").wait(timeout=10)
                assert d(text="赛程").exists()
                d.sleep(2)

        with allure.step("资讯tab"):
                d(resourceId="com.halo.fkkq:id/lottie_discover").click()
                d(resourceId= "com.halo.fkkq:id/constraint_info").wait(timeout=10)
                assert d(resourceId= "com.halo.fkkq:id/constraint_info").exists()
                d(text="资讯").click()
                d(text = "热门").wait(timeout=10)
                assert d(text = "热门").exists()
                d(resourceId="com.halo.fkkq:id/image_top_one").wait(timeout=10)
                d(resourceId="com.halo.fkkq:id/image_top_one").click()
                d(text="详情").wait(timeout=10)
                assert d(text="详情").exists()
                d.press("back")
                d(text = "最新").wait(timeout=10)
                d(text="最新").click()
                d(text="今天").wait(timeout=10)
                assert d(text="今天").exists()
                d.sleep(2)

        with allure.step("数据tab"):
                d(text="数据").click()
                d(text = "模型").wait(timeout=10)
                assert d(text = "模型").exists()
                d(text="红单模型").wait(timeout=10)
                assert d(text = "红单模型").exists()
                d(text="免费模型").wait(timeout=10)
                assert d(text="免费模型").exists()
                d(text = "数据库").click()
                d(text = "近期热门").wait(timeout=10)
                assert d(text = "近期热门").exists()
                d(text = "最近查看").wait(timeout=10)
                assert d(text = "最近查看").exists()
                d(text = "欧冠").wait(timeout=10)
                assert d(text = "欧冠").exists()
                d(text = "国际赛事",resourceId = "com.halo.fkkq:id/constraint").wait(timeout=10)
                d(text = "国际赛事",resourceId = "com.halo.fkkq:id/constraint").click()
                d(text = "国际赛事",recourceId = "com.halo.fkkq:id/tv_continent_name").wait(timeout=10)
                assert d(text = "国际赛事",recourceId = "com.halo.fkkq:id/tv_continent_name").exists()














