import pytest
from returns_content_file import read_bin_file_content, read_text_file_content
import os
from pathlib import Path


@pytest.fixture(scope="session")
def global_tmp_path():
    # Define the value of tmp_path here
    tmp_path = "C:\\Automation\\New_folder\\"
    return tmp_path


@pytest.fixture
def temp_txt_file(global_tmp_path):
    txt_content = "Hello, this is a text file."
    file_path = Path(global_tmp_path) / "test1.txt"
    with open(file_path, 'w') as file_content:
        file_content.write(txt_content)
        file_content.close()
    return file_path


@pytest.fixture
def temp_txt_empty_file(global_tmp_path):
    file_path = Path(global_tmp_path) / "test_empty.txt"
    return file_path


@pytest.fixture
def temp_bin_file(global_tmp_path):
    file_content = b"Hello, this is a binary file."
    file_path = Path(global_tmp_path) / "test1.bin"
    with open(file_path, 'wb') as file:
        file.write(file_content)
        file.close()
    return file_path


# Test cases


def test_read_text_file_content_exists(temp_txt_file):
    content = read_text_file_content(temp_txt_file)
    assert content == "Hello, this is a text file."


def test_read_text_file_no_content_exists(temp_txt_empty_file):
    content = read_text_file_content(temp_txt_empty_file)
    assert content is None


def test_read_text_file_content_nonexistent(global_tmp_path):
    non_existent_file = Path(global_tmp_path) / "non_existent_file.txt"
    content = read_text_file_content(non_existent_file)
    assert content is None


def test_read_text_file_content_io_error(global_tmp_path):
    # Attempt to read a directory as a file
    with pytest.raises(IOError):
        read_text_file_content(global_tmp_path)


def test_read_bin_file_content_exists(temp_bin_file):
    content = read_bin_file_content(temp_bin_file)
    assert content == b"Hello, this is a binary file."


def test_read_bin_file_content_nonexistent(global_tmp_path):
    non_existent_file = Path(global_tmp_path) / "non_existent_file.bin"
    content = read_bin_file_content(non_existent_file)
    assert content is None


def test_read_bin_file_content_io_error(global_tmp_path):
    # Attempt to read a directory as a file
    directory_path = global_tmp_path + "directory"
    # directory_path.mkdir()
    os.makedirs(directory_path)
    with pytest.raises(IOError):
        read_bin_file_content(directory_path)


# Finalizer to remove the directory after the test
@pytest.fixture(autouse=True)
def cleanup_tmp_dir(request, global_tmp_path):
    tmp_path = Path(global_tmp_path)
    yield
    # Remove the directory after the test
    for item in tmp_path.iterdir():
        if item.is_dir():
            os.rmdir(item)


@pytest.fixture(autouse=True)
def cleanup_tmp_files(request, global_tmp_path):
    tmp_path = Path(global_tmp_path)
    yield
    for item in tmp_path.iterdir():
        if item.is_file():
            os.remove(item)
