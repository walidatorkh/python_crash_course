sentence = "If it is running on GitHub Actions, we retrieve the temporary directory path from the RUNNER_TEMP environment variable, which provides a temporary directory specific to the GitHub Actions runner."


def count_words(sentence: str) -> int:
    words = sentence.split()
    return len(words)


words_quantity = count_words(sentence)
print(words_quantity)
print(type(words_quantity))
