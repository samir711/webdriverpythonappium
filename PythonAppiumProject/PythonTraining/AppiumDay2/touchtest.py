import os
from appium import webdriver

apk_path = "\\PythonTraining\\data\\apk_files\\AndroidUI.apk"


os.chdir("..\..")
cwd = os.getcwd()
my_dir = cwd + apk_path
print(my_dir)

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = 'VKN7N15C29029254'
desired_caps['app'] = my_dir
desired_caps['appPackage']="com.android.androidui"
desired_caps['appActivity']="com.android.androidui.MainActivity"

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
showAlert=driver.find_element_by_id("com.android.androidui:id/buttonAlert")
showAlert.click()
yes=driver.find_element_by_id("android:id/button1")
yes.click()