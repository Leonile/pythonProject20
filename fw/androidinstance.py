import os
import subprocess
from subprocess import call

from data.settings import Settings


class AndroidEmulatorInstance:

    def __init__(self):
        self.settings = Settings

    def start_emulator(self):
        print('Start emulator')
        subprocess.Popen(['emulator', '@Pixel_6'])
        os.system('adb wait-for-device')
        os.system('Perform whatever adb commands you need')

    def stop_emulator(self):
        print('Stop emulator')
        os.system('adb devices')
        call(['adb', '-s', 'emulator-5554', 'emu', 'kill'])

    def clear_cache(self):
        print('Clear cache')
        os.system(('adb shell pm clear com.scheduleapp'))