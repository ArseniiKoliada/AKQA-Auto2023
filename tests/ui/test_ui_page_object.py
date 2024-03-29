# Import SignInPage class and Pytest
from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # create page object
    sign_in_page = SignInPage()

    # Open Github login page
    sign_in_page.go_to()

    # Try to log in using try_login method from SignInPage class with parameters {email, pasword}
    sign_in_page.try_login("wrongemail@email.com", "some password")

    # Check if page name is correct
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Close browser
    sign_in_page.close()