import pytest
from unittest.mock import mock_open, patch
from returns_content_file import read_text_file_content


# Test cases


def test_read_text_file_content_success():
    mock_file_content = "Some text!"
    with patch("builtins.open", mock_open(read_data=mock_file_content)) as mock_file:
        assert read_text_file_content("file_path") == mock_file_content
        mock_file.assert_called_once_with("file_path", 'r')


def test_read_text_file_content_is_directory():
    with patch("os.path.isdir", return_value=True):
        result = read_text_file_content("os.path.isdir")
        assert result is None


def test_read_text_file_content_file_not_found():
    with patch("builtins.open", mock_open()) as mock_file:
        mock_file.side_effect = FileNotFoundError
        assert read_text_file_content("file_path") is None
        mock_file.assert_called_once_with("file_path", 'r')


def test_read_text_file_content_io_error():
    with patch("builtins.open", mock_open()) as mock_file:
        mock_file.side_effect = IOError
        assert read_text_file_content("file_path") is None
        mock_file.assert_called_once_with("file_path", 'r')
