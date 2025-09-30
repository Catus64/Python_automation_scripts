from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.client_config import AppiumClientConfig
import time

SERVER_URL_BASE = 'http://127.0.0.1:4723'

desired_caps = {
    "platformName": "Android",
    "deviceName": "2GRYD24423001092",   # adb devices shows this name
    "automationName": "UiAutomator2", # Appium default for Android
    "appPackage":'com.android.settings', # Example: Android Settings app
    "appActivity":'com.android.settings.Settings',
    "language":'en',
    "locale":'US'
}

client_config = AppiumClientConfig(
    remote_server_addr=SERVER_URL_BASE,
    direct_connection=True,
    keep_alive=False,
    ignore_certificates=True,
)

driver = webdriver.Remote(
    options=UiAutomator2Options().load_capabilities(desired_caps),
    client_config=client_config
)

#time.sleep(1)

#driver.quit()