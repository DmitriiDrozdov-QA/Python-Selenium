"""
Smoke test
"""
import pytest

from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test_product_view_sku():
    """
    Test case WERT-1
    """
    logger.info("Start test")
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
    url = "https://testqastudio.me/"
    driver.get(url=url)

    WebDriverWait(driver, timeout=10, poll_frequency=1).until(EC.text_to_be_present_in_element(
       (By.CLASS_NAME, "razzi-posts__found-inner"), 'Показано 12 из 16 товары'))
    # driver.implicitly_wait(10)
    element = driver.find_element(by=By.CSS_SELECTOR, value="[class='tab-best_sellers ']")
    element.click()

    WebDriverWait(driver, timeout=10, poll_frequency=1).until(EC.text_to_be_present_in_element(
       (By.CLASS_NAME, "razzi-posts__found-inner"), "Показано 12 из 16 товары"))

    element = driver.find_element(By.CSS_SELECTOR, value='[class*="post-11094"]')
    element.click()

    sku = driver.find_element(By.CLASS_NAME, value="sku")

    assert sku.text == 'C0MSSDSUMK', "Unexpected sku"

@pytest.mark.smoke
def test_smoke(browser):
    """
    Test case SMK-1
    """
    url = "https://testqastudio.me/"
    browser.get(url=url)