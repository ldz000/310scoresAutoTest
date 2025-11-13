import os
import time

import allure
import pytest
import uiautomator2 as u2

from Android_autoTest.conftest import logout


@allure.epic("310scores Android 自动化测试报告")
@allure.feature("登录测试(推送远程仓库)")
def test_login(d, self=None):
    with allure.step("处理系列弹窗中......."):
        #判断got it 弹窗是否存在
        if d(text="Got It").wait(timeout=20):
            d(text="Got It").click()
        #去掉启动广告
            # for i in range(0, 3):
            #     time.sleep(6)
            #     if not d(text="matches").exists():
            #         d.click(0.929, 0.087)
    time.sleep(2)
    #处理选择球队
    if d(text = "Skip").wait(timeout=10):
        d(text ="Skip").click()
    time.sleep(2)
    #处理允许弹窗
    if d(text = "允许").wait(timeout=10):
        d(text ="允许").click()
    # 关闭活动弹窗
    time.sleep(2)
    if d(resourceId="com.scores.tfz:id/image_cancel").wait(timeout=30):
        d(resourceId="com.scores.tfz:id/image_cancel").click()
    with allure.step("弹窗处理成功，进入首页"):
        time.sleep(2)
        # 点击左上角头
        d(resourceId="com.scores.tfz:id/image_header").click()
        time.sleep(2)
        # 点击登录按钮
        d(resourceId="com.scores.tfz:id/sc_sign_in_tx").wait(timeout=20)
        d(resourceId="com.scores.tfz:id/sc_sign_in_tx").click()
        time.sleep(2)
    # with allure.step("准备用谷歌账号登录"):
    #     # 谷歌账号登录
    #     d(resourceId="com.scores.tfz:id/tv_google").wait(timeout=20)
    #     d(resourceId="com.scores.tfz:id/tv_google").click()
    #     d(text="LDZ").wait(timeout=20)
    #     d(text="LDZ").click()
    #     time.sleep(10)
    # with allure.step("检测谷歌邮箱登录是否成功"):
    #     assert not d(resourceId="com.scores.tfz:id/tv_google").exists()
    # with allure.step("谷歌账号登录成功,返回到首页"):
    #     time.sleep(2)
    #     d(resourceId="com.scores.tfz:id/sc_close_btn").click()
    # with allure.step("退出谷歌登录账号"):
    #     # 退出登录
    #     logout()
    with allure.step("准备切换邮件登录"):
        d.press("back")
        time.sleep(2)
        # 邮箱登录
        d(resourceId="com.scores.tfz:id/tv_email").click()
        time.sleep(2)
        d(resourceId="com.scores.tfz:id/et_address").send_keys("1020209073@test.com")
        time.sleep(2)
        d(text="Next").click()
        with allure.step("验证正确密码登录成功"):
            time.sleep(2)
            d(resourceId="com.scores.tfz:id/et_password").send_keys("654321")
            time.sleep(2)
            d(text="Enter").click()
            time.sleep(3)
            assert d(resourceId="com.scores.tfz:id/tv_sign_in_to").exists()
        with allure.step("验证正确密码登录成功"):
            time.sleep(2)
            d(resourceId="com.scores.tfz:id/et_password").clear_text()
            time.sleep(3)
            d(resourceId="com.scores.tfz:id/et_password").send_keys("123456")
            time.sleep(2)
            d(text="Enter").click()
            time.sleep(3)
            assert not d(resourceId="com.scores.tfz:id/tv_sign_in_to").exists()
            time.sleep(2)
    with allure.step("登录验证成功，返回首页"):
        d(resourceId="com.scores.tfz:id/sc_close_btn").click()
        time.sleep(2)

