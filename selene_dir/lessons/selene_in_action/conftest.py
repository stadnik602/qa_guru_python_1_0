import os
from typing import Literal

import pytest
from selene import browser as selene_browser, Browser, Config
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    driver_options = webdriver.FirefoxOptions()
    selene_browser.config.browser_name = os.getenv("selene.browser_name", "chrome")
    selene_browser.config.driver_options = driver_options
    selene_browser.config.timeout = float(os.getenv("selene.timeout", "3"))
    selene_browser.config.window_width = os.getenv("selene.window_width", "1024")
    selene_browser.config.window_height = os.getenv("selene.window_height", "768")
    selene_browser.config.base_url = os.getenv(
        "selene.base_url", "https://todomvc.com/examples/emberjs/todomvc/dist"
    )  # terminal command base_url='https://todomvc4tasj.herokuapp.com/' pytest selene_dir/lessons
    selene_browser.config.hold_browser_open = (
        os.getenv("hold_browser_open", "false").lower() == "true"
    )
    # driver_options.add_argument('--headless')
    # driver_options.add_argument('--window-size=1200x600')
    # selene_browser.config.type_by_js = True
    # selene_browser.config.click_by_js = True

    yield

    selene_browser.quit()


@pytest.fixture()
def driver():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=Service(executable_path=ChromeDriverManager().install()),
        options=driver_options,
    )
    yield driver

    driver.quit()


@pytest.fixture()
def browser(driver):

    yield Browser(Config(driver=driver))

SupportedBrowsers = Literal['chrome', 'firefox', 'edge']

@pytest.fixture(scope="function")
def with_new_browser():

    browsers = []

    def new_browser(name='chrome'):
        if name == 'chrome':
            browser = (Browser(
                Config(
                    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install())), base_url="https://todomvc.com/examples/emberjs/todomvc/dist")))
            browsers.append(browser)
        elif name == 'edge':
            browser = (Browser(
                Config(
                    driver=webdriver.Edge(), base_url="https://todomvc.com/examples/emberjs/todomvc/dist")))
        elif name == 'firefox':
            browser = (Browser(
                Config(driver = webdriver.Firefox(service=Service(GeckoDriverManager().install())), base_url="https://todomvc.com/examples/emberjs/todomvc/dist")))
        else:
            raise Exception(f"Browser: {name} is not supported! Please use 'chrome', 'firefox' or 'edge' values")
        return browser

    yield new_browser

    for browser_entity in browsers:
        browser_entity.quit()
