from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://home.testing-studio.com/")
        self.driver.implicitly_wait(3)

    def test_wait(self):
        self.driver.find_element(By.XPATH,'//*[@title="按类别分组的所有话题"]').click()
        # sleep(3)
        self.driver.find_element(By.XPATH,'//*[@title="过去一年、一个月、一周或一天中最活跃的话题"]').click()
        print("hello")