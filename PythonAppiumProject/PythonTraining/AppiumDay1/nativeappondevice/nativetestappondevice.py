import unittest
import os
from appium import webdriver

apk_path = "\\data\\apk_files\\testApp\\testApp.apk"
# apk_path = ".\..\..\\data\\apk_files\\testApp\\testApp.apk"

os.chdir("..\..")
cwd = os.getcwd()
my_dir = cwd + apk_path
print(my_dir)

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = 'VKN7N15C29029254'
# desired_caps['avd'] = "VKN7N15C29029254"
desired_caps['avdLaunchTimeout'] = 150000
desired_caps['app'] = my_dir
desired_caps['appPackage'] = "com.example.testapp"
desired_caps['appActivity'] = "MainActivity"

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_id("com.example.testapp:id/urlField").send_keys("https://www.google.com")
driver.find_element_by_id("com.example.testapp:id/goButton").click()
print(driver.page_source)