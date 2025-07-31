import os
import logging
from datetime import datetime
import structlog

class CustomLogger:
    def __init__(self, log_dir="logs"):
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)

        log_file = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        self.log_file_path = os.path.join(self.logs_dir, log_file)

    def get_logger(self, name=__file__):
        # return logging.getLogger(os.path.basename(name))
        logger_name = os.path.basename(name)

        file_handler = logging.FileHandler(self.log_file_path)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter("%(message)s"))

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter("%(message)s"))

        logging.basicConfig(
            level=logging.INFO,
            handlers=[file_handler, console_handler],
            format="%(message)s",
        )

        structlog.configure(
            processors=[
                structlog.processors.TimeStamper(fmt="iso", utc=True, key="timestamp"),
                structlog.processors.add_log_level,
                structlog.processors.EventRenamer(to="event"),
                structlog.processors.JSONRenderer(),
            ],
            logger_factory=structlog.stdlib.LoggerFactory(),
            cache_logger_on_first_use=True,
        )
        
        return structlog.get_logger(logger_name)


if __name__ == "__main__":
    logger = CustomLogger().get_logger(__file__)
    
    logger.info("This is an info message with Stream and File handlers")
    logger.warning("This is a warning message with Stream and File handlers")
    logger.error("This is an error message with Stream and File handlers")



#### Custom Logger Code using python logging module
# class CustomLogger:
#     def __init__(self, log_dir="logs"):
#         self.logs_dir = os.path.join(os.getcwd(), log_dir)
#         os.makedirs(self.logs_dir, exist_ok=True)

#         log_file = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
#         self.log_file_path = os.path.join(self.logs_dir, log_file)

#     def get_logger(self, name=__file__):
#         # return logging.getLogger(os.path.basename(name))
#         logger_name = os.path.basename(name)
#         logger = logging.getLogger(logger_name)
#         logger.setLevel(logging.INFO)

#         file_formatter = logging.Formatter(
#             "[%(asctime)s] %(levelname)s %(name)s (line: %(lineno)d) - %(message)s"
#         )

#         console_formatter = logging.Formatter(
#             "%(levelname)s - %(message)s"
#         )

#         file_handler = logging.FileHandler(self.log_file_path)
#         file_handler.setFormatter(file_formatter)

#         console_handler = logging.StreamHandler()
#         console_handler.setFormatter(console_formatter)

#         if not logger.handlers:
#             logger.addHandler(file_handler)
#             logger.addHandler(console_handler)
        
#         return logger 
    

# if __name__ == "__main__":
#     logger = CustomLogger().get_logger(__file__)
    
#     logger.info("This is an info message with Stream and File handlers")
#     logger.warning("This is a warning message with Stream and File handlers")
#     logger.error("This is an error message with Stream and File handlers")