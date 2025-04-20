import os
import pytest
from dotenv import load_dotenv
import platform
from pathlib import Path
from playwright.sync_api import sync_playwright
import allure
load_dotenv()


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


ALLURE_RESULTS_DIR = "allure-results"
env = os.getenv("TEST_ENV", "Local")  # можно подхватывать из .env
env_file = Path(ALLURE_RESULTS_DIR) / "environment.properties"


@pytest.hookimpl(tryfirst=True)
def pytest_configure():
    # Получим данные из Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        browser_version = context.browser.version
        browser.close()

    os.makedirs(ALLURE_RESULTS_DIR, exist_ok=True)

    with env_file.open("w") as f:
        f.write(f"Browser=Chromium\n")
        f.write(f"Browser.Version={browser_version}\n")
        f.write(f"OS={platform.system()} {platform.release()}\n")
        f.write(f"Environment={env}\n")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call" and result.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshot = page.screenshot()
            allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
