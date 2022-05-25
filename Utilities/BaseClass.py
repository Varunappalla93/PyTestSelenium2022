import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, ele_text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, ele_text)))

    def SelectByOption(self, loc, text):
        sel = Select(loc)
        sel.select_by_visible_text(text)

    def getlogger(self):
        loggerName = inspect.stack()[1][3]  # to get correct methodname in log file
        logger = logging.getLogger(loggerName)

        # logger = logging.getLogger(__name__) # gives wrong classname in log file

        filehandler = logging.FileHandler('logfile.log')

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel(logging.INFO)
        return logger
