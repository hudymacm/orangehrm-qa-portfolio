from pages.employee_management_page import EmployeeManagementPage
from pages.login_page import LoginPage
from tests.utils import generate_unique_name


def test_employee_deletion(driver):
    unique_name = generate_unique_name()

    login_page = LoginPage(driver)
    employee_management_page = EmployeeManagementPage(driver)

    login_page.open()
    login_page.login("Admin", "admin123")

    employee_management_page.navigate_to_pim()
    employee_management_page.create_employee("Jane", unique_name)
    existing_id = employee_management_page.get_employee_id()

    employee_management_page.navigate_to_pim()
    employee_management_page.search_by_employee_id(existing_id)
    employee_management_page.delete_employee()

    employee_management_page.navigate_to_pim()
    employee_management_page.search_by_employee_name("Jane", unique_name)

    assert employee_management_page.is_no_records_found_displayed()