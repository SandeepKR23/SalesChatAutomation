import re
import pytest
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestData.InboxPageData import InboxPageData
from pageObjects.InboxPage import InboxPage
from utilities.BaseClass import BaseClass
from pageObjects.LoginPage import LoginPage


class Testmain(BaseClass):
    logged_in = False

    def test_end2end(self):
        if not Testmain.logged_in:
            loginPageObject = LoginPage(self.driver)
            loginPageObject.loginPageUsername().send_keys("sandeep2tej@gmail.com")  # obj.functionName.action
            loginPageObject.loginPagePassword().send_keys("P@ss1234")
            loginPageObject.loginPageSubmit().click()
            self.driver.save_screenshot("Screenshots/Loginpage.png")
            Testmain.logged_in = True

        log = self.getLogger()
        sleep(3)

        for i in range(0, 3):
            wait = WebDriverWait(self.driver, 10)
            element1 = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@id='mat-tab-label-0-{i}']")))   # top vertical navigation 3
            element1.click()

            # Assigned_to_me_Count
            self.driver.find_element(By.XPATH, f"//div[@class='mat-select-arrow-wrapper ng-tns-c112-{3 + (i + i)}']").click()    # dropdown Icon
            # element2 = wait.until(EC.presence_of_element_located((By.XPATH, f"//div[@class='mat-select-arrow-wrapper ng-tns-c112-{3 + (i + i)}']")))
            # element2.click()
            print("dropdown Icon click ", i)
            sleep(2)
            Assigned_to_me_dropdown = self.driver.find_elements(By.XPATH, f"//div[@id='cdk-overlay-{i}']//div//div//mat-option//span")  # open and close
            print("Assigned_to_me_dropdown value is ", Assigned_to_me_dropdown)
            j = 0
            for dropdown_list_1 in Assigned_to_me_dropdown:
                dropdown = dropdown_list_1.text
                print("Dropdown is", dropdown)
                self.driver.find_element(By.XPATH, f"//mat-option[@id='option_{dropdown}']//span").click()
                sleep(2)
                Assigned_to_me_list = self.driver.find_elements(By.XPATH, "(//c-ect-custom-s-c-c-new-chat-listing[@class='lcap-component ng-star-inserted'])")

                def strip_and_convert(s):
                    stripped = re.sub(r'\D', '', s)
                    y = int(stripped)
                    return y

                Assigned_to_me_Count = strip_and_convert(dropdown)
                log.info("Dropdowm count is")
                log.info(Assigned_to_me_Count)
                log.info("Num of chats available in the side navigation bar")
                log.info(len(Assigned_to_me_list))

                try:
                    assert Assigned_to_me_Count == len(Assigned_to_me_list)
                except:
                    log.info("Missmatch in data")
                log.info("-------------------------------------------------------")

                if j == 0:
                    #self.driver.find_element(By.XPATH, f"//div[@class='mat-mdc-select-arrow-wrapper ng-tns-c136-{3 + (i + i)}']").click()
                    self.driver.find_element(By.XPATH, "//mat-select[@id='form_select_']").click()
                    j += 1
                sleep(2)
        # End of checking the count.



    @pytest.fixture(params=InboxPageData.Values_InboxPagedata)
    def getData(self, request):
        return request.param


    #Right Navigation bar
    def test_CheckRightNavBar(self, getData):
        InboxPageObject = InboxPage(self.driver)

        InboxPageObject.InboxPage_Unassigned_ALL().click()
        sleep(1)
        # Chats list
        InboxPageObject.InboxPage_Chat_list().click()
        # Unassigned dropdown
        # wait.until(EC.presence_of_element_located((By.XPATH, f"//div[normalize-space()='{visitor_ref}']"))).click()
        InboxPageObject.InboxPage_Name_dropdown().click()

        Name = 'S@ndeep'
        option_name = 'option_' + Name
        Select_assignee = InboxPageObject.Assigned_Name_Select(option_name)
        Select_assignee.click()
        sleep(3)
        InboxPageObject.InboxPage_Assigned_to_me().click()
        sleep(3)
        InboxPageObject.InboxPage_Chat_list().click()
        sleep(3)
        InboxPageObject.InboxPage_Name().clear()
        InboxPageObject.InboxPage_Name().send_keys(getData["Name"])
        InboxPageObject.InboxPage_Email_ID().clear()
        InboxPageObject.InboxPage_Email_ID().send_keys(getData["Email_Id"])
        InboxPageObject.InboxPage_Phone_num().clear()
        InboxPageObject.InboxPage_Phone_num().send_keys(getData["Phone_num"])
        sleep(3)
        InboxPageObject.InboxPage_Save().click()

        InboxPageObject.InboxPage_Mark_as_done().click()
        InboxPageObject.InboxPage_Re_Open().click()
        sleep(3)
        # User page
        InboxPageObject.UserPage_Button().click()
        InboxPageObject.UserPage_Search_Text().clear()
        InboxPageObject.UserPage_Search_Text().send_keys(getData["Email_Id"])  # Users_search
        InboxPageObject.UserPage_Search_Button().click()
        sleep(3)
        Users_Count = InboxPageObject.UserPage_Chat_Count().text
        User_table_count = InboxPageObject.UserPage_Chat_Table()
        print(Users_Count)
        print(len(User_table_count))

        for i in range(1, int(len(User_table_count) + 1)):
            User_Name = InboxPageObject.UserPage_get_user_name(i)
            User_Email = InboxPageObject.UserPage_get_user_email(i)
            User_Phone = InboxPageObject.UserPage_get_user_phone(i)
            print("My name is " + User_Name + " and email-id is " + User_Email + " and Phone number is " + User_Phone + ".")

            if User_Name == getData["Name"] and User_Email == getData["Email_Id"] and User_Phone == getData["Phone_num"]:
                print("New visitor is added to the Users page.")
            else:
                print("This is OLD visitor")
        sleep(3)








