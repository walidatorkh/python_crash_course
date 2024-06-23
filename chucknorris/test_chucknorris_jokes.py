import pytest
import requests
from chucknorris_jokes import print_random_joke, get_random_joke_by_category


def test_print_random_joke_success(capsys):
    result = print_random_joke("random")
    captured = capsys.readouterr()

    assert "Random Chuck Norris Joke:" in captured.out
    assert result == "random"


def test_print_random_joke_failure():
    result = print_random_joke("invalid_endpoint")
    assert result == "invalid_endpoint"


def test_get_random_joke_by_category_success():
    result = get_random_joke_by_category("random")
    assert isinstance(result, list)


def test_get_joke_categories_failure(monkeypatch):
    def mock_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self):
                self.status_code = 404

            def json(self):
                return None

        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_requests_get)
    result = get_random_joke_by_category("invalid_category")
    assert result is None
