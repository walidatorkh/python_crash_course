
import os


def read_text_file_content(file_path: str) -> str | None:
    try:
        if os.path.isdir(file_path):
            print(f"'{file_path}' is a directory, not a file.")
            return None
        if os.path.islink(file_path):
            print(f"'{file_path}' is a symbolic link.")
            # Resolve the symlink to the actual file
            actual_path = os.readlink(file_path)
            with open(actual_path, 'r') as file:
                content = file.read()
            return content
        else:
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
    except OSError as e:
        print(f"Error handling symlink '{file_path}': {e}")
        return None


# function with context manager
def read_bin_file_content(file_path: str) -> bytes | None:
    if os.path.isdir(file_path):
        raise IsADirectoryError(f"{file_path} is a directory, not a file")
    try:
        if os.path.islink(file_path):
            print(f"'{file_path}' is a symbolic link.")
            # Resolve the symlink to the actual file
            actual_path = os.readlink(file_path)
            with open(actual_path, 'rb') as file:
                content = file.read()
        else:
            with open(file_path, 'rb') as file:
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
    except OSError as e:
        print(f"Error handling symlink '{file_path}': {e}")
        return None


# rfc1 = read_text_file_content("C:\\Automation\\New_folder2\\testEmpty.txt")
# rfc2 = read_text_file_content("C:\\Automation\\New_folder\\non_existent_file.txt")
# rfc3 = read_text_file_content("C:\\Automation\\New_folder2\\file.txt")
# rfc = read_text_file_content("C:\\Automation\\new_folder2\\binbinych.bin")
# print(f"content is: {rfc1}")
# print(f"content is: {rfc2}")
# print(f"content is: {rfc3}")
#
# rbfc = read_bin_file_content("C:\\Automation\\new_folder2\\binbinych.bin")
# print(f"content is: {rbfc}")
