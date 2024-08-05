from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


class ChatbotPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    chatbotpage_button = (By.XPATH, "//lcap-container[@id='menu_container_12']//lcap-menu[@id='menu_44']//button")
    newchatbot_button = (By.XPATH, "//lcap-button[@id='button_5']//button")
    enter_chatbot_name = (By.XPATH, "//input[@id='input_New Name']")
    cancel_chatbot_button = (By.XPATH, "//lcap-button[@id='button_6']//button")
    create_chatbot_button = (By.XPATH, "//lcap-button[@id='button_8']//button")

    check_name_existsORnot = (By.XPATH, "//lcap-caption[@id='caption_8']//div")
    character_count = (By.XPATH, "//lcap-caption[@id='caption_7']//div")

    starting_step_buttton = (By.XPATH, "(//div[@class='lcap-chatstep-body'])[1]")

    step_0_field_click = (By.XPATH, "//div[@class='lcap-chatstep-editor-readonly lcap-chatstep-editor-required']")
    step_0_field_input = (By.XPATH, "//div[@class='mat-form-field-infix ng-tns-c109-69']//grammarly-extension[2]//textarea")
    popup_close = (By.XPATH, "//mat-icon[@class='mat-icon notranslate material-icons mat-icon-no-color'][normalize-space()='close']")

    step_1_button = (By.XPATH, "(//div[@class='lcap-chatstep-body'])[2]")
    step_1_field_click = (By.XPATH, )
    step_2_button = (By.XPATH, "(//div[@class='lcap-chatstep-body'])[2]")
    step_2_field = (By.XPATH, )
    step_3_button = (By.XPATH, "(//div[@class='lcap-chatstep-body'])[2]")
    step_3_field = (By.XPATH, )

    end_step_button = (By.XPATH, "(//div[@class='lcap-chatstep-body'])[2]")

    def ChatbotPage_button(self):
        return self.driver.find_element(*ChatbotPage.chatbotpage_button)

    def NewChatbot_button(self):
        return self.driver.find_element(*ChatbotPage.newchatbot_button)

    def Enter_chatbot_name(self):
        return self.driver.find_element(*ChatbotPage.enter_chatbot_name)

    def Cancel_button(self):
        return self.driver.find_element(*ChatbotPage.cancel_chatbot_button)

    def Create_button(self):
        return self.driver.find_element(*ChatbotPage.create_chatbot_button)

    def Character_Count(self):
        # return self.wait.until(EC.presence_of_element_located(*ChatbotPage.character_count))
        return self.driver.find_element(*ChatbotPage.character_count)

    def Check_Name_existsORnot(self):
        return self.driver.find_element(*ChatbotPage.check_name_existsORnot)

        # Steps:------------------------------------------------------------------------------------------------------

    def Popup_close(self):
        return self.driver.find_element(*ChatbotPage.popup_close)

    def Starting_step_button(self):
        return self.driver.find_element(*ChatbotPage.starting_step_buttton)

    def Step_0_field_click(self):
        return self.driver.find_element(*ChatbotPage.step_0_field_click)

    def Step_0_field_Input(self):
        return self.driver.find_element(*ChatbotPage.step_0_field_input)

    def Step_1_button(self):
        return self.driver.find_element(*ChatbotPage.step_1_button)

    def Step_2_button(self):
        return self.driver.find_element(*ChatbotPage.step_2_button)

    def Step_3_button(self):
        return self.driver.find_element(*ChatbotPage.step_3_button)

    def Step_4_button(self):
        return self.driver.find_element(*ChatbotPage.step_4_button)

    def End_step_button(self):
        return self.driver.find_element(*ChatbotPage.end_step_button)

    # Triggers
    triggers_button = (By.XPATH, "//lcap-menu[@id='menu_27']//button")
    add_triggers_dropdown = (By.XPATH, "//mat-select[@role='combobox']")
    current_page_checkbox = (By.XPATH, "//mat-option[@id='option_Current Page URL']")
    time_spent_checkbox = (By.XPATH, "//mat-option[@id='option_Time Spent on URL']")
    total_visits_checkbox = (By.XPATH, "//mat-option[@id='option_Total Visits on URL']")

    current_page_URL_filed_2 = (By.XPATH, "//input[@id='input_']")

    time_Spent_field_1 = (By.XPATH, "(//mat-select[@ng-reflect-placeholder='+ Add Trigger'])")
    time_Spent_field2_dropdown = (By.XPATH, "(//mat-select[@ng-reflect-placeholder='minutes'])")
    time_Spent_field2_option = (By.XPATH, "//mat-option[@id='option_seconds']")

    total_Visits_field1_dropdown = (By.XPATH, "(//mat-select[@ng-reflect-placeholder='more than'])")
    total_Visits_field1_option = (By.XPATH, "//mat-option[@id='option_more than']")
    total_Visits_field_2 = (By.XPATH, "(//input[@id='input_number_'])[2]")
    total_Visits_field_3 = (By.XPATH, "(//input[@id='input_number_'])[3]")
    triggers_publish = (By.XPATH, "//button[@class='mat-focus-indicator mat-tooltip-trigger mat-badge mat-raised-button mat-button-base mat-accent mat-badge-above mat-badge-after mat-badge-hidden ng-star-inserted']")

    # Triggers
    def Triggers_button(self):
        return self.driver.find_element(*ChatbotPage.triggers_button)

    def Add_Triggers_dropdown(self):
        return self.driver.find_element(*ChatbotPage.add_triggers_dropdown)

    def Current_Page_checkbox(self):
        return self.driver.find_element(*ChatbotPage.current_page_checkbox)

    def Time_Spent_checkbox(self):
        return self.driver.find_element(*ChatbotPage.time_spent_checkbox)

    def Total_Visits_checkbox(self):
        return self.driver.find_element(*ChatbotPage.total_visits_checkbox)

    def Current_Page_URL_filed_2(self):
        return self.driver.find_element(*ChatbotPage.current_page_URL_filed_2)

    def Time_Spent_field_1(self):
        return self.driver.find_element(*ChatbotPage.time_Spent_field_1)

    def Time_Spent_field2_dropdown(self):
        return self.driver.find_element(*ChatbotPage.time_Spent_field2_dropdown)

    def Time_Spent_field2_option(self):
        return self.driver.find_element(*ChatbotPage.time_Spent_field2_option)

    def Total_Visits_field1_dropdown(self):
        return self.driver.find_element(*ChatbotPage.total_Visits_field1_dropdown)

    def Total_Visits_field1_option(self):
        return self.driver.find_element(*ChatbotPage.total_Visits_field1_option)

    def Total_Visits_field_2(self):
        return self.driver.find_element(*ChatbotPage.total_Visits_field_2)

    def Total_Visits_field_3(self):
        return self.driver.find_element(*ChatbotPage.total_Visits_field_3)

    def Triggers_publish_button(self):
        return self.driver.find_element(*ChatbotPage.triggers_publish)





    # Schedule
    schedule_button = (By.XPATH, "//lcap-menu[@id='menu_28']//button")
    Stop_Showing = (By.XPATH, "//mat-radio-button[@id='radio_single_select_1_0']")
    Bot_Flow = (By.XPATH, "//mat-radio-button[@id='radio_single_select_3_0']")
    schedule_save = (By.XPATH, "//span[normalize-space()='Save']")

    # Schedule
    def Schedule_button(self):
        return self.driver.find_element(*ChatbotPage.schedule_button)

    def Schedule_Stop_Showing(self):
        return self.driver.find_element(*ChatbotPage.Stop_Showing)

    def Schedule_Bot_Flow(self):
        return self.driver.find_element(*ChatbotPage.Bot_Flow)

    def Schedule_Save(self):
        return self.driver.find_element(*ChatbotPage.schedule_save)







