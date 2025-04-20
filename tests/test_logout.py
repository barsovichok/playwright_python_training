import allure

from pages.login_page import LoginPage
from utils.env import BASE_URL


@allure.suite("Регресс")
@allure.feature("Logout")
@allure.story("Успешный выход")
@allure.title("Успешный выход обычным юзером")
def test_login_and_logout(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_inventory_visible()
    login_page.logout()
    assert page.url == "https://www.saucedemo.com/"
