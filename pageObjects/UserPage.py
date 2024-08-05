from selenium.webdriver.common.by import By


class UserPage:

    def __init__(self, driver):
        self.driver = driver

    UserPage_button = (By.XPATH, "//lcap-container[@id='menu_container_12']//lcap-menu[@id='menu_48']//button")
    UserPage_rows_per_page = (By.XPATH, "(//mat-select[@id='form_select_'])[2]")
    UserPage_500_options = (By.XPATH, "(//div[@id='form_select_-panel'])/mat-option[4]")
    UserPage_lv_dropdown = (By.XPATH, "(//mat-select[@id='form_select_'])[1]")
    UserPage_lv_options = (By.XPATH, "(//div[@id='form_select_-panel'])/mat-option[{}]")
    # UserPage_lv_options = (By.XPATH, "(//div[@id='form_select_-panel'])//mat-option[@id='{}']]")

    UserPage_search = (By.XPATH, "//input[@id='input_']")
    # UserPage_search_button = (By.XPATH, "//i[@class='far fa-search']")
    UserPage_search_button = (By.XPATH, "(//button[@ng-reflect-disabled='false'])[3]")
    UserPage_count = (By.XPATH, "(//lcap-label[@class='lcap-component'])[2]/div")
    UserPage_chat_table = (By.XPATH, "(//tbody)[1]/tr")
    UserPage_get_user_name_path = (By.XPATH, "(//lcap-dynamic-table[@class='lcap-component'])//*//tr[{}]//td[2]//*//*//lcap-paragraph//div")
    UserPage_get_user_email_path = (By.XPATH, "(//lcap-dynamic-table[@class='lcap-component'])//*//tr[{}]//td[3]//*//*//lcap-container//div")
    UserPage_get_user_phone_path = (By.XPATH, "(//lcap-dynamic-table[@class='lcap-component'])//*//tr[{}]//td[4]//*//*//lcap-container//div")
    UserPage_get_user_stage_path = (By.XPATH, "(//lcap-dynamic-table[@class='lcap-component'])//*//tr[{}]//td[5]//*//*//lcap-paragraph//div")

    def UserPage_Button(self):
        return self.driver.find_element(*UserPage.UserPage_button)

    def UserPage_Rows_Dropdown(self):
        return self.driver.find_element(*UserPage.UserPage_rows_per_page)

    def UserPage_500_Options(self):
        return self.driver.find_element(*UserPage.UserPage_500_options)

    def UserPage_LV_dropdown(self):
        return self.driver.find_element(*UserPage.UserPage_lv_dropdown)

    def UserPage_LV_Options(self, dropdown_filter):
        return self.driver.find_element(By.XPATH, self.UserPage_lv_options[1].format(dropdown_filter))

    # search
    def UserPage_Search_Text(self):
        return self.driver.find_element(*UserPage.UserPage_search)

    def UserPage_Search_Button(self):
        return self.driver.find_element(*UserPage.UserPage_search_button)

    def UserPage_Chat_Count(self):
        return self.driver.find_element(*UserPage.UserPage_count)

    def UserPage_Chat_Table(self):
        return self.driver.find_elements(*UserPage.UserPage_chat_table)

    def UserPage_get_user_name(self, i):
        return self.driver.find_element(By.XPATH, self.UserPage_get_user_name_path[1].format(i)).text

    def UserPage_get_user_email(self, i):
        return self.driver.find_element(By.XPATH, self.UserPage_get_user_email_path[1].format(i)).text

    def UserPage_get_user_phone(self, i):
        return self.driver.find_element(By.XPATH, self.UserPage_get_user_phone_path[1].format(i)).text

    def UserPage_get_user_stage(self, i):
        return self.driver.find_element(By.XPATH, self.UserPage_get_user_stage_path[1].format(i)).text


