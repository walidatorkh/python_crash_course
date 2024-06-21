from unittest import mock

import pytest
from unittest.mock import mock_open, patch
from returns_content_file import read_text_file_content, read_bin_file_content


# Test cases


# def test_read_text_file_content_success():
#     mock_file_content = "Some text!"
#     with patch("builtins.open", mock_open(read_data=mock_file_content)) as mock_file:
#         assert read_text_file_content("file_path") == mock_file_content
#         mock_file.assert_called_once_with("file_path", 'r')
#
#
# def test_read_text_file_content_is_directory():
#     with patch("os.path.isdir", return_value=True):
#         result = read_text_file_content("os.path.isdir")
#         assert result is None
#
#
# def test_read_text_file_content_file_not_found():
#     with patch("builtins.open", mock_open()) as mock_file:
#         mock_file.side_effect = FileNotFoundError
#         assert read_text_file_content("file_path") is None
#         mock_file.assert_called_once_with("file_path", 'r')
#
#
# def test_read_text_file_content_io_error():
#     with patch("builtins.open", mock_open()) as mock_file:
#         mock_file.side_effect = IOError
#         assert read_text_file_content("file_path") is None
#         mock_file.assert_called_once_with("file_path", 'r')
@pytest.mark.parametrize("file_path, is_dir, is_link, readlink_target, open_data, open_side_effect, expected", [
    ('regular_file.txt', False, False, None, 'file content', None, 'file content'),
    ('directory', True, False, None, None, None, None),
    ('symlink', False, True, 'actual_file.txt', 'symlink content', None, 'symlink content'),
    ('protected_file.txt', False, False, None, None, PermissionError, None),
    ('nonexistent_file.txt', False, False, None, None, FileNotFoundError, None),
    ('error_file.txt', False, False, None, None, IOError('IO Error'), None),
    ('symlink_error', False, True, None, None, OSError('OS Error'), None),
])
def test_read_text_file_content(file_path, is_dir, is_link, readlink_target, open_data, open_side_effect, expected):
    with mock.patch('os.path.isdir', return_value=is_dir), \
            mock.patch('os.path.islink', return_value=is_link), \
            mock.patch('os.readlink', return_value=readlink_target), \
            mock.patch('builtins.open', mock.mock_open(read_data=open_data)) as mock_open:

        if open_side_effect:
            mock_open.side_effect = open_side_effect

        content = read_text_file_content(file_path)

    assert content == expected

    if not is_dir and not open_side_effect:
        if is_link and readlink_target:
            mock_open.assert_called_once_with(readlink_target, 'r')
        else:
            mock_open.assert_called_once_with(file_path, 'r')


# Test valid binary file read
def test_read_bin_file_content_valid():
    file_path = 'test.bin'
    test_content = b'This is a test binary file.'

    with patch('builtins.open', mock_open(read_data=test_content)) as mock_file:
        content = read_bin_file_content(file_path)
        mock_file.assert_called_once_with(file_path, 'rb')
        assert content == test_content


# Test reading a non-existent file
def test_read_bin_file_content_non_existent():
    file_path = 'non_existent.bin'

    with patch('builtins.open', side_effect=FileNotFoundError):
        content = read_bin_file_content(file_path)
        assert content is None


# Test reading a directory (should raise an exception)
def test_read_bin_file_content_is_directory():
    dir_path = '.'

    with pytest.raises(IsADirectoryError):
        read_bin_file_content(dir_path)


# Test reading a file with no permissions
def test_read_bin_file_content_no_permissions():
    file_path = 'no_perm.bin'

    with patch('builtins.open', side_effect=PermissionError):
        content = read_bin_file_content(file_path)
        assert content is None


# Test reading a symbolic link
def test_read_bin_file_content_symlink():
    file_path = 'test.bin'
    symlink_path = 'test_symlink.bin'
    test_content = b'This is a test binary file.'

    with patch('os.path.islink', return_value=True), \
            patch('os.readlink', return_value=file_path), \
            patch('builtins.open', mock_open(read_data=test_content)) as mock_file:
        content = read_bin_file_content(symlink_path)
        mock_file.assert_called_once_with(file_path, 'rb')
        assert content == test_content
