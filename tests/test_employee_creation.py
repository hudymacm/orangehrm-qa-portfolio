from pages.employee_management_page import EmployeeManagementPage
from pages.login_page import LoginPage

def test_add_employee(driver):
    login_page = LoginPage(driver)
    employee_management_page = EmployeeManagementPage(driver)

    login_page.open()
    login_page.login("Admin", "admin123")
    employee_management_page.navigate_to_pim()
    employee_management_page.create_employee("John", "Smith")

    assert employee_management_page.is_personal_details_page_loaded()
    assert employee_management_page.get_first_name() == "John"
    assert employee_management_page.get_last_name() == "Smith"

def test_add_employee_without_first_name(driver):
    login_page = LoginPage(driver)
    employee_management_page = EmployeeManagementPage(driver)

    login_page.open()
    login_page.login("Admin", "admin123")
    employee_management_page.navigate_to_pim()
    employee_management_page.open_add_employee_form()
    employee_management_page.fill_employee_name(None, "Smith")
    employee_management_page.click_save()

    assert employee_management_page.get_error_message() == "Required"

def test_add_employee_with_duplicate_id(driver):
    login_page = LoginPage(driver)
    employee_management_page = EmployeeManagementPage(driver)

    login_page.open()
    login_page.login("Admin", "admin123")
    employee_management_page.navigate_to_pim()
    employee_management_page.create_employee("John", "Smith")

    existing_id = employee_management_page.get_employee_id()
    employee_management_page.navigate_to_pim()
    employee_management_page.search_by_employee_id(existing_id)
    employee_management_page.open_add_employee_form()
    employee_management_page.fill_employee_name("Jane", "Brown")
    employee_management_page.set_employee_id(existing_id)

    assert employee_management_page.get_error_message() == "Employee Id already exists"
