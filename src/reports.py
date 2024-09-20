import json
from datetime import datetime, timedelta
from functools import wraps
from src.utils import get_transaction_data
import os

import pandas as pd


def save_report(filename: str = "report.json"):
    """Декоратор для записи отчетов в файл."""
    output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'reports'))

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            os.makedirs(output_folder, exist_ok=True)
            file_path = os.path.join(output_folder, filename)

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=4)
            return result

        return wrapper

    return decorator


@save_report("spending_by_category.json")
def spending_by_category(data: pd.DataFrame, category: str, date: str = None) -> str:
    """Возвращает траты по заданной категории"""
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    current_date = datetime.strptime(date, "%Y-%m-%d")

    three_mounths_ago = current_date - timedelta(days=90)

    filtered_data = data[
        (data["Дата операции"] >= three_mounths_ago)
        & (data["Дата операции"] <= current_date)
        & (data["Категория"] == category)
    ]

    total_spent = round(filtered_data["Сумма операции"].sum(), 2)

    result = {
        "category": category,
        "total_spent": total_spent,
        "from": three_mounths_ago.strftime("%Y-%m-%d"),
        "to": current_date.strftime("%Y-%m-%d"),
    }

    return result


if __name__ == '__main__':
    data = get_transaction_data("operations.xlsx")

    data['Дата операции'] = pd.to_datetime(data['Дата операции'], dayfirst=True, format='%d.%m.%Y %H:%M:%S')

    result = spending_by_category(data, category='Переводы', date='2021-12-31')
