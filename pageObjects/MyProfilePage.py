from selenium.webdriver.common.by import By


class MyProfilePage:

    def __init__(self, driver):
        self.driver = driver

    myprofile_On_Inbox = (By.XPATH, "//lcap-container[@id='menu_container_12']//lcap-menu[@id='menu_46']//button")
    myprofile_email = (By.XPATH, "//input[@id='input_Email']")
    myprofile_nickname = (By.XPATH, "//input[@id='input_Nickname']")
    myprofile_fullname = (By.XPATH, "//input[@id='input_Full name']")
    myprofile_submit = (By.XPATH, "//button[@class='mat-badge mat-mdc-tooltip-trigger mdc-button mdc-button--raised mat-mdc-raised-button mat-accent mat-mdc-button-base mat-badge-above mat-badge-after mat-badge-hidden ng-star-inserted']")

    SCvisitor_chatbot_name = (By.XPATH, "(//lcap-container[@class='lcap-component'])[10]//lcap-title//div")

    def SCVisitor_Chatbot_Name(self):
        return self.driver.find_elements(*MyProfilePage.SCvisitor_chatbot_name)

    def Myprofile_Button_Inbox(self):
        return self.driver.find_element(*MyProfilePage.myprofile_On_Inbox)

    def Myprofile_Email(self):
        return self.driver.find_element(*MyProfilePage.myprofile_email)

    def Myprofile_Nickname(self):
        return self.driver.find_element(*MyProfilePage.myprofile_nickname)

    def Myprofile_Fullname(self):
        return self.driver.find_element(*MyProfilePage.myprofile_fullname)

    def Myprofile_Submit(self):
        return self.driver.find_element(*MyProfilePage.myprofile_submit)
