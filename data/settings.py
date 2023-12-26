class Settings:

    mobile_stand = {
        'appium_server': 'http://127.0.0.1:4723',
        'Pixel_6': {
            'platformName': "Android",
            'platformVersion': "33",
            'deviceName': 'Xiaomi2101K9AG',
            'appPackage': "com.scheduleapp",
            'appActivity': "com.scheduleapp.MainActivity",
            'language': 'ru',
            'locale': 'RU'
        }
    }

    appium_settings = {
        'NewCommandTimeout': 120,
        'autoGrantPermissions': True
    }
