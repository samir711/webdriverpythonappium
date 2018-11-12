import unittest

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['avd'] = "DemoNexus"
desired_caps['avdLaunchTimeout'] = 150000
desired_caps['appPackage'] = "com.android.calculator2"
desired_caps['appActivity'] = "com.android.calculator2.Calculator"

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # passing the url of appium server, and the desired cap object

driver.find_element_by_id("com.android.calculator2:id/digit_5").click()
driver.find_element_by_id("com.android.calculator2:id/op_add").click()
driver.find_element_by_id("com.android.calculator2:id/digit_6").click()
driver.find_element_by_id("com.android.calculator2:id/eq").click()
res = driver.find_element_by_id("com.android.calculator2:id/result").text

print(res)
if int(res) == 11:
    print("pass")
else:
    print("fail")
