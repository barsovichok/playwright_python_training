import allure

from pages.base_page import BasePage
from utils.env import BASE_URL, INVENTORY_URL


class LoginPage(BasePage):
    def open(self):
        with allure.step("Открываем страницу входа"):
            self.page.goto(BASE_URL)

    def login(self, username, password):
        with allure.step(f"Вводим логин: {username} и пароль: {password}"):
            self.page.fill("#user-name", username)
            self.page.fill("#password", password)
            self.page.click("#login-button")

    def is_inventory_visible(self):
        with allure.step("Видим главную страницу магазина"):
            return self.page.url == INVENTORY_URL

    def get_error_message(self):
        with allure.step("Проверяем сообщение об ошибке входа"):
            return self.page.locator("h3[data-test='error']").inner_text()

    def logout(self):
        with allure.step("Проверяем успешный logout"):
            self.page.click("#react-burger-menu-btn")
            self.page.click("#logout_sidebar_link")
