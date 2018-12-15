from AppSetting import AppSetting
from WebDriverFactory import WebDriverFactory
from WebhardManager import WebhardManager
from Ondisk.OndiskAccount import OndiskAccount
from Ondisk.OndiskMyPage import OndiskMyPage
from Ondisk.OndiskMyItem import OndiskMyItem

# load setting
setting = AppSetting('AppSetting.ini')
driverPath = setting.webDriverPath

# load chrome driver
url = setting.ondiskUrl
print(url)
driver = WebDriverFactory(driverPath).createChromeDriver()
account = OndiskAccount(setting.ondiskId, setting.ondiskIdXpath, setting.ondiskPw, setting.ondiskPwXpath, setting.ondiskLoginXpath)
myPage = OndiskMyPage(setting.ondiskMyPageUrl, setting.ondiskMyPageCheckBoxXpath, setting.ondiskUpButtonXpath)
myItem = OndiskMyItem()

webhardManager = WebhardManager(url, driver, account, myPage, myItem, None)
webhardManager.run()


