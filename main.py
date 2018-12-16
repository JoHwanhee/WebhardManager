from _datetime import datetime
from AppSetting import AppSetting
from Ondisk.OndiskAccount import OndiskAccount
from Ondisk.OndiskMyItem import OndiskMyItem
from Ondisk.OndiskMyPage import OndiskMyPage
from WebDriverFactory import WebDriverFactory
from WebhardManager import WebhardManager
import threading

global is_run
is_run = 1

global repeat_tick
repeat_tick = 60 * 30


def main_logic():
    setting = AppSetting('AppSetting.ini')
    driverPath = setting.webDriverPath

    nowHour = datetime.now().hour;
    print(nowHour)
    if 2 <= nowHour <= 24:
        try:
            url = setting.ondiskUrl
            print(url)
            driver = WebDriverFactory(driverPath).createChromeDriver()
            account = OndiskAccount(setting.ondiskId, setting.ondiskIdXpath, setting.ondiskPw, setting.ondiskPwXpath,
                                    setting.ondiskLoginXpath)
            myPage = OndiskMyPage(setting.ondiskMyPageUrl, setting.ondiskMyPageCheckBoxXpath,
                                  setting.ondiskUpButtonXpath)
            myItem = OndiskMyItem()

            webhardManager = WebhardManager(url, driver, account, myPage, myItem, None)
            webhardManager.run()
        except Exception as e:
            print(e)
        finally:
            pass

    timer = threading.Timer(repeat_tick, main_logic)
    if is_run == 1:
        timer.start()
    else:
        timer.cancel()


main_logic()
a = input("Press any key to exit")
is_run = 0

print("exited")
