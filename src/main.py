import pandas as pd
from src.views import display_main_page
from src.services import search_personal_transfers
from src.utils import get_transaction_data
from src.reports import spending_by_category

if __name__ == "__main__":
    print(display_main_page("2021-12-28 09:36:56"))

    transactions = [
        {"category": "Переводы", "description": "Перевод Иванов И.П."},
        {"category": "Оплата", "description": "Оплата за услуги"},
        {"category": "Переводы", "description": "Перевод Петров В.А."},
    ]

    print(search_personal_transfers(transactions))
    print(get_transaction_data("operations.xlsx"))

    file_path = "../data/operations.xlsx"
    data = get_transaction_data(file_path)

    data['Дата операции'] = pd.to_datetime(data['Дата операции'], dayfirst=True, format='%d.%m.%Y %H:%M:%S')

    result = spending_by_category(data, category='Переводы', date='2021-12-31')
    print(spending_by_category(result))