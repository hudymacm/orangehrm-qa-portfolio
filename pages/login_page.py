from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    USERNAME_FIELD_LOCATOR = (By.NAME, "username")
    PASSWORD_FIELD_LOCATOR = (By.NAME, "password")
    LOGIN_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".orangehrm-login-button")
    ERROR_MESSAGE_LOCATOR = (By.CSS_SELECTOR, ".oxd-alert-content-text")
    PAGE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.driver.get(self.PAGE_URL)

    def login(self, username, password):
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_FIELD_LOCATOR)
        )
        username_field.clear()
        username_field.send_keys(username)

        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_FIELD_LOCATOR)
        )
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON_LOCATOR)
        )
        login_button.click()

    def get_error_message(self):
        error_message = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE_LOCATOR)
        )
        return error_message.text