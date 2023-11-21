from appium.webdriver.common.appiumby import AppiumBy

from fw.mobile_base import MobileBase

class Locator:
    select_teacher = '(//android.view.ViewGroup[@class="android.view.ViewGroup"])[8]'

class TabSchedule(MobileBase):

    def select_teacher(self, teacher_name):
        self.click_by_xpath(Locator.select_teacher)
        return self.click_by_xpath(f'//android.widget.TextView[@text="{teacher_name} " and @class="android.widget.TextView"]')

    def check_lesson_on_page(self, name_lesson):
        try:
            self.find_element(by=AppiumBy.XPATH, value=f'(//android.widget.TextView[@text="{name_lesson}" and @class="android.widget.TextView"])')
            return True
        except:
            return False

