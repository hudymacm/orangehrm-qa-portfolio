from pages.employee_management_page import EmployeeManagementPage
from pages.login_page import LoginPage

def test_search_employee(driver):
    login_page = LoginPage(driver)
    employee_management_page = EmployeeManagementPage(driver)

    login_page.open()
    login_page.login("Admin", "admin123")

    employee_management_page.navigate_to_pim()
    employee_management_page.create_employee("John", "Striker")

    employee_management_page.navigate_to_pim()
    employee_management_page.search_by_employee_name("John", "Striker")

    assert employee_management_page.get_search_result_first_name() == "John"
    assert employee_management_page.get_search_result_last_name() == "Striker"