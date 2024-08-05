from time import sleep

from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestSCVisitorApp(BaseClass):
    logged_in = False

    # Function to initialize and return the driver object for visitor page
    def visitor_page_driver(self):
        service_obj = Service("C:/Users/rajku-sa/Desktop/Selenium/drivers/chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        URL = "https://web-255-92.ect-telecoms.de/preview/b8ec3115854c467c8bec0be008cf11b7/#/MainLayoutGroup/Homepage"
        driver.get(URL)
        driver.maximize_window()
        return driver

    # Function to initialize and return the driver object for agent page
    def agent_page_driver(self):
        if not TestSCVisitorApp.logged_in:
            loginPageObject = LoginPage(self.driver)
            loginPageObject.loginPageUsername().send_keys("sandeep2tej@gmail.com")  # obj.functionName.action
            loginPageObject.loginPagePassword().send_keys("P@ss1234")
            loginPageObject.loginPageSubmit().click()
            TestSCVisitorApp.logged_in = True
        return self.driver

    def test_conversation(self):
        visitor_message = "Hello, can you help me with my issue?"
        New_visitor_message = "I have issue with my Laptop"
        Email_Id = 'Sandeep2tej@gmail.com'
        Phone_num = '49121548596121'

        # Initialize the visitor page driver
        visitor_driver = TestSCVisitorApp.visitor_page_driver(self)
        visitor_driver.implicitly_wait(10)

        # Locate and send a message from the visitor page
        wait = WebDriverWait(visitor_driver, 20)  # wait for bot
        wait.until(EC.presence_of_element_located((By.XPATH, "//lcap-container[@class='lcap-component Rectangle13']//lcap-container[@class='lcap-component Rectangle13']"))).click()

        visitor_driver.find_element(By.XPATH, "//input[@id='input_']").send_keys(visitor_message)
        visitor_driver.find_element(By.XPATH, "//lcap-image[@class='lcap-component ng-untouched ng-pristine ng-valid ng-star-inserted']//img[@alt='alt config']").click()
        sleep(2)
        ConvID = visitor_driver.execute_script("return window.localStorage.getItem('ConvId');")
        print("Visitor reference is ", ConvID)

        Visitor_Name = 'Site Visitor ' + str(ConvID)
        print(Visitor_Name)
        Name = 'Tester S ' + str(ConvID)
        agent_message = 'Of course! I will do my best to assist you. What is the issue? ' + Visitor_Name

        # Initialize the agent page driver
        self.driver = TestSCVisitorApp.agent_page_driver(self)
        self.driver.find_element(By.ID, "mat-tab-label-0-1").click()  # Assigned/Unassigned/All
        sleep(2)
        # wait.until(EC.presence_of_element_located((By.XPATH, f"//div[normalize-space()='{Visitor_Name}']"))).click()
        self.driver.find_element(By.XPATH, f"//div[normalize-space()='{Visitor_Name}']").click()

        self.driver.find_element(By.XPATH, "//input[@placeholder='Write a reply']").send_keys(agent_message)
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Send']").click()  # send button
        sleep(2)

        # Verify the messages
        message_count = len(self.driver.find_elements(By.XPATH, "(//lcap-paragraph[@stl='text-align: left;'])"))
        print('Message count length is ',message_count)
        #agent_text = self.driver.find_elements(By.XPATH, "(//lcap-container[@class='lcap-component AgentMessageColor'])")[message_count-1].text
        agent_text = self.driver.find_element(By.XPATH, "(//lcap-container[@class='lcap-component AgentMessageColor'])").text
        agent_text1 = agent_text.strip(' ')
        print("Last message of agent is :", agent_text1)

        # Main details Name, Email, Phone
        self.driver.find_element(By.XPATH, "(//input[@id='input_'])[2]").clear()
        self.driver.find_element(By.XPATH, "(//input[@id='input_'])[2]").send_keys(Name)  # Name
        self.driver.find_element(By.XPATH, "(//input[@id='input_'])[3]").clear()
        self.driver.find_element(By.XPATH, "(//input[@id='input_'])[3]").send_keys(Email_Id)  # Email
        self.driver.find_element(By.XPATH, "(//input[@id='input_'])[4]").clear()
        self.driver.find_element(By.XPATH, "(//input[@id='input_'])[4]").send_keys(Phone_num)  # Phone num
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Save']").click()  # Save

        # Visitor side message check
        visitor_driver.switch_to.window(visitor_driver.window_handles[0])

        visitor_driver.find_element(By.XPATH, "//input[@id='input_']").send_keys(New_visitor_message)
        visitor_driver.find_element(By.XPATH, "//lcap-image[@class='lcap-component ng-untouched ng-pristine ng-valid ng-star-inserted']//img[@alt='alt config']").click()
        sleep(2)
        # Verify the messages on the visitor page
        visitor_message_count = len(visitor_driver.find_elements(By.XPATH, "(//lcap-paragraph[@stl='text-align: left;'])"))
        print("visitor_message_count is ", visitor_message_count)
        visitor_text = visitor_driver.find_elements(By.XPATH, "(//lcap-paragraph[@stl='text-align: left;'])")[visitor_message_count - 2].text
        visitor_text1 = visitor_text.strip()
        print("Last message on visitor page:", visitor_text1)
        sleep(5)

        # Check if the messages match
        assert visitor_text1 == agent_text1, f"Expected text: {visitor_text1}, but got: {agent_text1}"


