from fw.mobile_base import MobileBase


class Locator:
    button_settings = '//android.widget.TextView[@text="󰢻" and @class="android.widget.TextView"]'
    button_schedule = '(//android.view.ViewGroup[@class="android.view.ViewGroup"])[22]'


class Sidebar(MobileBase):

    def click_on_settings(self):
        return self.click_by_xpath(Locator.button_settings)

    def click_on_schedule(self):
        return self.click_by_xpath(Locator.button_schedule)