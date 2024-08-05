from time import sleep
import pytest
from selenium.webdriver.common.by import By
from TestData.BusinessHoursData import BusinessHoursData
from pageObjects.BusinessHours import BusinessHours
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class TestBusinessHours(BaseClass):
    logged_in = False

    @pytest.fixture(params=BusinessHoursData.Values_BusinessHoursdata)
    def getData(self, request):
        return request.param

    def test_BusinessHoursPage(self, getData):
        businessHoursObject = BusinessHours(self.driver)

        if not TestBusinessHours.logged_in:
            loginPageObject = LoginPage(self.driver)
            loginPageObject.loginPageUsername().send_keys("sandeep2tej@gmail.com")  # obj.functionName.action
            loginPageObject.loginPagePassword().send_keys("P@ss1234")
            loginPageObject.loginPageSubmit().click()
            TestBusinessHours.logged_in = True

        businessHoursObject.settingsPagebutton().click()                        # Settings
        businessHoursObject.businessHoursOptionbutton().click()                 # Businesshours
        businessHoursObject.businesshours_Time_Dropdown_Click().click()         # Timestamp dropdown click
        sleep(1)

        # Timezone
        Timezone_list = businessHoursObject.businesshours_Time_Dropdown_List()
        print("The total count of the time-zones are ", len(Timezone_list))
        Timezone_option_element = businessHoursObject.businesshours_Time_Dropdown_Select(getData["Timezone_partial_text"])
        Timezone_option_element.click()

        # RegularHours
        businessHoursObject.businesshours_RegularHours_Dropdown().click()
        # RegularHours_list = businessHoursObject.businesshours_RegularHours_Dropdown_List()
        # print(RegularHours_list)
        # print("The total count of the Regular hours are ", len(RegularHours_list))

        if getData["RegularHours_value"] == "Everyday":
            BusinessHours_option = businessHoursObject.businesshours_RegularHours_Dropdown_Select(getData["RegularHours_value"])
            BusinessHours_option.click()

            businessHoursObject.businesshours_RegularHours_EDF1_Dropdown().click()
            RH_Time_1_Select = businessHoursObject.businesshours_RegularHours_EDF1_Dropdown_Select('08:00')
            ActionChains(self.driver).move_to_element(RH_Time_1_Select).perform()
            RH_Time_1_Select.click()
            sleep(2)
            businessHoursObject.businesshours_RegularHours_EDF2_Dropdown().click()
            RH_Time_2_Select = businessHoursObject.businesshours_RegularHours_EDF2_Dropdown_Select('12:00')
            sleep(2)
            ActionChains(self.driver).move_to_element(RH_Time_2_Select).perform()

            RH_Time_2_Select.click()
            sleep(1)

            businessHoursObject.businessHours_PlusIcon().click()  # +plus icon

            businessHoursObject.businesshours_RegularHours_EDF3_Dropdown().click()
            RH_Time_3_Select = businessHoursObject.businesshours_RegularHours_EDF3_Dropdown_Select('13:00')
            ActionChains(self.driver).move_to_element(RH_Time_3_Select).perform()
            RH_Time_3_Select.click()
            businessHoursObject.businesshours_RegularHours_EDF4_Dropdown().click()
            RH_Time_4_Select = businessHoursObject.businesshours_RegularHours_EDF4_Dropdown_Select('17:00')
            ActionChains(self.driver).move_to_element(RH_Time_4_Select).perform()
            RH_Time_4_Select.click()
            sleep(2)

        elif getData["RegularHours_value"] == "Weekends":
            BusinessHours_option = businessHoursObject.businesshours_RegularHours_Dropdown_Select(getData["RegularHours_value"])
            BusinessHours_option.click()

            businessHoursObject.businesshours_RegularHours_EDF1_Dropdown().click()
            RH_Time_1_Select = businessHoursObject.businesshours_RegularHours_EDF1_Dropdown_Select('08:15')
            ActionChains(self.driver).move_to_element(RH_Time_1_Select).perform()
            RH_Time_1_Select.click()
            businessHoursObject.businesshours_RegularHours_EDF2_Dropdown().click()
            RH_Time_2_Select = businessHoursObject.businesshours_RegularHours_EDF2_Dropdown_Select('12:15')
            ActionChains(self.driver).move_to_element(RH_Time_2_Select).perform()
            RH_Time_2_Select.click()
            sleep(1)

            businessHoursObject.businessHours_PlusIcon().click()  # +plus icon

            businessHoursObject.businesshours_RegularHours_EDF3_Dropdown().click()
            RH_Time_3_Select = businessHoursObject.businesshours_RegularHours_EDF3_Dropdown_Select('13:00')
            ActionChains(self.driver).move_to_element(RH_Time_3_Select).perform()
            RH_Time_3_Select.click()
            businessHoursObject.businesshours_RegularHours_EDF4_Dropdown().click()
            RH_Time_4_Select = businessHoursObject.businesshours_RegularHours_EDF4_Dropdown_Select('17:00')
            ActionChains(self.driver).move_to_element(RH_Time_4_Select).perform()
            RH_Time_4_Select.click()

        elif getData["RegularHours_value"] == "Mon. to Fri.":
            BusinessHours_option = businessHoursObject.businesshours_RegularHours_Dropdown_Select(getData["RegularHours_value"])
            BusinessHours_option.click()

            businessHoursObject.businesshours_RegularHours_EDF1_Dropdown().click()
            RH_Time_1_Select = businessHoursObject.businesshours_RegularHours_EDF1_Dropdown_Select('08:15')
            ActionChains(self.driver).move_to_element(RH_Time_1_Select).perform()
            RH_Time_1_Select.click()

            businessHoursObject.businesshours_RegularHours_EDF2_Dropdown().click()
            RH_Time_2_Select = businessHoursObject.businesshours_RegularHours_EDF2_Dropdown_Select('17:45')
            ActionChains(self.driver).move_to_element(RH_Time_2_Select).perform()
            RH_Time_2_Select.click()
            sleep(1)
        else:
            print("Already selected")

        businessHoursObject.businessHours_Save().click()  # Save button
        businessHoursObject.businessHours_Back().click()  # Back button



