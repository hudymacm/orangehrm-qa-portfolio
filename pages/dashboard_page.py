from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    DASHBOARD_HEADING_LOCATOR = (By.XPATH, "//h6[text()='Dashboard']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def is_loaded(self):
        dashboard_heading = self.wait.until(
            EC.visibility_of_element_located(
                self.DASHBOARD_HEADING_LOCATOR
            )
        )
        return dashboard_heading.is_displayed()