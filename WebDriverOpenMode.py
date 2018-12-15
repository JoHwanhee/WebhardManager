from enum import Enum


class WebDriverOpenMode (Enum):
    Non = 0
    Hide = 1
    Normal = 2
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance