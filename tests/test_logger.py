import logging
import os

from src.logger import create_basic_logger


def test_create_basic_logger():
    logger_name = "test_logger"
    logger = create_basic_logger(logger_name)

    assert isinstance(logger, logging.Logger)

    log_dir = r"C:\Users\Andrey\PycharmProjects\my_prj\Course_work_3\logs"
    log_file_path = os.path.join(log_dir, f"{logger_name.upper()}.log")

    os.makedirs(log_dir, exist_ok=True)

    logger.info("Это тестовое сообщение для логирования")

    for handler in logger.handlers:
        handler.flush()

    assert os.path.exists(log_file_path), f"Файл не найден: {log_file_path}"

    with open(log_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    assert (
        "Это тестовое сообщение для логирования" in content
    ), "Тестовое сообщение не записалось в лог-файл"
