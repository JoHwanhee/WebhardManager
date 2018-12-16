from ProcessKiller import ProcessKiller


class WebhardManager:
    def __init__(self, webharUrl, driver, userAccount, userMyPage, userMyItem, userMyCash):
        self._webHardUrl = webharUrl
        self.driver = driver
        self.userAccount = userAccount
        self.userMyPage = userMyPage
        self.userMyItem = userMyItem
        self.userMyCash = userMyCash

    def login(self):
        self.userAccount.login(self.driver)

    def click_contents_up_button(self):
        self.userMyPage.click_contents_up(self.driver)

    def buy_item(self):
        self.userMyItem.buy_item(self.driver)

    def requestWithdraw(self):
        print()

    def openWebSite(self):
        try:
            self.driver.get(self._webHardUrl)
        except ConnectionError:
            print("Cannot open website [" + self._webHardUrl + "]")

    def close(self):
        self.driver.close()

    def run(self):
        try:
            self.openWebSite()
            self.login()
            self.buy_item()
            self.click_contents_up_button()
            self.close()

        finally:
            self.driver.close()
            ProcessKiller().kill_chrome()
            print()