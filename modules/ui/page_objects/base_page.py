# import Selenium webdriver and Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# create a BasePage class, locate the chromedriver executable and start the service
class BasePage:
    PATH = r"c:/Users/Mine-iac/Desktop/AKQA-Auto2023"
    DRIVER_NAME = "chromedriver.exe"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
        )

    def close(self):
        self.driver.close()