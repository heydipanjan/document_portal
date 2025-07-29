import sys
import traceback

from logger.custom_logger import CustomLogger

logger = CustomLogger().get_logger(__file__)

class DocumentPortalException(Exception):
    """Base class for all exceptions in the Document Portal."""
    def __init__(self, error_message:str, error_details:sys):
        _,_,exc_traceback = error_details.exc_info()
        self.file_name = exc_traceback.tb_frame.f_code.co_filename
        self.lineno = exc_traceback.tb_lineno
        self.error_message = str(error_message)
        self.traceback_str = ''.join(traceback.format_exception(*error_details.exc_info()))

    def __str__(self):
        return f"""
        Error in [{self.file_name} at line {self.lineno}]
        Message: {self.error_message}
        Traceback: {self.traceback_str}
        """

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        doc_exception = DocumentPortalException(e, sys)
        logger.error(doc_exception)
        raise doc_exception

