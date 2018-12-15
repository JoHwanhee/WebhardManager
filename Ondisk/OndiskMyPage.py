from selenium import webdriver


class OndiskMyPage:
    def __init__(self, url, checkboxTag , upButtonTag):
        self.myPageUrl = url
        self.checkboxTag = checkboxTag
        self.upButtonTag = upButtonTag

    #=webdriver.Chrome()
    def click_contents_up(self, driver):
        driver.get(self.myPageUrl)
        driver.find_element_by_xpath(self.checkboxTag).click()
        driver.find_element_by_xpath(self.upButtonTag).click()
        driver.implicitly_wait(10)
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
        driver.switch_to.alert.accept()
        print(driver.page_source)

    def can_find_contents(self, driver):
        return driver.find_element_by_xpath(self.checkboxTag).is_selected()