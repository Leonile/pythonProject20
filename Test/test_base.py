from fw.application_manager import ApplicationManager


class TestBase:

    APP = ApplicationManager()

    def setup_class(self):
        #self.APP.android_instance.start_emulator()
        pass

    def setup_method(self):
        self.APP.driver_instance.get_Appium_Driver_Instance()

    def teardown_method(self):
        self.APP.android_instance.clear_cache()
        self.APP.driver_instance.stop_Test()

    def teardown_class(self):
        self.APP.android_instance.stop_emulator()