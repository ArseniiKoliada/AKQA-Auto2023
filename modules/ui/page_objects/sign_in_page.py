# Import BasePage to enable inheritance and import By to enable finding elements on a web page
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = "https://github.com/login"        # URL which will be opened

    def __init__(self) -> None:
        super().__init__()

    # Open the selected URL from URL class attribute    
    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # Find login field
        login_elem = self.driver.find_element(By.ID, "login_field")

        #Enter incorrect name or email
        login_elem.send_keys(username)

        # Find password field
        pass_elem = self.driver.find_element(By.ID, "password")

        # Enter wrong password
        pass_elem.send_keys(password)

        # Find sign in button
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Emulate left click
        btn_elem.click()

    # Check the title of the page
    def check_title(self, expected_title):
        return self.driver.title == expected_title