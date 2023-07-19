import inspect
import logging


class LogClass:

    def get_logger(self):

        logger_name = inspect.stack()[1][3]
        # Capture the filename in the __name__ parameter. Mandatory to give this
        logger = logging.getLogger(logger_name)

        # Log file creation
        fileHandler = logging.FileHandler("logfile.log")

        # Log format - How to print logs
        # YYYY-MM-DD HH:MM:SS,MMS :LOG_LEVEL : TEST_NAME :LOG_MESSAGE
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

        # Tell the fileHandler object how to format the log file
        fileHandler.setFormatter(formatter)

        # Giving the logger in which file it has to print the logs - Where to print logs
        logger.addHandler(fileHandler)

        # Setting level of logging
        # At INFO level, debu logs won't be printed
        logger.setLevel(logging.DEBUG)

        return logger
