from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.open()
    login_page.login("Admin", "admin123")

    assert dashboard_page.is_loaded()

def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("Admin", "wrongpassword")

    assert login_page.get_error_message() == "Invalid credentials"