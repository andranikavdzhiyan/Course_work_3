
import pytest

from unittest.mock import patch
from src.utils import get_transaction_data


@patch("src.utils.pd.read_excel")
@patch("src.utils.os.path.isfile")
@patch("src.utils.os.path.abspath")
def test_get_transaction_data_read_error(mock_abspath, mock_isfile, mock_read_excel):
    mock_abspath.return_value = "/fake_path/data/operations.xlsx"
    mock_isfile.return_value = True

    # Симулируем ошибку при чтении файла
    mock_read_excel.side_effect = Exception("Ошибка чтения файла")

    # Проверяем, что функция вызывает ValueError при ошибке чтения
    with pytest.raises(ValueError, match="Не удалось прочитать файл"):
        get_transaction_data("operations.xlsx")
