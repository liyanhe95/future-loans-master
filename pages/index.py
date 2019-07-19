#-*-coding:utf-8-*-
# @time      :2019/1/2014:46
# @Author   :lemon_hehe
# @Email     :976621712@qq.com
# @File      :test_login.py
# @software:PyCharm Community Edition

from selenium.webdriver.support.wait import WebDriverWait  # 显示等待
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base import BasePage


class IndexPage(BasePage):

    user_locator = (By.XPATH,'//img[@class="mr-5"]')
    #//a[@class="btn btn-special"]  因为python无法解析中间有空格的，所以需要在前面添加一个contains  注意：这是坑
    bid_ele_locator = (By.XPATH,'//a[contains(@class,"btn btn-special")]')

    #定位投资项目
    bid_project_locator = (By.XPATH,'//div[text()="投资项目"]')

    def get_user(self):
        # return WebDriverWait(self.driver,20).until(EC.visibility_of_element_located
        #                                            ((By.XPATH,'//img[@class="mr-5"]//..')))
        return self.get_visible_element(self.user_locator)

    def bid_project(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",self.get_bid_project())
        return self.get_bid_project()

    def bid(self):
        return self.get_bid_button.click()

    @property
    def get_bid_button(self):
        return self.get_visible_element(self.bid_ele_locator)

    def get_bid_project(self):
        project =  self.get_visible_element(self.bid_project_locator)
        return project



