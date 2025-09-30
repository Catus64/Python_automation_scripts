import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='RR8T904NMKL',
    appPackage='com.convep.commudesk',
    appActivity='com.qms_owner.MainActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_apps(self) -> None:
        #el = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="Search settings"]')
        #el.click()
        time.sleep(100000)

if __name__ == '__main__':
    unittest.main()