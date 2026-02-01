import requests
from selene import browser, query
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_text_in_downloaded_file():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": "/Users/komashka/PycharmProjects/qa_guru_python_1_0/tmp",
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    browser.config.driver = driver


    browser.open('https://github.com/pytest-dev/pytest/blob/main/README.rst')
    # browser.element('[data-testid="download-raw-button"]').click()
    # time.sleep(5)
    download_url = browser.element('[data-testid="raw-button"]').get(query.attribute("href"))
    print(download_url)
    content = requests.get(url=download_url).content
    with open("tmp/readme.rst", "wb") as file:
        file.write(content)

    with open("tmp/readme.rst") as file:
        file_content_str = file.read()
        assert "test_answer " in file_content_str
