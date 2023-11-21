from appium.webdriver.common.appiumby import AppiumBy


class MobileBase:

    def __init__(self, ApplicationManager):
        self.manager = ApplicationManager

    def GetDriver(self):
        if self.manager.driver_instance.appium_driver is None:
            self.manager.driver_instance.get_Appium_Driver_Instance()
        return self.manager.driver_instance.appium_driver

    def click_by_xpath(self, locator):
        return self.find_element(by=AppiumBy.XPATH, value=locator).click()

    def find_element(self, by, value):
        return self.GetDriver().find_element(by, value)

    def scroll_to_element(self, by, value, down=True, search_before_scroll=False, step=1):
        if down:
            direction = f"new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd({step}))"
        else:
            direction = f"new UiScrollable(new UiSelector().scrollable(true)).scrollToBeginning({step}))"
        for count in range(30):
            try:
                if search_before_scroll:
                    try:
                        # Ищем элемент перед тем как скролить
                        el = self.find_element(by, value, 2)
                        if el:
                            return el
                    except:
                        pass
                # Скролим вниз
                self.find_element(AppiumBy.ANDROID_UIAUTOMATOR, direction, 0)
                # Если скрол не дошёл до конца - ищем элемент на страницу
                el = self.find_element(by, value, 0)
                if el:
                    return el
            except:
                try:
                    # Ищем элемент на странице
                    el = self.find_element(by, value, 0)
                    if el:
                        return el
                except:
                    pass
        return self