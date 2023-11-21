class Settings:

    mobile_stand = {
        'appium_server': 'http://127.0.0.1:4723',
        'Pixel_6': {
            'platformName': "Android",
            'platformVersion': "34",
            'deviceName': 'Pixel_6',
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
