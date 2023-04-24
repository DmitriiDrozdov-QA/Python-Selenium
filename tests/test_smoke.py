# импортируем модули и отдельные классы
import pytest

from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager





# каждый тест должен начинаться с test_
def test_product_view_sku():
    """
    Test case WERT-1
    """
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    chrome_options.add_argument("--disable-gpu") #  applicable to windows os only
    chrome_options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		# определяем адрес страницы для теста и переходим на неё
    url = "https://testqastudio.me/"
    driver.get(url=url)
		# ждем и ищем по селектору элемент меню "Бестселлеры" и кликаем по нему
    WebDriverWait(driver, timeout=10, poll_frequency=1).until(EC.text_to_be_present_in_element(
       (By.CLASS_NAME, "razzi-posts__found-inner"), 'Показано 12 из 16 товары'))
    # driver.implicitly_wait(10)
    element = driver.find_element(by=By.CSS_SELECTOR, value="[class='tab-best_sellers ']")
    element.click()
		# ждем и ищем по CSS селектору "Журнальный столик" и кликаем по нему, чтобы просмотреть детали
    WebDriverWait(driver, timeout=10, poll_frequency=1).until(EC.text_to_be_present_in_element(
       (By.CLASS_NAME, "razzi-posts__found-inner"), "Показано 12 из 16 товары"))

    element = driver.find_element(By.CSS_SELECTOR, value='[class*="post-11094"]')
    element.click()
		# ищем по имени класса артикул для "Журнального столика"
    sku = driver.find_element(By.CLASS_NAME, value="sku")
		# проверяем соответствие
    assert sku.text == 'C0MSSDSUMK', "Unexpected sku"

