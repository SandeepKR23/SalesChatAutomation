from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    emailid = (By.ID, "input_Email")
    password = (By.ID, "input_Password")
    submit = (By.XPATH, "//lcap-button[@id='createPW_button']//button")

    def loginPageUsername(self):
        return self.driver.find_element(*LoginPage.emailid)    #classname.var

    def loginPagePassword(self):
        return self.driver.find_element(*LoginPage.password)

    def loginPageSubmit(self):
        return self.driver.find_element(*LoginPage.submit)