#vpn太慢，充值会员已注释
# @allure.feature("金币/会员支付")
# def test_pay(d, self=None):
#     with allure.step("验证金币充值"):
#         time.sleep(10)
#         #去掉启动广告
#         for i in range(0, 3):
#             time.sleep(6)
#             if not d(text="matches").exists():
#                 d.click(0.929, 0.087)
#         # 点击左上角头像
#         d(resourceId="com.scores.tfz:id/image_header").click()
#         time.sleep(2)
#         d(text="Earn more here").click()
#         time.sleep(8)
#         d(text="Recharge").click()
#         time.sleep(2)
#         current_balance = float(d(resourceId="com.scores.tfz:id/sc_my_balance_gold_num").get_text())
#         print(current_balance)
#         time.sleep(2)
#         d(text="Charge now").click()
#         time.sleep(5)
#         d(text="一键购买").click()
#         time.sleep(8)
#         for i in range(0,3):
#             d.press("back")
#             if d(text="Recharge").exists():
#                 break
#         time.sleep(6)
#         expect_balance = float(d(resourceId="com.scores.tfz:id/sc_points_score_gold_num").get_text())
#         print(expect_balance)
#         time.sleep(2)
#         assert expect_balance == current_balance+200.0
#     with allure.step("验证购买会员"):
#         time.sleep(2)
#         d.press("back")
#         time.sleep(2)
#         d(text="Learn more here").click()
#         time.sleep(2)
#         d(text="BECOME A PRO").click()
#         time.sleep(6)
#         d(text="订阅").click()
#         time.sleep(5)
#         d(resourceId="com.scores.tfz:id/image_cancel").click()
#         time.sleep(5)
#         d.press("back")
#         time.sleep(6)
#         assert d(resourceId="com.scores.tfz:id/sc_my_vip_icon").exists()
#         time.sleep(1)
#         d.press("back")
#         time.sleep(2)

@allure.feature("国家语言切换")
def test_fllow(d, self=None):
    d.app_stop("com.scores.tfz")
    d.app_start("com.scores.tfz")
    time.sleep(10)
    if d(text="Matches").exists():
        time.sleep(2)
    else:
        # 去掉启动广告
        for i in range(0, 3):
            time.sleep(6)
            if not d(text="matches").exists():
                d.click(0.929, 0.087)
    with allure.step("验证英语：highlight和all展示出来"):
        time.sleep(3)
        assert d(resourceId="com.scores.tfz:id/tv_content",text="HIGHLIGHTS").exists()
        time.sleep(2)
        assert d(resourceId="com.scores.tfz:id/tv_content", text="ALL").exists()
        time.sleep(2)
        #点击左上角头像
        d(resourceId="com.scores.tfz:id/image_header").click()
        time.sleep(2)
        d(text="Settings and Privacy").click()
        time.sleep(2)
        d(text="Language").click()
        time.sleep(2)
    with allure.step("验证葡语：highlight和all展示出来"):
        #切换为葡语
        d(resourceId="com.scores.tfz:id/sc_language_tx_Portuguese").click()
        time.sleep(5)
        assert d(resourceId="com.scores.tfz:id/tv_content", text="DESTAQUES").exists()
        time.sleep(2)
        assert d(resourceId="com.scores.tfz:id/tv_content", text="TODAS").exists()
        time.sleep(2)
        d(resourceId="com.scores.tfz:id/image_header").click()
        time.sleep(2)
        d(text="Configurações e Privacidade").click()
        time.sleep(2)
        d(text="Idioma").click()
        time.sleep(2)
    with allure.step("验证越南语：highlight和all展示出来"):
        #切换为越南语
        d(text="Vietnamita - Tiếng Việt").click()
        time.sleep(5)
        assert d(resourceId="com.scores.tfz:id/tv_content", text="ĐIỂM NỔI BẬT").exists()
        time.sleep(2)
        assert d(resourceId="com.scores.tfz:id/tv_content", text="TẤT CẢ").exists()
        time.sleep(2)
        d(resourceId="com.scores.tfz:id/image_header").click()
        time.sleep(2)
        d(text="Cài đặt và Quyền riêng tư").click()
        time.sleep(2)
        d(text="Ngôn ngữ").click()
        time.sleep(2)
    with allure.step("验证印尼语：highlight和all展示出来"):
        #切换为印尼语
        d(text="Tiếng Indo - Bahasa Indonesia").click()
        time.sleep(5)
        assert d(resourceId="com.scores.tfz:id/tv_content", text="SEMUA").exists()
        time.sleep(2)
        d(resourceId="com.scores.tfz:id/image_header").click()
        time.sleep(2)
        d(text="Pengaturan dan Privasi").click()
        time.sleep(2)
        d(text="Bahasa").click()
        time.sleep(2)
        #回到英语
        d(text="Inggris - English").click()

