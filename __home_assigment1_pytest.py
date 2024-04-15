import pytest
import os
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.canadadealsonline.com/")
    yield driver
    driver.quit()


def test_find_unique_words(setup):
    driver = setup
    try:
        driver.implicitly_wait(8)
        search_input = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_input.send_keys("Keyboard")
        driver.implicitly_wait(5)
        print("Unique words in the text:")

    except NoSuchElementException:
        print("Element not found.")
    print(f"Test scenario test01_find_unique_words finished")

