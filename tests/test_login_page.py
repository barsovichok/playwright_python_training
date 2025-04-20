import allure
import pytest
from pages.login_page import LoginPage


@allure.suite("Регресс")
@allure.feature("Login")
@allure.story("Успешный вход")
@allure.title("Успешный вход обычным юзером")
def test_login_success(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_inventory_visible()


@allure.suite("Регресс")
@allure.feature("Login")
@allure.story("Юзеры с ошибками")
@allure.title("Юзер с ошибкой: {expected_error}")
@pytest.mark.parametrize("username,password,expected_error", [
    ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out."),
    ("standard_user", "wrong_password", "Username and password do not match"),
    ("", "", "Username is required")
])
def test_login_failures(page, username, password, expected_error):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)
    error = login_page.get_error_message()
    assert expected_error.lower() in error.lower()
