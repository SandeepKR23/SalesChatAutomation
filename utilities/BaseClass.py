import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('C:/Users/rajku-sa/PycharmProjects/SalesChatAutomation/utilities/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyPreviewWait(self):
        wait = WebDriverWait(self.driver, 150)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "(//button[@id='preview-get-started'])[1]")))

    def verifyLinkPresenceWait(self, text):
        wait = WebDriverWait(self.driver, 150)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))