import os
import platform


class ProcessKiller:
    def kill_chrome(self):
        print("Kill the processes for chrome")
        system = platform.system()
        if system == 'Windows':
            os.system("taskkill /f /im chromedriver.exe /t")
            os.system("taskkill /f /im chrome.exe /t")
        elif system == 'Linux':
            os.system("killall chromedriver")
            os.system("killall chrome")
