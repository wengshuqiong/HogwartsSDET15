from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# noReset fullReset 是否在测试前后重置相关环境（例如首次打开弹框，或者时登录信息）
# dontStopAppOnReset 首次启动的时候，不停止 app（可以调试或者运行的时候提升运行速度）
# skipDeviceInitialization 跳过安装，权限设置等操作（可以调试或者运行的时候提升运行速度）

desire_cap = {
    "platformName": "android",
    "appium:deviceName": "127.0.0.1:7555",
    "appium:appPackage": "com.xueqiu.android",
    "appium:appActivity": ".view.WelcomeActivityAlias",
    "appium:noReset": "true",
    "appium:dontStopAppOnReset": "true"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
driver.implicitly_wait(10)


