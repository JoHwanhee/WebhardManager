from selenium import webdriver


class WebDriverFactory:
    def __init__(self, driverPath):
        self._driverPath = driverPath

    def createChromeDriver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(executable_path=self._driverPath, chrome_options=chrome_options)
        driver.implicitly_wait(3)

        return driver