@allure.feature("新闻模块")
def test_news(d, self=None):
    d.app_stop("com.scores.tfz")
    d.app_start("com.scores.tfz")
    time.sleep(10)
    if d(text="Matches").exists():
        time.sleep(2)
    else:
        # 去掉启动广告
        for i in range(0, 3):
            time.sleep(6)
            if not d(text="matches").exists():
                d.click(0.929, 0.087)
    with allure.step("新闻跳转summer页"):
        time.sleep(6)
        d(resourceId="com.scores.tfz:id/sc_news_animation_icon").click()
        # 等待新闻加载出
        d(resourceId="com.scores.tfz:id/sc_image_type_video").wait(timeout=10)
        time.sleep(3)
        d(resourceId="com.scores.tfz:id/sc_image_type_video").click()
        time.sleep(3)
    with allure.step("验证新闻标签存在"):
        assert d(resourceId="com.scores.tfz:id/text_hot_flow").exists()
        time.sleep(2)
    with allure.step("验证标签右边按钮点击"):
        ele = d.xpath(
            '//*[@resource-id="com.scores.tfz:id/sc_relates_recycler_view"]/android.view.ViewGroup[4]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]').wait(
            timeout=10)
        if ele:
            d.xpath(
                '//*[@resource-id="com.scores.tfz:id/sc_relates_recycler_view"]/android.view.ViewGroup[4]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]').click()
            time.sleep(2)
            d.press("back")
        time.sleep(2)
    with allure.step("验证新闻评论/点赞"):
        d(resourceId="com.scores.tfz:id/sc_like_num").wait(timeout=10)
        current_balance = float(d(resourceId="com.scores.tfz:id/sc_like_num").get_text())
        d.xpath(
            '//*[@resource-id="com.scores.tfz:id/sc_like_inner_layout"]/android.view.View[1]').click()
        next_balance = float(d(resourceId="com.scores.tfz:id/sc_like_num").get_text())
        assert next_balance > current_balance
        #取消点赞，防止下次是取消点赞
        d.xpath(
            '//*[@resource-id="com.scores.tfz:id/sc_like_inner_layout"]/android.view.View[1]').click()
    with allure.step("验证新闻评论/点赞"):
        timestamp = time.strftime("%Y-%m-%d %H", time.localtime())
        d.xpath(
            '//*[@resource-id="com.scores.tfz:id/sc_comment_layout"]/android.view.View[1]').click()
        d(resourceId="com.scores.tfz:id/sc_input_tx_btn").wait(timeout=10)
        d(resourceId="com.scores.tfz:id/sc_input_tx_btn").click()
        d(resourceId="com.scores.tfz:id/et_msg_content").send_keys(f"scores_{timestamp}")
        d(resourceId="com.scores.tfz:id/sc_send_btn").click()
        time.sleep(5)
        assert d(resourceId="com.scores.tfz:id/sc_comment_content",text=f"scores_{timestamp}").exists()


    # with allure.step("验证summere页广告加载"):
    #     for i in range(0, 4):
    #         time.sleep(2)
    #         d.swipe(0.5, 0.8, 0.5, 0.2, duration=0.2)
    #     time.sleep(3)
    #     d(resourceId="com.scores.tfz:id/native_ad_view").wait(timeout=10)
    #     assert d(resourceId="com.scores.tfz:id/native_ad_view").exists()
    #     time.sleep(3)

