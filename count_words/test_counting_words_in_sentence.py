import pytest

from counting_words_in_sentence import count_words


@pytest.mark.parametrize("sentence, expected_count", [
    # Test case: Sentence with expected word count
    (
    "If it is running on GitHub Actions, we retrieve the temporary directory path from the RUNNER_TEMP environment variable, which provides a temporary directory specific to the GitHub Actions runner.",
    29),
    # Test case: Single word sentence
    ("Actions", 1),
    # Test case: Empty sentence
    (" ", 0),
    # Test case: Sentence with extra spaces
    ("   This  has  extra   spaces   ", 4),
    # Test case: Sentence with special characters
    ("! @ $ %, //////", 5),
    # Test case: Sentence with numbers
    ("3 4 5 6 ", 4),
    # Test case: Sentence with numbers and words
    ("There are 123 numbers.", 4),
])
def test_count_words_base_functional(sentence, expected_count):
    assert count_words(sentence) == expected_count
