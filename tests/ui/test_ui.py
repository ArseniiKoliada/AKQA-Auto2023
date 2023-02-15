import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # Create object for controlling browser
    driver = webdriver.Chrome(
        service=Service('c:/Users/Mine-iac/Desktop/AKQA-Auto2023' + r'/chromedriver.exe')
        )

    # Open https://github.com/login
    driver.get('https://github.com/login')


    # Find login field
    login_elem = driver.find_element(By.ID, 'login_field')

    # Enter wrong email
    login_elem.send_keys("arsenii.koliada@wrongemail.com")

    # Find password field
    pass_elem = driver.find_element(By.ID, 'password')

    # Enter wrong password
    pass_elem.send_keys("wrong password")

    # Find sign in button
    btn_elem = driver.find_element(By.NAME, "commit")

    # Check if page name is correct
    assert driver.title == "Sign in to GitHub · GitHub"
    # Emulate left click
    btn_elem.click()

    # Close browser
    driver.close()