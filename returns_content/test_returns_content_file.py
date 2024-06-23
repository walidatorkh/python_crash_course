import tempfile
from unittest import mock

import pytest
from returns_content_file import read_bin_file_content, read_text_file_content
import os


# Test case: Reading content from an existing text file
def test_read_valid_file():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b'Hello, World!')
        temp_path = f.name
    assert read_text_file_content(temp_path) == 'Hello, World!'
    os.remove(temp_path)


# Test case: Attempting to read content from a non-existing file
def test_read_non_existent_file():
    assert read_text_file_content('non_existent.txt') is None


# Test case: Attempting to read content from a file with no permissions
def test_read_no_permission_file():
    # This part is tricky because Windows does not support the concept of read permissions in the same way as Unix
    if os.name != 'nt':  # 'nt' indicates the Windows platform
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(b'Hello, World!')
            temp_path = f.name
        os.chmod(temp_path, 0o222)  # write-only permissions
        assert read_text_file_content(temp_path) is None
        os.chmod(temp_path, 0o777)  # reset permissions
        os.remove(temp_path)


# Test case: Attempting to read content from a directory instead of a file
def test_read_directory_instead_of_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        assert read_text_file_content(temp_dir) is None


# Test IOError exception
def test_read_file_raises_ioerror():
    with mock.patch('builtins.open', mock.mock_open()) as m:
        m.side_effect = IOError
        assert read_text_file_content('any_path') is None


# Test PermissionError exception
def test_read_file_raises_permission_error():
    with mock.patch('builtins.open', mock.mock_open()) as m:
        m.side_effect = PermissionError
        assert read_text_file_content('any_path') is None


# Test FileNotFoundError exception
def test_read_file_raises_file_not_found_error():
    with mock.patch('builtins.open', mock.mock_open()) as m:
        m.side_effect = FileNotFoundError
        assert read_text_file_content('any_path') is None


# Test case: Reading content from an existing bin file
def test_read_bin_file_content_existing_file(tmp_path):
    # Arrange: Create a temporary binary file with content
    content = b"Hello, World!"
    file_path = tmp_path / "test_file.bin"
    with open(file_path, 'wb') as file:
        file.write(content)

    # Act: Call the function to read the file content
    result = read_bin_file_content(file_path)

    # Assert: Check if the content matches
    assert result == content


# Test case: Reading content from a non-existing bin file
def test_read_bin_file_content_non_existing_file(tmp_path):
    # Arrange: Use a non-existing file path
    file_path = tmp_path / "non_existing_file.bin"

    # Act: Call the function to read the file content
    result = read_bin_file_content(file_path)

    # Assert: Check if the result is None
    assert result is None


# Test case: Reading content from a directory
def test_read_bin_file_content_directory(tmp_path):
    # Arrange: Create a temporary directory
    directory_path = tmp_path / "test_directory"
    os.makedirs(directory_path)

    # Act and Assert: Check if IsADirectoryError is raised
    with pytest.raises(IsADirectoryError):
        read_bin_file_content(directory_path)
