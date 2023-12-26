import os
from pathlib import Path

from data.settings import Settings
from appium import webdriver
from appium.options.android import UiAutomator2Options


class AppiumInstance:

    def __init__(self):
        self.settings = Settings

    appium_driver = None

    def get_Appium_Driver_Instance(self):
        if self.appium_driver is None:

            option = UiAutomator2Options()
            option.platform_name = self.settings.mobile_stand['Pixel_6']['platformName']
            option.automation_name = 'uiautomator2'
            option.device_name = self.settings.mobile_stand['Pixel_6']['deviceName']
            option.app_package = self.settings.mobile_stand['Pixel_6']['appPackage']
            option.app = os.path.join(Path(__file__).parent, '../data', 'Ngieu.apk')
            option.app_activity = self.settings.mobile_stand['Pixel_6']['appActivity']
            if Settings.appium_settings['autoGrantPermissions']:
                option.auto_grant_permissions = True
            option.ignore_hidden_api_policy_error = True
            option.language = self.settings.mobile_stand['Pixel_6']['language']
            option.locale = self.settings.mobile_stand['Pixel_6']['locale']
            option.new_command_timeout = Settings.appium_settings['NewCommandTimeout']

            self.appium_driver = webdriver.Remote(self.settings.mobile_stand['appium_server'], options=option)
            self.appium_driver.implicitly_wait(3)
        return self.appium_driver

    def stop_Test(self):
        if self.appium_driver is not None:
            self.appium_driver.quit()
            self.appium_driver = None
