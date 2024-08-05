from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


class BusinessHours:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    settings_button = (By.XPATH, "//lcap-container[@id='menu_container_12']//lcap-menu[@id='menu_45']//button")
    businesshours_button = (By.XPATH, "//lcap-container[@id='menu_container_5']//lcap-menu[@id='menu__ea5dr9lbw']//button")

    businesshours_time_dropdown_click = (By.XPATH, "(//mat-select[@id='form_select_Label'])[1]//div//div//span//span")
    businesshours_time_dropdown_list = (By.XPATH, "//div[@id='form_select_Label-panel']//mat-option")
    businesshours_time_dropdown_select = (By.XPATH, "//div[@id='form_select_Label-panel']//mat-option[contains(@id, '{}')]")

    businesshours_regularhours_dropdown = (By.XPATH, "(//mat-select[@id='form_select_Label'])[2]//div//div//span//span")
    businesshours_regularhours_dropdown_list = (By.XPATH, "//div[@id='form_select_Label-panel']//mat-option")
    businesshours_regularhours_dropdown_select = (
    By.XPATH, "(//div[@id='form_select_Label-panel'])//mat-option[contains(@id, '{}')]")

    businesshours_RH_ED_1_dropdown = (By.XPATH, "(//mat-select[@id='form_select_'])[1]")
    businesshours_RH_ED_2_dropdown = (By.XPATH, "(//mat-select[@id='form_select_'])[2]")
    businesshours_RH_ED_3_dropdown = (By.XPATH, "(//mat-select[@id='form_select_'])[3]")
    businesshours_RH_ED_4_dropdown = (By.XPATH, "(//mat-select[@id='form_select_'])[4]")

    businesshours_RH_ED_1_dropdown_select = (By.XPATH, "(//div[@id='form_select_-panel'])//mat-option[contains(@id, '{}')]")

    # businesshours_plusIcon = (By.XPATH, "(//span[@class='mat-mdc-button-touch-target'])[12]")
    businesshours_plusIcon = (By.XPATH, "//i[@class='far fa-plus']")
    # businesshours_plusIcon = (By.XPATH, "//button[@class='mat-mdc-tooltip-trigger mdc-icon-button mat-mdc-icon-button mat-unthemed mat-mdc-button-base ng-star-inserted']//span[@class='mat-mdc-button-touch-target']")

    businesshours_save = (By.XPATH, "//button[@class='mat-focus-indicator mat-tooltip-trigger mat-badge mat-raised-button mat-button-base mat-accent mat-badge-above mat-badge-after mat-badge-hidden ng-star-inserted']")

    businesshours_save_assert = (By.XPATH, "//simple-snack-bar//div[@class='mat-mdc-snack-bar-label mdc-snackbar__label']")
    businesshours_back = (By.XPATH, "//lcap-container[@id='menu_container_5']//lcap-menu[@id='menu__vk57ywc58']//button")

    def settingsPagebutton(self):
        return self.driver.find_element(*BusinessHours.settings_button)

    def businessHoursOptionbutton(self):
        return self.driver.find_element(*BusinessHours.businesshours_button)

    def businesshours_Time_Dropdown_Click(self):
        return self.driver.find_element(*BusinessHours.businesshours_time_dropdown_click)

    def businesshours_Time_Dropdown_List(self):
        return self.driver.find_elements(*BusinessHours.businesshours_time_dropdown_list)

    def businesshours_Time_Dropdown_Select(self, dropdown_timezone):
        return self.wait.until(EC.presence_of_element_located(
            (By.XPATH, self.businesshours_time_dropdown_select[1].format(dropdown_timezone))))

    def businesshours_RegularHours_Dropdown(self):
        return self.driver.find_element(*BusinessHours.businesshours_regularhours_dropdown)

    def businesshours_RegularHours_Dropdown_List(self):
        return self.driver.find_elements(*BusinessHours.businesshours_regularhours_dropdown_list)

    def businesshours_RegularHours_Dropdown_Select(self, RegularHours_text):
        return self.wait.until(EC.presence_of_element_located(
            (By.XPATH, self.businesshours_regularhours_dropdown_select[1].format(RegularHours_text))))

    # Time set 1
    def businesshours_RegularHours_EDF1_Dropdown(self):
        return self.driver.find_element(*BusinessHours.businesshours_RH_ED_1_dropdown)

    def businesshours_RegularHours_EDF1_Dropdown_Select(self, RH_Time_1):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.businesshours_RH_ED_1_dropdown_select[1].format(RH_Time_1))))

    # Time set 2
    def businesshours_RegularHours_EDF2_Dropdown(self):
        return self.driver.find_element(*BusinessHours.businesshours_RH_ED_2_dropdown)

    def businesshours_RegularHours_EDF2_Dropdown_Select(self, RH_Time_2):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.businesshours_RH_ED_1_dropdown_select[1].format(RH_Time_2))))


    # Time set 3
    def businesshours_RegularHours_EDF3_Dropdown(self):
        return self.driver.find_element(*BusinessHours.businesshours_RH_ED_3_dropdown)

    def businesshours_RegularHours_EDF3_Dropdown_Select(self, RH_Time_3):
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.businesshours_RH_ED_1_dropdown_select[1].format(RH_Time_3))))

    # Time set 4
    def businesshours_RegularHours_EDF4_Dropdown(self):
        return self.driver.find_element(*BusinessHours.businesshours_RH_ED_4_dropdown)

    def businesshours_RegularHours_EDF4_Dropdown_Select(self, RH_Time_4):
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.businesshours_RH_ED_1_dropdown_select[1].format(RH_Time_4))))


    def businessHours_PlusIcon(self):
        return self.driver.find_element(*BusinessHours.businesshours_plusIcon)

    def businessHours_Save(self):
        return self.driver.find_element(*BusinessHours.businesshours_save)

    def businessHours_save_assert(self):
        return self.wait.until(EC.presence_of_element_located(*BusinessHours.businesshours_save_assert))
        #return self.driver.find_element(*BusinessHours.businesshours_save_assert)

    def businessHours_Back(self):
        return self.driver.find_element(*BusinessHours.businesshours_back)
