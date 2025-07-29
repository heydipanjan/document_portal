import os
import logging
from datetime import datetime

class CustomLogger:
    def __init__(self, log_dir="logs"):
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)

        log_file = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        self.log_file_path = os.path.join(self.logs_dir, log_file)

        # logging.basicConfig(
        #     filename=log_file_path,
        #     format="[ %(asctime)s ] %(levelname)s %(name)s (line: %(lineno)d) - %(message)s",
        #     level=logging.INFO
        # )

    def get_logger(self, name=__file__):
        # return logging.getLogger(os.path.basename(name))
        logger_name = os.path.basename(name)
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)

        file_formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s %(name)s (line: %(lineno)d) - %(message)s"
        )

        console_formatter = logging.Formatter(
            "%(levelname)s - %(message)s"
        )

        file_handler = logging.FileHandler(self.log_file_path)
        file_handler.setFormatter(file_formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(console_formatter)

        if not logger.handlers:
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)
        
        return logger 
    

if __name__ == "__main__":
    logger = CustomLogger().get_logger(__file__)
    
    logger.info("This is an info message with Stream and File handlers")
    logger.warning("This is a warning message with Stream and File handlers")
    logger.error("This is an error message with Stream and File handlers")