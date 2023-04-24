"""
Configuration test
"""
import os
import pytest

from loguru import logger
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def browser():
    """
    Main fixture
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized") # open Browser in maximized mode
    chrome_options.add_argument("--disable-infobars") # disabling infobars
    chrome_options.add_argument("--disable-extensions") # disabling extensions
    chrome_options.add_argument("--disable-gpu") #  applicable to windows os only
    chrome_options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems
    # chrome_options.add_argument("--headless")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def cleare_report():
    """
    Clear all allure reports
    """
    path = f"{os.getcwd()}\\allure_results\\"
    # for file_name in os.listdir(path):
    #     file = path + file_name
    #     if os.path.isfile(file):
    #         logger.info(f'Deleting file: {file}')
    #         os.remove(file)
