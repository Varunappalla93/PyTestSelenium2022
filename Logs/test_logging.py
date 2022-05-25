import logging

def test_logdemo():
    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('logfile.log')

    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)

    logger.setLevel(logging.INFO)

    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Something is in warning mode")

    logger.error("Error occurred")

    logger.critical("Critical Issue")