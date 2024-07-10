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
    driver.get("https://en.wikipedia.org/wiki/Test_automation")
    yield driver
    driver.quit()


def test_find_unique_words(setup):
    driver = setup
    try:
        title_element = driver.find_element(By.ID, "Test-driven_development")
        paragraph_element = title_element.find_element(By.XPATH, "./following::p[1]")
        text = paragraph_element.text
        words = re.findall(r'\b\w+\b', text.lower())
        unique_words = set(words)
        print("Unique words in the text:")
        for word in unique_words:
            print(word)
        output_path = "C:\\Automation\\unique_words.txt"
        with open(output_path, "w") as writer:
            for word in unique_words:
                writer.write(word + "\n")
    except NoSuchElementException:
        print("Element not found.")
    print(f"Test scenario test01_find_unique_words finished")


def test_find_brackets(setup):
    driver = setup
    try:
        title_element = driver.find_element(By.ID, "Test-driven_development")
        paragraph_element = title_element.find_element(By.XPATH, "./following::p[1]")
        text = paragraph_element.text
        result_without_brackets = re.sub(r'\[[^\]]*\]', '', text)
        output_path = "C:\\Automation\\withoutBrackets.txt"
        with open(output_path, "w") as writer:
            writer.write(result_without_brackets)
    except NoSuchElementException:
        print("Element not found.")
    print(f"Test scenario test02_find_brackets finished")


def test_find_delimiters(setup):
    driver = setup
    try:
        title_element = driver.find_element(By.ID, "Test-driven_development")
        paragraph_element = title_element.find_element(By.XPATH, "./following::p[1]")
        text = paragraph_element.text
        result_without_delimiters = re.sub(r'[\s\.,;-]+', ' ', text)
        output_path = "C:\\Automation\\withoutDelimiters.txt"
        with open(output_path, "w") as writer:
            writer.write(result_without_delimiters)
    except NoSuchElementException:
        print("Element not found.")
    print(f"Test scenario test03_find_delimiters finished")


def test_count_occurrences(setup):
    driver = setup
    try:
        title_element = driver.find_element(By.ID, "Test-driven_development")
        paragraph_element = title_element.find_element(By.XPATH, "./following::p[1]")
        text = paragraph_element.text
        words = text.split()
        word_counts = {}
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        print("Word Counts:")
        for word, count in word_counts.items():
            print(f"{word}: {count}")
    except NoSuchElementException:
        print("Element not found.")
        print(f"Test scenario test04_count_occurrences finished")
