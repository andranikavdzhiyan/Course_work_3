import datetime
import json
import os

import requests
from dotenv import load_dotenv

from src.utils import get_transaction_data

load_dotenv()
api_key = os.getenv("API_FINNHUB_API_KEY")
api_key_1 = os.getenv("API_EXC_API_KEY")


def get_greeting(hour: int) -> str:
    """Возвращает приветствие в зависимоти от текущего времени суток."""
    if 5 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def fetch_currency_rates(user_currencies: list[str]) -> dict[str, float]:
    """Получает курс валют из API"""
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    params = {"access_key": api_key_1}
    response = requests.get(api_url, params=params)
    response.raise_for_status()

    data = response.json()

    if not isinstance(data, dict):
        raise ValueError("Ответ от API не является словарем")

    return {
        currency: data.get("rates", {}).get(currency, 0.0)
        for currency in user_currencies
    }


def fetch_stock_prices(user_stocks: list[str]) -> dict[str, float]:
    """Получает цены акций из API"""
    stock_prices = {}

    api_url = "https://finnhub.io/api/v1/quote"

    for symbol in user_stocks:
        params = {"symbol": symbol, "token": api_key}

        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            data = response.json()
            stock_prices[symbol] = data.get("c", 0.0)
        else:
            raise Exception(
                f"Ошибка получения цены акций для {symbol}: {response.status_code}"
            )

    return stock_prices


def load_main_page() -> dict:
    """Загружает пользовательские настройки из файла user_settings.json"""
    setting_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "user_settings.json")
    )
    with open(setting_file, "r", encoding="utf-8") as f:
        return json.load(f)


def display_main_page(date_str: str) -> str:
    """Формирует JSON-ответ для главной страницы"""
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    data = get_transaction_data("operations.xlsx")

    user_settings = load_main_page()
    user_currencies = user_settings.get("user_currencies", ["USD", "EUR"])
    user_stoks = user_settings.get(
        "user_stoks", ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
    )

    # Пример обработки данных
    top_transactions = data.nlargest(5, "Сумма операции")[
        ["Дата операции", "Сумма операции", "Категория", "Описание"]
    ].to_dict(orient="records")

    response = {
        "greeting": get_greeting(date.hour),
        "cards": [
            {"last_digist": "5814", "total_spent": 1262.00, "cashback": 12.62},
            {"last_digist": "7512", "total_spent": 7.94, "cashback": 0.00},
        ],
        "top_transactions": top_transactions,
        "currency_rates": fetch_currency_rates(user_currencies),
        "stock_prices": fetch_stock_prices(user_stoks),
    }
    return json.dumps(response, ensure_ascii=False, indent=4)
