def find_unique(elements: any):
    count_dict = {}
    for element in elements:
        count_dict[element] = count_dict.get(element, 0) + 1

    unique_elements = [element for element, count in count_dict.items() if count == 1]

    return unique_elements


input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print(find_unique(input_list))  # Вывод: [1, 3, 5]


# Test case 1: Empty list should return an empty list
def test_find_unique_empty_list():
    assert find_unique([]) == []


# Test case 2: List with all unique elements should return the same elements
def test_find_unique_all_unique():
    assert find_unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


# Test case 3: List with duplicates, should return only unique elements
def test_find_unique_with_duplicates():
    assert find_unique([1, 2, 2, 3, 3, 4, 5, 5]) == [1, 4]


# Test case 4: List with all elements being the same should return an empty list
def test_find_unique_all_same_elements():
    assert find_unique([1, 1, 1, 1, 1]) == []


# Test case 5: List with mixed types (str and int), should handle them correctly
# Due a function works with integers only
def test_find_unique_mixed_types():
    assert find_unique([1, 'hello', 2, 'hello', 3, 4, 4]) == [1, 2, 3]


# Test case 6: List with None and empty strings
def test_find_unique_with_none_and_empty_strings():
    assert find_unique([None, '', 'hello', None, '', 1, 2]) == ['hello', 1, 2]


# Test case 7: List with special characters
def test_find_unique_with_special_characters():
    assert find_unique(['!', '@', '#', '$', '%', '^']) == ['!', '@', '#', '$', '%', '^']
