from selenium.webdriver.common.by import By


class LoginPage:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    user_name = "standard_user"
    user_password = "secret_sauce"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_credentials(self):
        self.driver.find_element(*self.USERNAME).send_keys(self.user_name)
        self.driver.find_element(*self.PASSWORD).send_keys(self.user_password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()


