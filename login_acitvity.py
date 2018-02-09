#coding=utf-8
from appium import webdriver;
'''
{
  "deviceName": "Android Emulator",
  "automationName": "Appium",
  "platformName": "Android",
  "appPackage": "com.laiqian.diamond",
  "appActivity": "com.laiqian.login.view.LoginActivity",
  "app": "/Users/emery/AndroidStudioProjects/fastfood_trunk_studio/app/lqkProd/release/fastfood_lqkProdRelease_13.441_0208_2134.apk",
  "platformVersion": "4.4"
}
'''

desired_caps = {}
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['automationName'] = 'Appium'
desired_caps['platformName'] = 'Android'
desired_caps['appPackage'] = 'com.laiqian.diamond'
desired_caps['appActivity'] = 'com.laiqian.login.view.LoginActivity'
desired_caps['app'] = '/Users/emery/AndroidStudioProjects/fastfood_trunk_studio/app/lqkProd/release/fastfood_lqkProdRelease_13.441_0208_2134.apk'
desired_caps['platformVersion'] = '4.4'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id("com.laiqian.diamond:id/l_userPhone").send_keys("20170502999")
driver.find_element_by_id("com.laiqian.diamond:id/l_password").send_keys("123456")
driver.find_element_by_id("com.laiqian.diamond:id/tvLoginLable").click()

