# list = [
#     "The Document Object Model (DOM) hierarchy is a tree-like structure that represents the structure of an HTML or XML document. It provides a way for programs (typically web browsers) to interact with the structure, content, and style of a document."]


def find_unique(elements: any):
    count_dict = {}
    for element in elements:
        count_dict[element] = count_dict.get(element, 0) + 1

    unique_elements = [element for element, count in count_dict.items() if count == 1]

    return unique_elements


input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print(find_unique(input_list))  # Вывод: [1, 3, 5]
