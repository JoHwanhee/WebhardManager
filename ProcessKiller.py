import os
import platform


class ProcessKiller:
    def kill_chrome(self):
        print("프로새ㅔ스들 킬 합니다.")
        system = platform.system()
        if system == 'Windows':
            os.system("taskkill /f /im chromedriver.exe /t")
            os.system("taskkill /f /im chrome.exe /t")
        elif system == 'Linux':
            print('구현중..')