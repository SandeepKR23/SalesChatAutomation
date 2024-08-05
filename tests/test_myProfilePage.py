from time import sleep
from pageObjects.LoginPage import LoginPage
from pageObjects.MyProfilePage import MyProfilePage
from utilities.BaseClass import BaseClass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestMyProfile(BaseClass):

    def test_myProfilePage(self):
        log = self.getLogger()
        loginPageObject = LoginPage(self.driver)
        loginPageObject.loginPageUsername().send_keys("sandeep2tej@gmail.com")  # obj.functionName.action
        loginPageObject.loginPagePassword().send_keys("P@ss1234")
        loginPageObject.loginPageSubmit().click()
        sleep(3)

        myProfilePageObject = MyProfilePage(self.driver)
        myProfilePageObject.Myprofile_Button_Inbox().click()

        myProfilePageObject.Myprofile_Email().clear()
        myProfilePageObject.Myprofile_Email().send_keys("sandeep2tej@gmail.com")  # obj.functionName.action

        myProfilePageObject.Myprofile_Nickname().clear()
        myProfilePageObject.Myprofile_Nickname().send_keys("SANDY_1")

        myProfilePageObject.Myprofile_Fullname().clear()
        myProfilePageObject.Myprofile_Fullname().send_keys("S@ndeep")
        myProfilePageObject.Myprofile_Submit().click()
        sleep(5)
        # except:
        #     print("Issue in MyProfile page")

        # -----------------------------------SCVisitor--------------------------------------------------------------
        """
        service_obj = Service("C:/Users/rajku-sa/Desktop/Selenium/chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        URL = "https://web-144-90.ect-telecoms.de/preview/d3d5e5193b224781b8eb7393fe5d5f5b/#/MainLayoutGroup/Homepage"
        driver.get(URL)
        driver.refresh()
        driver.maximize_window()
        driver.implicitly_wait(5)

        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH,
                                                   "//lcap-container[@class='lcap-component Rectangle13']//lcap-container[@class='lcap-component Rectangle13']"))).click()
        customer_name = driver.find_elements(By.XPATH,
                                             "(//lcap-container[@class='lcap-component'])[10]//lcap-title//div")
        chatbot_Name = "null"
        for i in customer_name:
            chatbot_Name = i.text
            print(chatbot_Name)
        try:
            assert "SANDY_1" == chatbot_Name
        except:
            print("Miss-match in the Visitor name and chatbot name")
        sleep(5)

        # except:
        #     print("My profile page issue- SCVisitor")
        """
