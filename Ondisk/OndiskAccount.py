from selenium import webdriver


class OndiskAccount:
    def __init__(self, loginId, idXPath, loginPassword, pwXPath, loginXPath):
        self.id = loginId
        self.idXPath = idXPath
        self.pw = loginPassword
        self.pwXPath = pwXPath
        self.loginXPath = loginXPath

    #=webdriver.Chrome()
    def login(self, driver):
        driver.find_element_by_xpath(self.idXPath).send_keys(self.id)
        driver.find_element_by_xpath(self.pwXPath).send_keys(self.pw)
        driver.find_element_by_xpath(self.loginXPath).click()
        driver.switch_to.alert.accept()
        print('로그인 성공!')