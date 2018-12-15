from configparser import ConfigParser


class AppSetting:
    def __init__(self, fileName):
        self.__instance = None
        self.__loadSetting(fileName)

    def __loadSetting(self, fileName):
        config = ConfigParser()
        config.read(fileName, encoding='UTF8')
        self.webDriverPath = config['DEFAULT']['WebDriverPath']
        self.ondiskUrl = config['ONDISK']['URL']
        self.ondiskId = config['ONDISK']['ID']
        self.ondiskPw = config['ONDISK']['PW']
        self.ondiskIdXpath = config['ONDISK_XPATH_ACCOUNT']['ID']
        self.ondiskPwXpath = config['ONDISK_XPATH_ACCOUNT']['PW']
        self.ondiskLoginXpath = config['ONDISK_XPATH_ACCOUNT']['LOGIN']

        self.ondiskMyPageUrl = config['ONDISK_XPATH_MYPAGE']['URL']
        self.ondiskMyPageCheckBoxXpath = config['ONDISK_XPATH_MYPAGE']['CheckBox']
        self.ondiskUpButtonXpath = config['ONDISK_XPATH_MYPAGE']['UpButton']

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance