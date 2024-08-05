from time import sleep
import pytest
from prompt_toolkit.contrib.telnet.protocol import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="session")
def browser():
    service_obj = Service("C:/Users/rajku-sa/Desktop/Selenium/drivers/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    URL = "https://web-255-92.ect-telecoms.de/preview/cd7cdbe84d6547b4a81f4e4c48395dfa/#/MainLayoutGroup/Homepage"
    driver.get(URL)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_chatbot_load(browser):

    #browser.get("https://web-255-92.ect-telecoms.de/preview/cd7cdbe84d6547b4a81f4e4c48395dfa/#/MainLayoutGroup/Homepage")
    sleep(1)

    for i in range(10):
        # Open a new browser window
        browser.execute_script("window.open();")
        browser.switch_to.window(browser.window_handles[-1])
        browser.get("https://web-255-92.ect-telecoms.de/preview/cd7cdbe84d6547b4a81f4e4c48395dfa/#/MainLayoutGroup/Homepage")
        # Simulate user interaction with the chatbot

        visitor_message = "Hello, can you help me with my issue?"

        # --------------------------------------------------------------------------------------------------------------------------------------
        # Initialize the visitor page driver
        visitor_driver = webdriver.Chrome(service=Service("C:/Users/rajku-sa/Desktop/Selenium/drivers/chromedriver_win32/chromedriver.exe"))
        # Locate and send a message from the visitor page
        wait = WebDriverWait(visitor_driver, 20)  # wait for bot
        wait.until(EC.presence_of_element_located((By.XPATH,
                                                   "//lcap-container[@class='lcap-component Rectangle13']//lcap-container[@class='lcap-component Rectangle13']"))).click()

        visitor_driver.find_element(By.XPATH, "//input[@id='input_']").send_keys(visitor_message)
        visitor_driver.find_element(By.XPATH,
                                    "//lcap-image[@class='lcap-component ng-untouched ng-pristine ng-valid ng-star-inserted']//img[@alt='alt config']").click()
        sleep(5)
