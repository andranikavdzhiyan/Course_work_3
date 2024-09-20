import os.path

import pandas as pd


def get_transaction_data(filename: str = "operations.xlsx") -> pd.DataFrame:
    """Чтение данных транзакций из Excel-файла"""
    data_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

    file_path = os.path.join(data_folder, filename)

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")

    return pd.read_excel(file_path)

