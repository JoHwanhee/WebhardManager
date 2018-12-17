from _datetime import datetime
from AppSetting import AppSetting
from Ondisk.OndiskAccount import OndiskAccount
from Ondisk.OndiskMyItem import OndiskMyItem
from Ondisk.OndiskMyPage import OndiskMyPage
from WebDriverFactory import WebDriverFactory
from WebhardManager import WebhardManager
from time import sleep


def main_logic():
    setting = AppSetting('AppSetting.ini')
    driverPath = setting.webDriverPath

    nowHour = datetime.now().hour
    print(nowHour)
    if 18 <= nowHour <= 24:
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


while 1:
    main_logic()
    sleep(10)


print("exited")
