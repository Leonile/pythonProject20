from appium.webdriver.common.appiumby import AppiumBy

from fw.mobile_base import MobileBase

class Locator:
    select_group_or_teacher = '(//android.view.ViewGroup[@class="android.view.ViewGroup"])[6]'

class TabSchedule(MobileBase):

    def select_group_or_teacher(self, teacher_or_group_name):
        self.click_by_xpath(Locator.select_group_or_teacher)
        return self.click_by_xpath(f'//android.widget.TextView[@text="{teacher_or_group_name}" and @class="android.widget.TextView"]')


    def check_group_or_teacher_on_page(self, name_group_or_teacher):
        try:
            self.find_element(by=AppiumBy.XPATH, value=f'//android.widget.TextView[@text="{name_group_or_teacher}" and @class="android.widget.TextView"]')
            return True
        except:
            return False

