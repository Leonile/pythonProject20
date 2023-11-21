from appium.webdriver.common.appiumby import AppiumBy

from fw.mobile_base import MobileBase

class Locator:
    button_change_view = '//android.view.ViewGroup[@content-desc="Студент"]'
    button_change_cathedra = '(//android.view.ViewGroup[@class="android.view.ViewGroup"])[16]'

class TabSettings(MobileBase):

    def click_button_change_view(self):
        return self.click_by_xpath(Locator.button_change_view)

    def select_cathedra(self, name_cathedra):
        self.click_by_xpath(Locator.button_change_cathedra)
        return self.click_by_xpath(f'//android.widget.TextView[@text="{name_cathedra}" and @class="android.widget.TextView"]')