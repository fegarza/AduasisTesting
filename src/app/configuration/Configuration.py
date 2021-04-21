import json
from selenium import webdriver

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Configuration(metaclass=Singleton):
    def __init__(self):
        with open('../settings.json') as json_file:
            configFile = json.load(json_file)
            urls = configFile['direcciones']
            self.portal_url = urls["portal"]
            self.mobile_url = urls["mobile"]
        self.driver = webdriver.Chrome(executable_path='../chromedriver.exe')
