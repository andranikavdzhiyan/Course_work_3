import json
import pytest
from src.services import search_personal_transfers


@pytest.fixture
def test_transactions():
    """Создаем тестовый набор данных"""
    return [
        {"category": "Переводы", "description": "Иванов И.И."},
        {"category": "Переводы", "description": "Петров П."},
        {"category": "Переводы", "description": "Тест Т."},
        {"category": "Покупка", "description": "Магазин"},
        {"category": "Переводы", "description": "Неправильный формат"},
        {"category": "Переводы", "description": "Сидоров С.А."},
    ]


def test_empty_transactions():
    """Тестируем функцию с пустум списком транзакций."""
    result = search_personal_transfers([])
    assert result == json.dumps([]), "Ожидался пустой JSON для пустого списка транзакций."


def test_no_personal_transfers(test_transactions):
    """Тестируем функцию, когда нет переводов физ.лицам."""
    for txn in test_transactions:
        txn['category'] = 'Покупка'

    result = search_personal_transfers(test_transactions)
    assert result == json.dumps([]), "Ожидался пустой JSON для пустого списка транзакций."


def test_some_personal_transfers(test_transactions):
    result = search_personal_transfers(test_transactions)
    expected_result = [
        {"category": "Переводы", "description": "Иванов И.И."},
        {"category": "Переводы", "description": "Сидоров С.А."},
    ]
    assert json.loads(result) == expected_result, "Фильтрация переводов физ.лицам не сработала"
