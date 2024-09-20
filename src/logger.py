import logging
import os


def create_basic_logger(name: str) -> logging.Logger:
    name_file = name
    while True:
        if "." in name_file:
            name_file = (
                name_file[: name_file.index(".")].upper()
                + "_"
                + name_file[name_file.index(".") + 1:]
            )
        else:
            break

    logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")

    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    log_file = os.path.join(logs_dir, f"{name_file}.log")

    with open(log_file, "w"):
        pass

    logger = logging.getLogger(name)
    file_handler = logging.FileHandler(log_file)
    file_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - (%(name)s.%(funcName)s): %(message)s"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)

    return logger
