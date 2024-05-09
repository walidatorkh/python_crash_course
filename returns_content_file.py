import os

# function without context manager
# def read_text_file_content(file_path: str) -> str | None:
#     if os.path.isdir(file_path):
#         print(f"{file_path} is a directory, not a file")
#         return None
#     if not os.path.isfile(file_path):
#         print(f"File '{file_path}' not found.")
#         return None
#     try:
#         with open(file_path, 'r') as file:
#             content = file.read()
#         return content
#     except IOError as e:
#         print(f"Error reading file '{file_path}': {e}")
#         return None

import os


def read_text_file_content(file_path: str) -> str | None:
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except PermissionError:
        print(f"File '{file_path}' is not readable.")
        return None
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        return None


# function with context manager
def read_bin_file_content(file_path: str) -> bytes | None:
    if os.path.isdir(file_path):
        raise IsADirectoryError(f"{file_path} is a directory, not a file")
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            file.close()
        return content

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        return None


# rfc = read_text_file_content("C:\\Automation\\New_folder2\\testEmpty.txt")
# rfc = read_text_file_content("C:\\Automation\\New_folder\\non_existent_file.txt")
# rfc = read_text_file_content("C:\\Automation\\New_folder2\\file.txt")
# rfc = read_text_file_content("C:\\Automation\\new_folder2\\binbinych.bin")
# print(f"content is: {rfc}")
#
# rbfc = read_bin_file_content("C:\\Automation\\new_folder2\\binbinych.bin")
# print(f"content is: {rbfc}")
