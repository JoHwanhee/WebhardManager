from selenium import webdriver
import re


class OndiskMyItem:
    # =webdriver.Chrome()
    def check_money_remaining(self, driver):
        text = driver.find_element_by_xpath("//span[@class='recommendgg']").text
        m = re.match('[0-9]+', text)
        return int(m.string)

    def how_many_can_buy_item(self, myMoney):
        if myMoney < 40:
            return 0

        price = 40;
        amount = int(myMoney / price);

        if 0 < amount <= 10:
            pass
        elif 11 <= amount <= 19:
            amount = 10
        elif 21 <= amount <= 49:
            amount = 20
        elif 51 <= amount <= 99:
            amount = 50
        elif 100 <= amount:
            amount = 100
        else:
            amount = 0

        return amount

    def buy(self, amount, driver):
        items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 50, 100]

        index = 0
        for i in items:
            if i == amount:
                break

            index += 1

        if i == items.count():
            index = 0

        if index > 0:
            itemType = 'cnt_4'
            driver.find_element_by_xpath("//select[@name='" + itemType + "']/option[@value='" + index + "']").click()
            driver.find_element_by_xpath(
                "//input[@src='https://image.ondisk.co.kr/main/popup/image/item_cash/itembuying_28.gif']").click()
            driver.switch_to.alert.accept()
            driver.switch_to.alert.accept()

    def buy_item(self, driver):
        print("여기까지?")
        driver.get("https://ondisk.co.kr/pop.php?mode=popup&sm=item_cash")

        myMoney = self.check_money_remaining(driver)
        amount = self.how_many_can_buy_item(myMoney)

        self.buy(amount, driver)
