from appium import webdriver
import os

app_path = "/Users/mehmettop/Desktop/iOS-Development/AppiumTestApp/Target/AppiumTestApp-fduddtambqialkhkjdcxyrxgiabp/Build/Products/Debug-iphonesimulator/AppiumTestApp.app"
#udid = "<your udid>"
platformVersion = "10.2"
deviceName = "iPhone 7 Plus"

success = True
desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = platformVersion
desired_caps['deviceName'] = deviceName
#desired_caps['udid'] = udid
desired_caps['automationName'] = 'XCUITest'
desired_caps['realDeviceLogger'] = 'idevicesyslog'
desired_caps['app'] = os.path.abspath(app_path)

wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)

try:
	wd.find_element_by_xpath("//XCUIElementTypeButton[@name='OK']").click()
	wd.find_element_by_xpath("//XCUIElementTypeTextField[1]").send_keys("123")
finally:
	wd.quit()
	if not success:
		raise Exception("Test failed.")
