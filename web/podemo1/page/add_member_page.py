from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.podemo1.page.base_page import BasePage


class AddMemberPage(BasePage):

    # def __init__(self,driver:WebDriver):
    #     self.driver = driver

    def add_member(self,username,account,phonenum):

        # sleep(3)
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        self.find(By.CSS_SELECTOR,".js_btn_save").click()
        sleep(3)

        # checkbox = (By.CSS_SELECTOR,".ww_checkbox")
        # self.wait_for_click(checkbox)
        return True

    def get_member(self):
        # 验证联系人添加成功
        contactlist = self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        titlelist = [element.get_attribute("title") for element in contactlist]
        print(titlelist)
        # titlelist = []
        # for element in contactlist:
        #     titlelist.append(element.get_attribute("title"))

        # while True:
        #     contactlist = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        #     titlelist = [element.get_attribute("title") for element in contactlist]
        #     print(titlelist)
        #
        #     result = self.find(By.CSS_SELECTOR,'.')

        return titlelist