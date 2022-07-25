import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestTestdemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        # 复用浏览器
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown_method(self, method):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get("http://www.baidu.com")
        sleep(3)

    def test_weixin(self):
        self.driver.find_element(By.ID, "menu_contacts").click()
        sleep(3)

    def test_cookie(self):
        # get_cookies() 可以获取当前打开的页面的 cookies 信息
        # add_cooike() 可以把 cookies 添加到当前的页面中去
        # cookies = self.driver.get_cookies()
        # print(cookies)
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': '_REHu-sLVwAxrDLNq4mZPzTIddJnSqT6gy4FqVJuN12aqLOAmgWWKFDSvmgXwl3J5ENx93qJr7yAL60A2EpCVXyTulJ0hKIXnSwBbWmk_0okBL5QK5YQ0ijRurB0aeVrs2tBI_L_THNzmK-bkoh9dJBNmoWX9X3_GE6bmm4DlJJvBj_E7znLWGAHIrFXthFngqKduX3WeM6fVYr7mNSJMJkBl8KfV9gjAlGX7HZ3-EdWGWEYhmk2oHUxU4SONdMjGQw8cQmPRHtlaZfMF9nxLQ'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'KjId6VH248uqYDZrJMpKnF-8bJz5N1h2-AuHbxtkY5dAKFiMo2MDrRQZCrQherLZ'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a3467662'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'secure': False,
             'value': 'true'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688856374346826'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325819985320'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688856374346826'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '9506368000'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1684396803, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 2147483645, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '51c4718c4416bec77a1f1b689cb6336cdd8d9562ce81359f7f8ffbe2905c0aa1'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'leYoxl9C7r'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1655526179, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '5478101682578433'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
             'value': ''},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '3019739136'}]
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?index")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        # self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?index")
        # print(cookies)
        sleep(5)

    def test_shelve(self):
        # shelve python 内置模块， 专门用来对数据进行持久化存储的库，相当于小型的数据库
        # 可以通过 key， value 来把数据保存到 shelve中
        # 读取cookie

        db = shelve.open("cookies")
        cookies = db['cookie']
        db.close()

        # 利用读取的cookie 完成登录操作
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

        # 找到“导入通讯录”按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()

        # 上传
        # 定位 “文件上传”这个元素，只能选择 input 标签内的
        # 通过 input 标签实现的上传功能，可以将其看作是一个输入框，即通过send_keys()指定本地文件路径的方式实现文件上传。
        # 参考文章 https://www.cnblogs.com/newsss/p/13358280.html
        self.driver.find_element(By.CSS_SELECTOR, "#js_upload_file_input").send_keys("D:\study\mydata.xlsx")

        # 验证 上传文件名
        # filename = self.driver.find_element(By.XPATH,value='//*[@id="upload_file_name"]').text
        # filename = self.driver.find_element(By.ID, value='upload_file_name').text
        filename = self.driver.find_element(By.CSS_SELECTOR,"#upload_file_name").text
        assert "mydata.xlsx" == filename
        # sleep(3)

        db.close()
