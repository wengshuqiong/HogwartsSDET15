from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions



class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        self.driver.get("http://www.baidu.com")
        el = self.driver.find_element_by_id("kw")
        ele_seach = self.driver.find_element_by_xpath('//*[@value="百度一下"]')

        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(ele_seach)
        action.perform()

        action.scroll_from_element(el, 0, 10000).perform()