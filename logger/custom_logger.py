import os
import logging
from datetime import datetime

class CustomLogger:
    def __init__(self, log_dir="logs"):
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)

        log_file = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        log_file_path = os.path.join(self.logs_dir, log_file)

        logging.basicConfig(
            filename=log_file_path,
            format="[ %(asctime)s ] %(levelname)s %(name)s (line: %(lineno)d) - %(message)s",
            level=logging.INFO
        )

    def get_logger(self, name=__file__):
        return logging.getLogger(os.path.basename(name))
    

if __name__ == "__main__":
    custom_logger = CustomLogger()
    logger = custom_logger.get_logger(__file__)
    
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")