from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


class InboxPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    Assigened_to_me = (By.ID, "mat-tab-label-0-0")
    unassigned_ALL = (By.ID, "mat-tab-label-0-2")

    Chat_list = (By.XPATH, "//c-ect-custom-s-c-c-new-chat-listing")
    mark_as_done = (By.XPATH, "//span[normalize-space()='Mark as done']")
    re_open = (By.XPATH, "//span[normalize-space()='Re-open']")
    name_dropdown = (By.XPATH, "//div[@class='mat-select-arrow ng-tns-c112-25']")
    Assigned_Name_select = (By.XPATH, "//div[@id='form_select_-panel']//mat-option[contains(@id, '{}')]")

    name = (By.XPATH, "(//input[@id='input_'])[2]")
    email_id = (By.XPATH, "(//input[@id='input_'])[3]")
    phone_number = (By.XPATH, "(//input[@id='input_'])[4]")
    submit = (By.XPATH, "//button[@class='mat-focus-indicator mat-tooltip-trigger mat-badge lcap-button mat-stroked-button mat-button-base mat-accent mat-badge-above mat-badge-after mat-badge-hidden ng-star-inserted']")

    # User page
    users_button = (By.XPATH, "//lcap-container[@id='menu_container_12']//lcap-menu[@id='menu_48']//button")
    UserPage_search = (By.XPATH, "//input[@id='input_']")
    UserPage_search_button = (By.XPATH, "(//button[@ng-reflect-disabled='false'])[3]")
    UserPage_count = (By.XPATH, "(//lcap-label[@class='lcap-component'])[2]/div")
    UserPage_chat_table = (By.XPATH, "(//tbody)[1]/tr")
    UserPage_get_user_name_path = (By.XPATH, "(//lcap-dynamic-table[@class='lcap-component'])//*//tr[{}]//td[2]//*//*//lcap-paragraph//div")
    UserPage_get_user_email_path = (By.XPATH, "(//lcap-dynamic-table[@class='lcap-component'])//*//tr[{}]//td[3]//*//*//lcap-container//div")
    UserPage_get_user_phone_path = (By.XPATH, "(//lcap-dynamic-table[@class='lcap-component'])//*//tr[{}]//td[4]//*//*//lcap-container//div")



    def InboxPage_Unassigned_ALL(self):
        return self.driver.find_element(*InboxPage.unassigned_ALL)

    def InboxPage_Assigned_to_me(self):
        return self.driver.find_element(*InboxPage.Assigened_to_me)

    def InboxPage_Chat_list(self):
        return self.driver.find_element(*InboxPage.Chat_list)

    def InboxPage_Mark_as_done(self):
        return self.driver.find_element(*InboxPage.mark_as_done)

    def InboxPage_Re_Open(self):
        return self.driver.find_element(*InboxPage.re_open)

    def InboxPage_Name_dropdown(self):
        return self.driver.find_element(*InboxPage.name_dropdown)

    def Assigned_Name_Select(self, name):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.Assigned_Name_select[1].format(name))))

    # Name, email, phone
    def InboxPage_Name(self):
        return self.driver.find_element(*InboxPage.name)

    def InboxPage_Email_ID(self):
        return self.driver.find_element(*InboxPage.email_id)

    def InboxPage_Phone_num(self):
        return self.driver.find_element(*InboxPage.phone_number)

    def InboxPage_Save(self):
        return self.driver.find_element(*InboxPage.submit)

    # User page
    def UserPage_Button(self):
        return self.driver.find_element(*InboxPage.users_button)

    def UserPage_Search_Text(self):
        return self.driver.find_element(*InboxPage.UserPage_search)

    def UserPage_Search_Button(self):
        return self.driver.find_element(*InboxPage.UserPage_search_button)

    def UserPage_Chat_Count(self):
        return self.driver.find_element(*InboxPage.UserPage_count)

    def UserPage_Chat_Table(self):
        return self.driver.find_elements(*InboxPage.UserPage_chat_table)

    def UserPage_get_user_name(self, i):
        return self.driver.find_element(By.XPATH, self.UserPage_get_user_name_path[1].format(i)).text

    def UserPage_get_user_email(self, i):
        return self.driver.find_element(By.XPATH, self.UserPage_get_user_email_path[1].format(i)).text

    def UserPage_get_user_phone(self, i):
        return self.driver.find_element(By.XPATH, self.UserPage_get_user_phone_path[1].format(i)).text