"""
First Module
"""
# импортируем модули и отдельные классы
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# каждый тест должен начинаться с test_
def test_1():
    """
    Test case WERT-1
    """
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		# определяем адрес страницы для теста и переходим на неё
    driver.get("https://testqastudio.me")  

    element = driver.find_element(by=By.CSS_SELECTOR, value='ul [class*= "post-11342"]')
    element.click()

    sku = driver.find_element(by=By.CLASS_NAME, value="sku")
    
    assert sku.text == 'MFQJUZ43E7', "unexpected SKU, wait for: MFQJUZ43E7"
    