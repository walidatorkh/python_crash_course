import os


def find_and_read_bin_files(root_dir):
    bin_files_data = {}
    found_files_count = 0
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.bin'):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'rb') as file:
                    bin_files_data[file_path] = file.read()
                found_files_count += 1
    print(f"Found {found_files_count} binary files.")
    print(f"Found {bin_files_data} binary files.")
    return bin_files_data


# Example usage:
# root_directory = 'C:\\Automation\\New_folder\\'
# bin_files_data = find_and_read_bin_files(root_directory)
# for file_path, data in bin_files_data.items():
#     print("File:", file_path)
#     print("Data:", data)

# Pytest test cases
def test_find_and_read_bin_files(tmp_path):
    # Create a directory structure with binary files
    bin_file_contents = [b"Binary data 1", b"Binary data 2"]
    file_names = ["test1.bin", "test2.bin"]
    dir_names = ["dir1", "dir2"]

    for dir_name in dir_names:
        os.mkdir(os.path.join(tmp_path, dir_name))
        for file_name, content in zip(file_names, bin_file_contents):
            with open(os.path.join(tmp_path, dir_name, file_name), 'wb') as file:
                file.write(content)

    # Call the function to find and read binary files
    result = find_and_read_bin_files(tmp_path)

    # Assert: Check if the function returns the correct data
    assert isinstance(result, dict)
    assert len(result) == len(dir_names) * len(file_names)
    for dir_name in dir_names:
        for file_name, content in zip(file_names, bin_file_contents):
            file_path = os.path.join(tmp_path, dir_name, file_name)
            assert file_path in result
            assert result[file_path] == content


def test_find_and_read_bin_files_no_bin_files(tmp_path):
    # Create a directory structure without binary files
    os.makedirs(os.path.join(tmp_path, "empty_dir"))

    # Call the function to find and read binary files
    result = find_and_read_bin_files(tmp_path)

    # Assert: Check if the function returns an empty dictionary
    assert isinstance(result, dict)
    assert len(result) == 0