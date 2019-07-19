#-*-coding:utf-8-*-
# @time      :2019/1/2014:46
# @Author   :lemon_hehe
# @Email     :976621712@qq.com
# @File      :test_login.py
import pytest
from pages.index import IndexPage
from data import login_message
#web  UI 自动化测试效率不高（而接口自动化测试效率很高），因为每次开关浏览器的时间太长了
#提供自动化测试的效率，每次只需要开关一次浏览器就OK了
#pytest是需要安装才可以使用，而unittest是直接集成在python里面的，直接导入就可以使用
#pytest的用法比unittest复杂一些
#pytest  1--可以标记（mark）用例，只需执行指定的标记就好了
#2--pytest不需要入口，自动发现用例
#3--断言（assert），断言变得更加简单
#4---环境管理更灵活
#5--与unittest是兼容的，pytest与unittest是共存的
#6--不导入unittest直接用setup或tearDown是不可以的
#7--提供了很多的插件，pytest-allure，支持几百种这样的插件
#8--可以在类上面添加all，（pytest.mark.all）,还可以进行逻辑运算，and,or,not
#9--pytest-help
#10---unittest测试用例要以test开头，或test结尾的
#如果要运行的是test里面的，类就要以test开头
#注意类里面不能含有init这样的一个函数，如果出现了init，会表示这不是一个测试用例的类
#函数一定要以test开头，与unittest一样
#可以修改pytest里面的规则
#pytest有自动识别这个测试用例的功能，无非就是你定义一个配置，根据配置去找
#pip install returnfailures   重运行机制
#pytest--reruns  重试次数
#pytest --reruns 2:运行失败的用例可以重新运行第二次
#pytest --reruns 2 --reruns-delay 5 表示失败的用例可以重新运行2次。第一次和第二次的时间间隔为2秒
# @ddt
class TestLogin():

    def setUp(self):
        # self.driver = webdriver.Chrome()
        # self.driver.get("http://120.78.128.25:8765/Index/login.html")
        # self.driver.maximize_window()
        # self.login_page = LoginPage(self.driver)
        pass
    @pytest.mark.login  #（标记的名称）
    @pytest.mark.smoke  #冒烟用例
    @pytest.mark.usefixtures('init_driver')
    # @data(*login_message.user_corrent)
    @pytest.mark.parametrize('data',login_message.user_corrent)
    #定义data的参数名称，前面没有星号了
    def test_login_sucess(self,data,init_driver):
        #从conftest里面取出来，init_driver代表的yield出来的两个值
        driver,login_page = init_driver
        login_page.submit_userinfo(data['phone'],data['password'])
        # 找到账户的元素
        user_ele = IndexPage(driver).get_user()
        print(user_ele.text)
        assert (data['expected'] == user_ele.text)
        # print(user_ele.text)

    def tearDown(self):
        # self.driver.quit()
        pass





