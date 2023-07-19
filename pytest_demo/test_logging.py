import logging


def test_logging_demo():

    # Capture the filename in the __name__ parameter. Mandatory to give this
    logger = logging.getLogger(__name__)

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

    # What to print in log file
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue")