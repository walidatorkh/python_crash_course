import os
import re
import pytest
import requests
from collections import defaultdict


class TestHomeAssignment2:
    url = "https://www.mediawiki.org/w/api.php"

    @pytest.fixture(scope="class")
    def session(self):
        return requests.Session()

    def test_find_on_page_unique_words(self, session):
        try:
            # Prepare request to query the API
            params = {
                "action": "query",
                "list": "search",
                "srsearch": "Test automation",
                "format": "json"
            }
            response = session.get(self.url, params=params)

            # Check if the request was successful
            if response.ok:
                # Parse JSON response
                json_response = response.json()

                # Extract search results from the response
                search_results = json_response["query"]["search"]

                # Concatenate text content from search results
                text_content = " ".join([r["snippet"] for r in search_results])

                # Tokenize the text content into words
                words = re.findall(r'\b\w+\b', text_content.lower())

                # Use set to store unique words (case-insensitive)
                unique_words = set(words)

                # Print unique words to the console
                print("Unique words in the text (case-insensitive):")
                for unique_word in unique_words:
                    print(unique_word)

                # Define output file path
                output_path = "C:\\Automation\\FindOnPageUniqueWords.txt"

                # Write unique words to a text file
                with open(output_path, "w") as writer:
                    for word in unique_words:
                        writer.write(word + "\n")
            else:
                # Print error message if request was not successful
                print("Error occurred:", response.text)

        except requests.RequestException as ex:
            # Print exception message if an error occurs
            print(ex)
        print(f"Test scenario test_find_on_page_unique_words finished")

    def test_find_page_and_exclude_delimiters(self, session):
        try:
            # Prepare request to query the API
            params = {
                "action": "query",
                "list": "search",
                "srsearch": "Test automation",
                "format": "json"
            }
            response = session.get(self.url, params=params)

            # Check if the request was successful
            if response.ok:
                # Parse JSON response
                json_response = response.json()

                # Extract text content from search results and concatenate
                text_content = " ".join([s["snippet"] for s in json_response["query"]["search"]])

                # Define delimiters to exclude
                delimiters = ' ,.:;()-[]{}<>"\'\n\r\t'

                # Tokenize the text content into words while excluding delimiters
                words = re.split('[' + re.escape(delimiters) + ']+', text_content)

                # Use defaultdict to store word counts
                word_counts = defaultdict(int)
                for word in words:
                    word_counts[word] += 1

                # Print unique words to the console
                print("Unique words in the text (case-insensitive, excluding delimiters):")
                for word, count in word_counts.items():
                    print(f"{word}: {count}")

                # Define output file path
                output_path = "C:\\Automation\\FindPageAndExcludeDelimiters.txt"

                # Write unique words to a text file
                with open(output_path, "w") as writer:
                    for word, count in word_counts.items():
                        writer.write(f"{word}: {count}\n")
            else:
                # Print error message if request was not successful
                print("Error occurred:", response.text)

        except requests.RequestException as ex:
            # Print exception message if an error occurs
            print(ex)
        print(f"Test scenario test_find_page_and_exclude_delimiters finished")

    def test_print_occurrences(self, session):
        try:
            # Prepare request to query the API
            params = {
                "action": "query",
                "list": "search",
                "srsearch": "Test automation",
                "format": "json"
            }
            response = session.get(self.url, params=params)

            # Check if the request was successful
            if response.ok:
                # Parse JSON response
                json_response = response.json()

                # Extract text content from search results and concatenate
                text_content = " ".join([s["snippet"] for s in json_response["query"]["search"]])

                # Define delimiters to exclude
                delimiters = ' ,.:;()-[]{}<>"\'\n\r\t'

                # Tokenize the text content into words while excluding delimiters
                words = re.split('[' + re.escape(delimiters) + ']+', text_content)

                # Use defaultdict to store word counts
                word_counts = defaultdict(int)
                for word in words:
                    word_counts[word] += 1

                # Print the number of occurrences for each word
                print("Number of occurrences for each word:")
                for word, count in word_counts.items():
                    print(f"{word}: {count}")

            else:
                # Print error message if request was not successful
                print("Error occurred:", response.text)

        except requests.RequestException as ex:
            # Print exception message if an error occurs
            print(ex)
        print(f"Test scenario test_print_occurrences finished")
