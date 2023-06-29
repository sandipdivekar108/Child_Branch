import logging


def test_getlogger():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is execueted")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has occured")
    logger.critical("Critical Issue")