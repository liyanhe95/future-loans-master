#-*-coding:utf-8-*-
# @time      :2019/1/2014:46
# @Author   :lemon_hehe
# @Email     :976621712@qq.com
# @File      :test_login.py
# @software:PyCharm Community Edition
import pytest
from selenium import webdriver
from pages.login import LoginPage
from data import login_message
from pages.index import IndexPage
from pages.bid import BidPage
@pytest.fixture
#每个测试用例所对应的环境可能是不一样的，
#如果要使用pytest的环境管理，那么就不要使用unittest，尤其不可以和ddt一起使用
def init_driver():
    print('begin driver')
    driver = webdriver.Chrome()
    driver.get("http://120.78.128.25:8765/Index/login.html")
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.submit_userinfo(login_message.user_corrent[0]["phone"], login_message.user_corrent[0]["password"])
    index_page = IndexPage(driver)
    bid_page = BidPage(driver)

    yield  (driver,index_page,bid_page)
    #在执行yield地时候会执行测试用例，执行完测试用例在执行quit driver（生成器）
    #yield 后面可以return一些东西，生成器的概念
    print('quit driver')
    driver.quit()