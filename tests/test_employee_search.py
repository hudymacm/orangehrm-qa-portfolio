from pages.employee_management_page import EmployeeManagementPage
from pages.login_page import LoginPage
from tests.utils import generate_unique_name


def test_search_employee(driver):
    unique_name = generate_unique_name()

    login_page = LoginPage(driver)
    employee_management_page = EmployeeManagementPage(driver)

    login_page.open()
    login_page.login("Admin", "admin123")

    employee_management_page.navigate_to_pim()
    employee_management_page.create_employee("John", unique_name)

    employee_management_page.navigate_to_pim()
    employee_management_page.search_by_employee_name("John", unique_name)

    assert employee_management_page.get_search_result_first_name() == "John"
    assert employee_management_page.get_search_result_last_name() == unique_name