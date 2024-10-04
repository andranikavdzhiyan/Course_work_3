import json
import re
from typing import Dict, List

from src.logger import create_basic_logger

logger = create_basic_logger(__name__)


def search_personal_transfers(transactions: List[Dict[str, str]]) -> str:
    """Возвращает JSON с транзакциями перевода физ.лицам"""
    pattern = pattern = r"[А-Я][а-я]+\s[А-Я]\.[А-Я]\."
    if not transactions:
        logger.warning("Передан пустой список транзакций.")
        return json.dumps([])

    result = [
        txn
        for txn in transactions
        if txn.get("category") == "Переводы"
        and re.search(pattern, txn.get("description"))
    ]

    result_json = json.dumps(result, ensure_ascii=False, indent=4)

    logger.info(
        f"Исходные транзакции: {json.dumps(transactions, ensure_ascii=False, indent=4)}"
    )
    logger.info(f"Фильтрованные транзакции: (Перевод физ.лицам) {result_json}")

    return result_json
