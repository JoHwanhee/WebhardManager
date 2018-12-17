import threading
from _datetime import datetime

from AppSetting import AppSetting
from Ondisk.OndiskAccount import OndiskAccount
from Ondisk.OndiskMyItem import OndiskMyItem
from Ondisk.OndiskMyPage import OndiskMyPage
from WebDriverFactory import WebDriverFactory
from WebhardManager import WebhardManager


def main_logic():
    setting = AppSetting('AppSetting.ini')
    driverPath = setting.webDriverPath

    nowHour = datetime.now().hour
    if 18 >= nowHour or nowHour <= 9:
        try:
            url = setting.ondiskUrl
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

    timer = threading.Timer(120, main_logic)
    timer.start()


main_logic()
