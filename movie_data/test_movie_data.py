import requests
import pytest
from movie_data import search_movies_total


# Test case: Valid search term with movies found
def test_search_movies_total_valid():
    # Arrange
    substr = "maze"
    # Act
    total = search_movies_total(substr)
    # Assert
    assert total is not None
    assert isinstance(total, int)
    assert total > 0


# Test case: Invalid search term with no movies found
def test_search_movies_total_invalid():
    # Arrange
    substr = "nonexistenttitle"
    # Act
    total = search_movies_total(substr)
    # Assert
    assert total == 0


# Test case: Network error (simulate using pytest-mock)
def test_search_movies_total_network_error(mocker):
    # Arrange
    substr = "maze"
    mocked_response = mocker.Mock()
    mocked_response.status_code = 500
    mocker.patch("requests.get", return_value=mocked_response)
    # Act
    total = search_movies_total(substr)
    # Assert
    assert total is None
