from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

# Web 控件的交互进阶
class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_case_click(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        # element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_click = self.driver.find_element(by=By.XPATH, value="//input[@value='click me']")
        element_doubleclick = self.driver.find_element(by=By.XPATH, value="//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element(by=By.XPATH, value="//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        sleep(3)
        action.perform()
        sleep(3)

    def test_movetoelement(self):
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element(by=By.XPATH, value='//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element(by=By.XPATH, value='//*[@id = "dragger"]')
        drop_element = self.driver.find_element(by=By.XPATH, value="/html/body/div[2]")

        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_element, drop_element).perform()
        # action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()

        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element(by=By.XPATH,value='/html/body/label[1]/input')
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

