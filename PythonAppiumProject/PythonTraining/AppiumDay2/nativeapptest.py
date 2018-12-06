import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['browserName']='Chrome'
# desired_caps['deviceName'] = 'LGK420fa0e66a'

desired_caps['deviceName'] = 'VKN7N15C29029254'

#LOGIN LOGOUT 5ELEMENTSLEARNING DEMOSITE
driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.get("http://5elementslearning.com/demosite") # open the browser with the url
driver.find_element_by_link_text("My Account").click()
driver.find_element_by_name("email_address").send_keys("samirdoc1@gmail.com") # sendkeys , type on the text box
driver.find_element_by_name("password").send_keys("vijay1980")

#sometimes we need to resort to mouse and keyboard actions when we are unable to use any other locator method
#Click on the Sign in button
driver.press_keycode(61); #press tab
driver.press_keycode(61); #press tab
driver.press_keycode(66); #press enter
#use another locator or approach to work.
driver.find_element_by_id("tdb4").click()
driver.find_element_by_id("tdb4").click()
# time.sleep(1000)
driver.quit()