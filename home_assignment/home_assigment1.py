import os
import re
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class TestHomeAssignment1(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://en.wikipedia.org/wiki/Test_automation")

    def test01_find_unique_words(self):
        try:
            title_element = self.driver.find_element(By.ID, "Test-driven_development")
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

    def test02_find_brackets(self):
        try:
            title_element = self.driver.find_element(By.ID, "Test-driven_development")
            paragraph_element = title_element.find_element(By.XPATH, "./following::p[1]")
            text = paragraph_element.text
            result_without_brackets = re.sub(r'\[[^\]]*\]', '', text)
            output_path = "C:\\Automation\\withoutBrackets.txt"
            with open(output_path, "w") as writer:
                writer.write(result_without_brackets)
        except NoSuchElementException:
            print("Element not found.")
        print(f"Test scenario test02_find_brackets finished")


    def test03_find_delimiters(self):
        try:
            title_element = self.driver.find_element(By.ID, "Test-driven_development")
            paragraph_element = title_element.find_element(By.XPATH, "./following::p[1]")
            text = paragraph_element.text
            result_without_delimiters = re.sub(r'[\s\.,;-]+', ' ', text)
            output_path = "C:\\Automation\\withoutDelimiters.txt"
            with open(output_path, "w") as writer:
                writer.write(result_without_delimiters)
        except NoSuchElementException:
            print("Element not found.")
        print(f"Test scenario test03_find_delimiters finished")


    def test04_count_occurrences(self):
        try:
            title_element = self.driver.find_element(By.ID, "Test-driven_development")
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


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
