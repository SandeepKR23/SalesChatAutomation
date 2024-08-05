from time import sleep
import pytest
from selenium.webdriver.common.by import By

from TestData.ChatbotPageData import ChatbotPageData
from pageObjects.ChatbotPage import ChatbotPage
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class TestChatbotPage(BaseClass):
    logged_in = False

    @pytest.fixture(params=ChatbotPageData.Values_ChatbotPageData)
    def getData(self, request):
        return request.param

    def test_ChatbotsPage(self, getData):
        Chatbot_Object = ChatbotPage(self.driver)

        if not TestChatbotPage.logged_in:
            loginPageObject = LoginPage(self.driver)
            loginPageObject.loginPageUsername().send_keys("sandeep2tej@gmail.com")  # obj.functionName.action
            loginPageObject.loginPagePassword().send_keys("P@ss1234")
            loginPageObject.loginPageSubmit().click()
            TestChatbotPage.logged_in = True

        Chatbot_Object.ChatbotPage_button().click()

        """
        # Check Existing Name ---------------------------------------------------------------------
        Chatbot_Object.NewChatbot_button().click()
        Chatbot_Object.Enter_chatbot_name().send_keys(getData["Existing_Name"])
        sleep(1)
        Char_count = Chatbot_Object.Character_Count().text
        try:
            assert int(Char_count) == len(getData["Existing_Name"])
        except:
            print("Character count MISS-MATCH in Existing_Name")

        try:
            SameName_Check = Chatbot_Object.Check_Name_existsORnot().text
            assert SameName_Check.strip() == 'This Name already exists. Enter a new one'
        except:
            print("Miss-match: This Name already exists")

        Chatbot_Object.Cancel_button().click()

        # Check Greater than 80 characters ----------------------------------------------------------
        Chatbot_Object.NewChatbot_button().click()
        Chatbot_Object.Enter_chatbot_name().send_keys(getData["Greater_then_80"])
        sleep(1)
        Char_count = Chatbot_Object.Character_Count().text
        try:
            assert int(Char_count) == len(getData["Greater_then_80"])
        except:
            print("Character count MISS-MATCH in Greater_then_80")

        try:
            Check_validation_80 = Chatbot_Object.Check_Name_existsORnot().text
            assert Check_validation_80.strip() == 'Name should contain less than 80 characters'
        except:
            print("Miss-match not working: Name should contain less than 80 characters")
        Chatbot_Object.Cancel_button().click()

        # Symbols ------------------------------------------------------------------------------------
        Chatbot_Object.NewChatbot_button().click()
        Chatbot_Object.Enter_chatbot_name().send_keys(getData["Sybmols"])
        try:
            Check_Null_name = Chatbot_Object.Check_Name_existsORnot().text
            print(Check_Null_name.strip())
            assert Check_Null_name.strip() == 'Oops! This format is not supported'
        except:
            print("Miss-match: This format is not supported for Symbols")

        Chatbot_Object.Cancel_button().click()
        """
        """
        # Remove name --------------------------------------------------------------------------------
        Chatbot_Object.NewChatbot_button().click()
        Chatbot_Object.Enter_chatbot_name().send_keys(getData["Existing_Name"])
        Chatbot_Object.Enter_chatbot_name().clear()
        Char_count = Chatbot_Object.Character_Count().text
        try:
            assert int(Char_count) == len(getData["Greater_then_80"])
        except:
            print("Character count MISS-MATCH in Null name")

        try:
            Check_Null_name = Chatbot_Object.Check_Name_existsORnot().text
            assert Check_Null_name.strip() == 'Oops! a Layout Name is needed here'
        except:
            print("mismatch- This Name already exists")
        Chatbot_Object.Cancel_button().click()
        """
        sleep(4)
        Chatbot_names = self.driver.find_elements(By.XPATH, "//c-ect-sch-bot-flow-table[@id='flowtable_1']//lcap-container//lcap-dynamic-table//table//tbody//tr//td[2]//div")

        for chatbot in Chatbot_names:
            print(chatbot.text)
            sleep(4)
            if chatbot.text == getData["New_Name"]:
                print(chatbot.text)
                self.driver.find_element(By.XPATH,"//body[1]/app[1]/state-flows_top_bar[1]/c-main-template[1]/l-main-layout[1]/div[1]/div[2]/div[2]/lcap-container[1]/state-flows_main[1]/lcap-container[1]/lcap-container[1]/lcap-container[3]/lcap-container[1]/c-ect-sch-bot-flow-table[1]/lcap-container[1]/lcap-dynamic-table[1]/table[1]/tbody[1]/tr[1]/td[5]/lcap-container[1]/c-ect-sch-bot-table-icons[1]/lcap-container[1]/lcap-container[1]/lcap-icon[1]/div[1]/i[1]").click()
                self.driver.find_element(By.XPATH,"//lcap-container[@class='lcap-component menuItemIndex ng-star-inserted']//lcap-container[1]").click()
                sleep(5)



        """
        # Create Chatbot
        Chatbot_Object.NewChatbot_button().click()
        Chatbot_Object.Enter_chatbot_name().send_keys(getData["New_Name"])
        Chatbot_Object.Create_button().click()

        # Edit chatbot
        Chatbot_Object.End_step_button().click()
        Chatbot_Object.Starting_step_button().click()
        
        Chatbot_Object.Step_0_field_click().click()
        
        # Switch to new window
        sleep(2)
        main_window_handle = self.driver.current_window_handle
        self.driver.switch_to.window(self.driver.window_handles[-1])
        sleep(4)
        Chatbot_Object.Step_0_field_Input().send_keys('Hello, Welcome to ECT')
        sleep(4)
        # Switch back to main window
        self.driver.close()
        sleep(4)
        self.driver.switch_to.window(main_window_handle)
        sleep(2)
        """

        # sleep(4)
        # self.driver.switch_to.window(self.driver.window_handles[1])
        # Chatbot_Object.Step_0_field_Input().send_keys('Hello, Welcome to ECT')
        # sleep(2)
        # self.driver.switch_to.window(self.driver.window_handles[0])
        # sleep(2)

        # Chatbot_Object.Step_1_button().click()
        # Chatbot_Object.Step_2_button().click()
        # Chatbot_Object.Step_3_button().click()
        # Chatbot_Object.Step_4_button().click()

        # Chatbot_Object.End_step_button().click()
        sleep(5)

    def test_Schedule_triggers(self, getData):
        Chatbot_Object2 = ChatbotPage(self.driver)

        # Triggers
        Chatbot_Object2.Triggers_button().click()
        Chatbot_Object2.Add_Triggers_dropdown().click()
        sleep(3)
        Chatbot_Object2.Current_Page_checkbox().click()
        Chatbot_Object2.Time_Spent_checkbox().click()
        Chatbot_Object2.Total_Visits_checkbox().click()
        sleep(3)
        sleep(3)
        Chatbot_Object2.Current_Page_URL_filed_2().send_keys('preview')

        Chatbot_Object2.Triggers_button().click()

        Chatbot_Object2.Time_Spent_field_1().send_keys('10')
        sleep(3)
        Chatbot_Object2.Time_Spent_field2_dropdown().click()
        sleep(3)
        Chatbot_Object2.Time_Spent_field2_option().click()

        Chatbot_Object2.Total_Visits_field1_dropdown().click()
        Chatbot_Object2.Total_Visits_field1_option().click()
        Chatbot_Object2.Total_Visits_field_2().send_keys('2')
        Chatbot_Object2.Total_Visits_field_3().send_keys('1')
        Chatbot_Object2.Triggers_publish_button().click()



        # Schedule
        Chatbot_Object2.Schedule_button().click()
        Chatbot_Object2.Schedule_Stop_Showing().click()
        Chatbot_Object2.Schedule_Bot_Flow().click()
        Chatbot_Object2.Schedule_Save().click()




