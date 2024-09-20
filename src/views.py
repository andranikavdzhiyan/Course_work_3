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


def fetch_currency_rates() -> dict[str, float]:
    """Получает курс валют из API"""
    api_key_1 = "API_EXC_API_KEY"
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    params = {"access_key": api_key_1}
    response = requests.get(api_url, params=params)
    response.raise_for_status()

    data = response.json()

    if not isinstance(data, dict):
        raise ValueError("Ответ от API не является словарем")

    return {
        "USD": data.get("rates", {}).get("USD", 1.0),
        "EUR": data.get("rates", {}).get("EUR", 0.1),
    }


def fetch_stock_prices() -> dict[str, float]:
    """Получает цены акций из API"""
    symbols = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
    stock_prices = {}

    api_url = "https://finnhub.io/api/v1/quote"

    for symbol in symbols:
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


def display_main_page(date_str: str) -> str:
    """Формирует JSON-ответ для главной страницы"""
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    data = get_transaction_data(
        "C:/Users/Andrey/PycharmProjects/my_prj/Course_work_3/data/operations.xlsx"
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
        "currency_rates": fetch_currency_rates(),
        "stock_prices": fetch_stock_prices(),
    }
    return json.dumps(response, ensure_ascii=False, indent=4)