@allure.feature("比赛详情页")
def test_match(d, self=None):
    d.app_stop("com.scores.tfz")
    d.app_start("com.scores.tfz")
    time.sleep(10)
    if d(text="Matches").exists():
        time.sleep(2)
    else:
        # 去掉启动广告
        for i in range(0, 3):
            time.sleep(6)
            if not d(text="matches").exists():
                d.click(0.929, 0.087)
    with allure.step("通过进入比赛详情页"):
        d(resourceId="com.scores.tfz:id/sc_home_search_icon").wait(timeout=10)
        d(resourceId="com.scores.tfz:id/sc_home_search_icon").click()
        d(resourceId="com.scores.tfz:id/sc_search_et").wait(timeout=10)
        d(resourceId="com.scores.tfz:id/sc_search_et").click()
        d(resourceId="com.scores.tfz:id/sc_search_et").send_keys("CR Flamengo")
        d(text="Teams").wait(timeout=10)
        d(text="Teams").click()
        d(resourceId="com.scores.tfz:id/sc_player_name_tx", text="Flamengo").wait(timeout=10)
        d(resourceId="com.scores.tfz:id/sc_player_name_tx", text="Flamengo").click()
        with allure.step("<进入球队主页"):
            time.sleep(3)
            if d(resourceId="com.scores.tfz:id/sc_close_btn").exists():
                d(resourceId="com.scores.tfz:id/sc_close_btn").click()
            d(text="Matches").wait(timeout=10)
            d(text="Matches").click()
            d(text="All").wait(timeout=10)
            d(text="All").click()
            d(text="CONMEBOL Copa Libertadores").wait(timeout=10)
            d(text="CONMEBOL Copa Libertadores").click()
        with allure.step("<进入比赛详情页"):
            d(text="Deportivo Tachira").wait(timeout=10)
            d(text="Deportivo Tachira").click()
            d(text="Live Match").wait(timeout=10)
            d(text="Live Match").click()
        with allure.step("动画直播正常播放"):
            time.sleep(10)
            if d(resourceId="com.scores.tfz:id/image_ad_close").exists():
                d(resourceId="com.scores.tfz:id/image_ad_close").click()
            time.sleep(5)
            assert d(resourceId="com.scores.tfz:id/toolbar_layout").exists()
        # with allure.step("聊天室发消息"):
        #     time.sleep(2)
        #     d.swipe(0.89, 0.33, 0.11, 0.33)
        #     d(text="Chat").wait(timeout=10)
        #     d(text="Chat").click()
        #     d(resourceId="com.scores.tfz:id/et_msg_content").wait(timeout=10)
        #     d(resourceId="com.scores.tfz:id/et_msg_content").send_keys("ff")
        #     d.press("enter")

@allure.feature("联赛主页")
def test_competion(d, self=None):
    d.app_stop("com.scores.tfz")
    d.app_start("com.scores.tfz")
    time.sleep(10)
    if d(text="Matches").exists():
        time.sleep(2)
    else:
        # 去掉启动广告
        for i in range(0, 3):
            time.sleep(6)
            if not d(text="matches").exists():
                d.click(0.929, 0.087)
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

@allure.feature("球队主页")
def test_team(d, self=None):
    d.app_stop("com.scores.tfz")
    d.app_start("com.scores.tfz")
    time.sleep(10)
    if d(text="Matches").exists():
        time.sleep(2)
    else:
        # 去掉启动广告
        for i in range(0, 3):
            time.sleep(6)
            if not d(text="matches").exists():
                d.click(0.929, 0.087)
    with allure.step("通过搜索进入球队主页"):
        time.sleep(5)
        d(resourceId="com.scores.tfz:id/sc_home_search_icon").wait(timeout=10)
        d(resourceId="com.scores.tfz:id/sc_home_search_icon").click()
        d(resourceId="com.scores.tfz:id/sc_search_edit_layout").wait(timeout=10)
        d(resourceId="com.scores.tfz:id/sc_search_et").send_keys("Chelsea")
        time.sleep(2)
        d.press("enter")
        d(resourceId="com.scores.tfz:id/sc_tv_text", text="Teams").wait(timeout=10)
        d(resourceId="com.scores.tfz:id/sc_tv_text", text="Teams").click()
        d(resourceId="com.scores.tfz:id/sc_player_name_tx", text="Chelsea").wait(timeout=10)
        d(resourceId="com.scores.tfz:id/sc_player_name_tx", text="Chelsea").click()
        d(text="Fixtures").wait(timeout=10)
        assert d(text="Fixtures").exists()

