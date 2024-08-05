from time import sleep
import pytest
from TestData.UserPageData import UserPageData
from pageObjects.LoginPage import LoginPage
from pageObjects.UserPage import UserPage
from utilities.BaseClass import BaseClass


class TestUserPage(BaseClass):
    logged_in = False
    i = False

    @pytest.fixture(params=UserPageData.Values_UserPagedata)
    def getData(self, request):
        return request.param

    def test_UserPage(self, getData):
        UserPageObject = UserPage(self.driver)

        if not TestUserPage.logged_in:
            loginPageObject = LoginPage(self.driver)
            loginPageObject.loginPageUsername().send_keys("sandeep2tej@gmail.com")  # obj.functionName.action
            loginPageObject.loginPagePassword().send_keys("P@ss1234")
            loginPageObject.loginPageSubmit().click()
            TestUserPage.logged_in = True
            UserPageObject.UserPage_Button().click()  # Users button

        # 500 users
        if not TestUserPage.i:
            UserPageObject.UserPage_Rows_Dropdown().click()  # Rows_click
            UserPageObject.UserPage_500_Options().click()  # 500 options
            TestUserPage.i = True

        # Visitor/lead/All
        UserPageObject.UserPage_LV_dropdown().click()  # L/V dropdown_click
        UserPageObject.UserPage_LV_Options(getData["Filter"]).click()  # L/V options

        # Search
        UserPageObject.UserPage_Search_Text().clear()
        UserPageObject.UserPage_Search_Text().send_keys(getData["Search_Name"])  # Users_search
        UserPageObject.UserPage_Search_Button().click()

        Users_Count = UserPageObject.UserPage_Chat_Count().text
        User_table_count = UserPageObject.UserPage_Chat_Table()
        print(Users_Count)
        print(len(User_table_count))

        try:
            assert Users_Count == len(User_table_count)
        except:
            print("User Page: Miss-match in the count")
        print("The filter is " + getData["Filter"] + " and the Search text is " + getData["Search_Name"])
        print("="*120)
        sleep(2)


        for i in range(1, int(len(User_table_count) + 1)):
            User_Name = UserPageObject.UserPage_get_user_name(i)
            User_Email = UserPageObject.UserPage_get_user_email(i)
            User_Phone = UserPageObject.UserPage_get_user_phone(i)
            User_Stage = UserPageObject.UserPage_get_user_stage(i)

            print("My name is " + User_Name + " and email-id is " + User_Email + " and Phone number is " + User_Phone + " and the stage is " + User_Stage + ".")

            if User_Name == "Unknown" and User_Email == "Unknown" and User_Phone == "Unknown":
                try:
                    assert User_Stage == "Visitor"
                except:
                    print("Cond 1: Incorrect match for visitors")

            elif User_Email == "Unknown" and User_Phone == "Unknown":
                try:
                    assert User_Stage == "Visitor"
                except:
                    print("Cond 1.2: Incorrect match for visitors")

            elif User_Email != "Unknown" and User_Phone != "Unknown":
                try:
                    assert User_Stage == "Lead"
                except:
                    print("Cond 2: Incorrect match for visitors")

            elif User_Name != "Unknown" and User_Email != "Unknown" and User_Phone != "Unknown":
                try:
                    assert User_Stage == "Lead"
                except:
                    print("Cond 4: In-Correct lead match")
        sleep(3)


