import json
import os
from datetime import datetime

import pandas as pd
import pytest

from src.reports import spending_by_category


@pytest.fixture
def test_data():
    """Создаем тестовый набор данных."""
    data = {
        "Дата операции": [
            datetime(2024, 8, 1),
            datetime(2024, 8, 15),
            datetime(2024, 9, 1),
            datetime(2024, 9, 15),
            datetime(2024, 9, 30),
            datetime(2024, 10, 1),
        ],
        "Категория": [
            "Еда",
            "Еда",
            "Транспорт",
            "Еда",
            "Транспорт",
            "Еда",
        ],
        "Сумма операции": [100, 150, 200, 50, 300, 400],
    }
    return pd.DataFrame(data)


def test_spending_by_category(test_data):
    """Тестируем функцию spending_by_category."""
    category = "Еда"
    expected_total_spent = 700

    now = datetime.now()

    result = spending_by_category(test_data, category)

    assert result["category"] == category
    assert result["total_spent"] == expected_total_spent

    output_folder = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "reports")
    )
    file_path = os.path.join(output_folder, "spending_by_category.json")

    assert os.path.exists(file_path), f"Файл отчета не найден: {file_path}"

    with open(file_path, "r", encoding="utf-8") as f:
        content = json.load(f)

    assert content["category"] == category
    assert content["total_spent"] == expected_total_spent
    assert content["from"] == "2024-07-06"
    assert content["to"] == now.strftime("%Y-%m-%d")