@allure.feature("球员主页")
def test_player(d, self=None):
    d.app_stop("com.scores.tfz")
    d.app_start("com.scores.tfz")
    time.sleep(10)
    if d(text="Matches").exists():
        time.sleep(2)
    else:
        # 去掉启动广告
        for i in range(0, 3):
            time.sleep(6)
            if not d(text="matches").exists():
                d.click(0.929, 0.087)
    with allure.step("通过搜索进入球队主页"):
        time.sleep(5)
        d(resourceId="com.scores.tfz:id/sc_home_search_icon").wait(timeout=10)
        d(resourceId="com.scores.tfz:id/sc_home_search_icon").click()
        d(resourceId="com.scores.tfz:id/sc_search_edit_layout").wait(timeout=10)
        d(resourceId="com.scores.tfz:id/sc_search_et").send_keys("Moises Caicedo")
        time.sleep(2)
        d.press("enter")
        d(resourceId="com.scores.tfz:id/sc_tv_text", text="Players").wait(timeout=10)
        d(resourceId="com.scores.tfz:id/sc_tv_text", text="Players").click()
        time.sleep(2)
        d(text="Chelsea - Ecuador").wait(timeout=10)
        d(text="Chelsea - Ecuador").click()
        time.sleep(5)
        if d(resourceId="com.scores.tfz:id/image_ad_close").exists():
            d(resourceId="com.scores.tfz:id/image_ad_close").click()
        d(text="Premier League · League · Round 8").click()
        d(text="Premier League · League · Round 8").wait(timeout=10)
        assert d(text="Premier League · League · Round 8").exists()

@allure.feature("日历")
def test_calendar(d, self=None):
    d.app_stop("com.scores.tfz")
    d.app_start("com.scores.tfz")
    time.sleep(10)
    if d(text="Matches").exists():
        time.sleep(2)
    else:
        # 去掉启动广告
        for i in range(0, 3):
            time.sleep(6)
            if not d(text="matches").exists():
                d.click(0.929, 0.087)
    d(text = "TODAY").wait(timeout=10)
    assert d(text="TODAY").exists()
    d(resourceId = "com.scores.tfz:id/sc_calendar_icon_tx").wait(timeout=10)
    d(resourceId = "com.scores.tfz:id/sc_calendar_icon_tx").click()
    time.sleep(2)
    assert d(text = "Back to today").exists()







# if __name__ == "__main__":
#     pytest.main(["--alluredir=./reports/allure_results"])
#     os.system("allure serve ./reports/allure_results")
#     os.system("allure generate ./reports/allure_results -o ./reports/allure_html")

# #捕获异常
#     try:
#         d(resourceId="com.example:id/btn_login").click()
#         print("元素存在且已点击")
#     except UiObjectNotFoundError:
#         print("元素不存在")



    # 测试数据参数化
    # @pytest.mark.parametrize("username, password, expected", [
    #     ("valid_user", "correct_password", True),  # 正确账号
    #     ("invalid_user", "123456", False),  # 错误账号
    #     ("", "", False),  # 空输入
    # ])

    # # 输入用户名和密码（根据实际 UI 元素修改定位方式）
    # d(resourceId="com.example.app:id/username").set_text(username)
    # d(resourceId="com.example.app:id/password").set_text(password)
    #
    # # 点击登录按钮
    # d(resourceId="com.example.app:id/login_btn").click()
    #
    # # 验证结果
    # if expected:
    #     # 登录成功：检查是否跳转到首页
    #     assert d(text="首页").exists(timeout=10)
    # else:
    #     # 登录失败：检查错误提示
    #     assert d(text="用户名或密码错误").exists(timeout=5)