import os.path

import pandas as pd

from src.logger import create_basic_logger

logger = create_basic_logger(__name__)


def get_transaction_data(filename: str = "operations.xlsx") -> pd.DataFrame:
    """Чтение данных транзакций из Excel-файла"""
    data_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))

    file_path = os.path.join(data_folder, filename)

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")

    try:
        data = pd.read_excel(file_path)
        logger.info(f"Файл {file_path} успешно прочитан.")
        return data
    except Exception as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {str(e)}")
        raise ValueError(f"Не удалось прочитать файл {file_path}. Ошибка:{str(e)}")
