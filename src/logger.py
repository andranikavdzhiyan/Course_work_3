import logging
import os


def create_basic_logger(name: str) -> logging.Logger:
    name_file = name.replace(".", "_").upper()

    logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")

    os.makedirs(logs_dir, exist_ok=True)

    log_file = os.path.join(logs_dir, f"{name_file}.log")

    logger = logging.getLogger(name)

    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler(log_file, encoding="utf-8-sig")
    file_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - (%(name)s.%(funcName)s): %(message)s"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)

    logger.debug(f"Logger {name} создан. Путь до файла: {log_file}")

    return logger
