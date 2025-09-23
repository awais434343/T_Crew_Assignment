import logging
import os
from datetime import datetime
import sys


class FrameworkLogger:
    @staticmethod
    def get_logger(name: str = "Framework"):
        log_folder = "logs"
        os.makedirs(log_folder, exist_ok=True)

        log_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_filename = f"{log_folder}/test_log_{log_time}.log"

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        if not logger.handlers:
            # File handler with UTF-8
            file_handler = logging.FileHandler(log_filename, mode='a', encoding='utf-8')

            # Stream handler with UTF-8 encoding
            console_handler = logging.StreamHandler(sys.stdout)

            formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s")
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger
