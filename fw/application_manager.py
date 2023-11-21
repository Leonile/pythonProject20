from fw.androidinstance import AndroidEmulatorInstance
from fw.appiuminstance import AppiumInstance
from fw.sidebar import Sidebar
from fw.tab_schedule import TabSchedule
from fw.tab_settings import TabSettings


class ApplicationManager:

    def __init__(self):
        self.android_instance = AndroidEmulatorInstance()
        self.driver_instance = AppiumInstance()
        self.sidebar = Sidebar(self)
        self.tab_settings = TabSettings(self)
        self.tab_schedule = TabSchedule(self)


