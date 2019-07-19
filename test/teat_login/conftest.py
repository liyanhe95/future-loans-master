#-*-coding:utf-8-*-
# @time      :2019/1/2014:46
# @Author   :lemon_hehe
# @Email     :976621712@qq.com
# @File      :test_login.py
# @software:PyCharm Community Edition
#conftest 是固定的格式，不可以改的。pytest只要建立了这样的一个文件，它就在这个文件里面来找
#根本不需要导入，直接使用usefixtures,它就会自己去找fixture
#我们的环境不是用来和测试用来绑定的
import pytest
from selenium import webdriver
from pages.login import LoginPage

@pytest.fixture
def init_driver():
    #这是一个函数
    print('begin driver')
    driver = webdriver.Chrome()
    driver.get("http://120.78.128.25:8765/Index/login.html")
    driver.maximize_window()
    login_page = LoginPage(driver)

    #yield出来，才可以在其他页面使用
    yield  (driver,login_page)#在执行yield的时候会执行测试用例，执行完测试用例在执行quit driver（生成器）

    print('quit driver')
    driver.quit()


#return可以终止一个函数，而yield可以接着执行
@pytest.fixture('class')
#可以实现setupclass
def my_set_class():
    #只会在某个类里面去执行一次
    print('begin my class')
    driver = webdriver.Chrome()
    driver.get("http://120.78.128.25:8765/Index/login.html")
    driver.maximize_window()
    login_page = LoginPage(driver)

    yield (driver,login_page)

    print('finish my class')
    driver.quit()

@pytest.fixture('session',autouse=False)
#autouse=True
#如果是true，只要定义了就会自动执行，根本不需要去加装饰器
def my_session():
    pass