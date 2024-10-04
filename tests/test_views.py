import pytest
from unittest.mock import patch, MagicMock
from src.views import get_greeting, fetch_currency_rates, fetch_stock_prices


# Тестируем функцию get_greeting
@pytest.mark.parametrize(
    "hour, expected_greeting",
    [
        (6, "Доброе утро"),
        (12, "Добрый день"),
        (15, "Добрый день"),
        (19, "Добрый вечер"),
        (23, "Доброй ночи"),
        (3, "Доброй ночи"),
    ],
)
def test_get_greeting(hour, expected_greeting):
    """Тестируем разные временные интервалы для get_greeting."""
    assert get_greeting(hour) == expected_greeting


# Тестируем fetch_currency_rates с использованием mock для requests
@patch("src.views.requests.get")
def test_fetch_currency_rates(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "rates": {
            "USD": 1.0,
            "EUR": 0.85,
        }
    }
    mock_get.return_value = mock_response

    user_currencies = ["USD", "EUR"]
    result = fetch_currency_rates(user_currencies)
    assert result == {"USD": 1.0, "EUR": 0.85}


@patch("src.views.requests.get")
def test_fetch_stock_prices(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "c": 150.0
    }
    mock_get.return_value = mock_response

    user_stocks = ["AAPL", "TSLA"]
    result = fetch_stock_prices(user_stocks)
    assert result == {"AAPL": 150.0, "TSLA": 150.0}
