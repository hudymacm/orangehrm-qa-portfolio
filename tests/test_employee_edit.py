from pages.employee_management_page import EmployeeManagementPage
from pages.login_page import LoginPage

def test_employee_edit(driver):
    login_page = LoginPage(driver)
    employee_management_page = EmployeeManagementPage(driver)

    login_page.open()
    login_page.login("Admin", "admin123")

    employee_management_page.navigate_to_pim()
    employee_management_page.create_employee("John", "Snow")
    existing_id = employee_management_page.get_employee_id()
    employee_management_page.navigate_to_pim()
    employee_management_page.search_by_employee_id(existing_id)

    employee_management_page.edit_employee("Jane", "Brown")

    assert employee_management_page.get_first_name() == "Jane"
    assert employee_management_page.get_last_name() == "Brown"



