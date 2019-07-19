#-*-coding:utf-8-*-
# @time      :2019/1/2014:46
# @Author   :lemon_hehe
# @Email     :976621712@qq.com
# @File      :test_login.py
# @software:PyCharm Community Edition

import pytest

# if __name__ == '__main__':
# #     pytest.main(['-m smoke','--result-log=report/test.log',
# #                  '--junit-xml=report/test.xml',
# #                  '--html=report/test.html'])  #指定存放到那个目录下
# #   #--capture=no  不要捕获log，让控制台看起来更详细

if __name__ == '__main__':
    pytest.main(['-m smoke','--capture=no','--alluredir=allure'])

#测试报告  log,xml,html
#pip insatll allure-pytest
#下载好配置环境变量以后需要重启pycharm
#allure.serve  开启allure的服务
#在python中去使用allure
#运行完了之后需要去启动  allure serve allure报告的路径（allure serve I:\pyc\future-loans-master\test\allure
#selenium 的原理
#1--开启一个服务，通过python中的subprocess,自动运行了我们装在python下的驱动
#我们一开机可以让它自动运行allure，不一定要通过命令去运行
#可以自己去封装一个allure serve的服务
#urllib3  标准库
#jenkins  分布式