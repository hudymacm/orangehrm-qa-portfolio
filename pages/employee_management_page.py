from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class EmployeeManagementPage:

    PIM_BUTTON_LOCATOR = (By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']")
    PIM_HEADING_LOCATOR = (By.XPATH, "//h6[text()='PIM']")
    ADD_BUTTON_LOCATOR = (By.XPATH, "//button[contains(., 'Add')]")
    FIRST_NAME_FIELD_LOCATOR = (By.NAME, "firstName")
    LAST_NAME_FIELD_LOCATOR = (By.NAME, "lastName")
    SAVE_BUTTON_LOCATOR = (By.XPATH, "//button[@type='submit']")
    PERSONAL_DETAILS_HEADING_LOCATOR = (By.XPATH, "//h6[text()='Personal Details']")
    ERROR_MESSAGE_LOCATOR = (By.CSS_SELECTOR,".oxd-input-field-error-message")
    EMPLOYEE_ID_LOCATOR = (By.XPATH, "//label[normalize-space()='Employee Id']/ancestor::div[contains(concat(' ', normalize-space(@class), ' '), ' oxd-input-group ')]//input")
    FORM_LOADER_LOCATOR = (By.CSS_SELECTOR, ".oxd-form-loader")
    SEARCH_BUTTON_LOCATOR = (By.XPATH, "//button[contains(., 'Search')]")
    FIRST_NAME_RESULT_LOCATOR = (By.XPATH,"//div[@role='row' and contains(@class, 'oxd-table-row--clickable')]//div[@role='cell'][3]")
    LAST_NAME_RESULT_LOCATOR = (By.XPATH, "//div[@role='row' and contains(@class, 'oxd-table-row--clickable')]//div[@role='cell'][4]")
    SEARCH_EMPLOYEE_NAME_FIELD_LOCATOR = (By.XPATH, "//div[normalize-space()='Employee Name']//input")
    EDIT_BUTTON_LOCATOR = (By.XPATH, "//button[.//i[contains(@class, 'bi-pencil-fill')]]")
    SUCCESS_TOAST_LOCATOR = (By.CSS_SELECTOR, ".oxd-toast--success")
    PERSONAL_DETAILS_SAVE_BUTTON_LOCATOR = (By.XPATH,"//input[@name='firstName']/ancestor::form//button[@type='submit']")
    DELETE_BUTTON_LOCATOR = (By.XPATH, "//button[.//i[contains(@class, 'bi-trash')]]")
    CONFIRM_DELETION_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'oxd-button--label-danger')]")
    NO_RECORDS_FOUND_LOCATOR = (By.XPATH,"//*[normalize-space()='No Records Found']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to_pim(self):
        pim_button = self.wait.until(
            EC.element_to_be_clickable(
                self.PIM_BUTTON_LOCATOR
            )
        )

        pim_button.click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.EMPLOYEE_ID_LOCATOR
            )
        )

    def create_employee(self, first_name=None, last_name=None, employee_id=None):
        self.open_add_employee_form()
        self.fill_employee_name(first_name, last_name)

        if employee_id is not None:
            self.set_employee_id(employee_id)

        self.click_save()

        self.wait.until(
            EC.visibility_of_element_located(
                self.PERSONAL_DETAILS_HEADING_LOCATOR
            )
        )

    def is_personal_details_page_loaded(self):
        personal_details_heading = self.wait.until(
            EC.visibility_of_element_located(
                self.PERSONAL_DETAILS_HEADING_LOCATOR
            )
        )

        return personal_details_heading.is_displayed()

    def get_filled_field_value(self, locator):
        filled_field = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        self.wait.until(
            lambda _: filled_field.get_attribute("value") != ""
        )

        return filled_field.get_attribute("value")

    def get_first_name(self):
        return self.get_filled_field_value(self.FIRST_NAME_FIELD_LOCATOR)

    def get_last_name(self):
        return self.get_filled_field_value(self.LAST_NAME_FIELD_LOCATOR)

    def get_error_message(self):
        error_message = self.wait.until(
            EC.visibility_of_element_located(
                self.ERROR_MESSAGE_LOCATOR
            )
        )
        return error_message.text

    def get_employee_id(self):
        return self.get_filled_field_value(self.EMPLOYEE_ID_LOCATOR)

    def fill_employee_name(self, first_name=None, last_name=None):
        if first_name is not None:
            first_name_field = self.wait.until(
                EC.visibility_of_element_located(self.FIRST_NAME_FIELD_LOCATOR)
            )

            first_name_field.send_keys(first_name)

        if last_name is not None:
            last_name_field = self.wait.until(
                EC.visibility_of_element_located(self.LAST_NAME_FIELD_LOCATOR)
            )

            last_name_field.send_keys(last_name)

    def set_employee_id(self, employee_id):
        employee_id_field = self.wait.until(
            EC.visibility_of_element_located(self.EMPLOYEE_ID_LOCATOR)
        )

        employee_id_field.send_keys(Keys.CONTROL, "a")
        employee_id_field.send_keys(Keys.BACKSPACE)
        employee_id_field.send_keys(employee_id)

    def open_add_employee_form(self):
        add_button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_BUTTON_LOCATOR)
        )

        add_button.click()

    def search_by_employee_id(self, employee_id):
        employee_id_field = self.wait.until(
            EC.visibility_of_element_located(self.EMPLOYEE_ID_LOCATOR)
        )
        employee_id_field.send_keys(employee_id)

        search_button = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON_LOCATOR)
        )
        search_button.click()

        result_id_locator = (
            By.XPATH,
            f"//*[normalize-space()='{employee_id}']"
        )

        self.wait.until(
            EC.visibility_of_element_located(result_id_locator)
        )

    def search_by_employee_name(self, first_name, last_name):
        full_name = f"{first_name} {last_name}"
        employee_name_field = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_EMPLOYEE_NAME_FIELD_LOCATOR)
        )
        employee_name_field.send_keys(full_name)

        search_button = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON_LOCATOR)
        )
        search_button.click()

    def get_search_result_first_name(self):
        first_name_cell = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME_RESULT_LOCATOR)
        )
        return first_name_cell.text

    def get_search_result_last_name(self):
        last_name_cell = self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME_RESULT_LOCATOR)
        )
        return last_name_cell.text

    def edit_employee(self, new_first_name, new_last_name):
        edit_button = self.wait.until(
            EC.element_to_be_clickable(self.EDIT_BUTTON_LOCATOR)
        )
        edit_button.click()

        self.wait.until(
            EC.visibility_of_element_located(self.PERSONAL_DETAILS_HEADING_LOCATOR)
        )

        self._replace_field_value(self.FIRST_NAME_FIELD_LOCATOR, new_first_name)

        self._replace_field_value(self.LAST_NAME_FIELD_LOCATOR, new_last_name)

        self.click_save()

        self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_TOAST_LOCATOR)
        )
        self.wait.until(
            EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD_LOCATOR, new_first_name)
        )
        self.wait.until(
            EC.text_to_be_present_in_element_value(self.LAST_NAME_FIELD_LOCATOR, new_last_name)
        )

    def _replace_field_value(self, locator, new_value):
        field = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.BACKSPACE)

        self.wait.until(
            lambda _: self.driver.find_element(*locator).get_attribute("value") == ""
        )

        field = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        field.send_keys(new_value)

        self.wait.until(
            lambda _: self.driver.find_element(*locator).get_attribute("value") == new_value
        )

    def delete_employee(self):
        delete_button = self.wait.until(
            EC.visibility_of_element_located(self.DELETE_BUTTON_LOCATOR)
        )
        delete_button.click()

        confirm_deletion_button = self.wait.until(
            EC.visibility_of_element_located(self.CONFIRM_DELETION_BUTTON_LOCATOR)
        )
        confirm_deletion_button.click()

        self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_TOAST_LOCATOR)
        )

    def is_no_records_found_displayed(self):
        message = self.wait.until(
            EC.visibility_of_element_located(self.NO_RECORDS_FOUND_LOCATOR)
        )
        return message.is_displayed()

    def click_save(self):
        save_button = self.wait.until(
            EC.element_to_be_clickable(self.SAVE_BUTTON_LOCATOR)
        )

        # Wait for the form loader to disappear so it doesn't intercept the Save click
        self.wait.until(
            EC.invisibility_of_element_located(
                self.FORM_LOADER_LOCATOR
            )
        )

        save_button.click()





















