from selenium import webdriver


def test_driver():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")