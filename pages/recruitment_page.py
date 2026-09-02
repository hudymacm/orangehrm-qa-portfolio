from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RecruitmentPage:

    RECRUITMENT_BUTTON_LOCATOR = (By.XPATH, "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']")
    SEARCH_CANDIDATE_NAME_FIELD_LOCATOR = (By.XPATH, "//div[normalize-space()='Candidate Name']//input")
    ADD_BUTTON_LOCATOR = (By.XPATH, "//button[contains(., 'Add')]")
    FIRST_NAME_FIELD_LOCATOR = (By.NAME, "firstName")
    LAST_NAME_FIELD_LOCATOR = (By.NAME, "lastName")
    EMAIL_FIELD_LOCATOR = (By.XPATH, "//div[normalize-space()='Email']//input")
    VACANCY_DROPDOWN_LOCATOR = (
        By.XPATH,
        "//label[normalize-space()='Vacancy']"
        "/ancestor::div[contains(@class, 'oxd-input-group')]"
        "//div[contains(@class, 'oxd-select-text')]"
    )
    SAVE_BUTTON_LOCATOR = (By.XPATH, "//button[@type='submit']")
    CANDIDATE_PROFILE_HEADING_LOCATOR = (By.XPATH, "//h6[text()='Candidate Profile']")
    RESUME_FILE_INPUT_LOCATOR = (By.CSS_SELECTOR, "input[type='file']")
    ATTACHMENT_SIZE_EXCEEDED_LOCATOR = (By.XPATH, "//*[normalize-space()='Attachment Size Exceeded']")
    SHORTLIST_BUTTON_LOCATOR = (By.XPATH, "//button[contains(., 'Shortlist')]")
    SCHEDULE_INTERVIEW_BUTTON_LOCATOR = (By.XPATH, "//button[contains(., 'Schedule Interview')]")
    SUCCESS_TOAST_LOCATOR = (By.CSS_SELECTOR, ".oxd-toast--success")
    INTERVIEWER_FIELD_LOCATOR = (By.XPATH, "//div[normalize-space()='Interviewer']//input")
    INTERVIEW_TITLE_FIELD_LOCATOR = (By.XPATH, "//div[normalize-space()='Interview Title']//input")
    INTERVIEW_DATE_FIELD_LOCATOR = (By.CSS_SELECTOR, "input[placeholder='yyyy-dd-mm']")
    MARK_INTERVIEW_PASSED_BUTTON_LOCATOR = (By.XPATH, "//button[contains(., 'Mark Interview Passed')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to_recruitment(self):
        recruitment_button = self.wait.until(
            EC.element_to_be_clickable(self.RECRUITMENT_BUTTON_LOCATOR)
        )
        recruitment_button.click()

        self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_CANDIDATE_NAME_FIELD_LOCATOR)
        )

    def create_candidate(self, first_name, last_name, email, vacancy):
        self.open_add_candidate_form()

        first_name_field = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME_FIELD_LOCATOR)
        )
        first_name_field.send_keys(first_name)

        last_name_field = self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME_FIELD_LOCATOR)
        )
        last_name_field.send_keys(last_name)

        email_field = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_FIELD_LOCATOR)
        )
        email_field.send_keys(email)

        vacancy_dropdown = self.wait.until(
            EC.element_to_be_clickable(self.VACANCY_DROPDOWN_LOCATOR)
        )
        vacancy_dropdown.click()

        option = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//*[normalize-space()='{vacancy}']")
            )
        )
        option.click()

        save_button = self.wait.until(
            EC.element_to_be_clickable(self.SAVE_BUTTON_LOCATOR)
        )
        save_button.click()

        self.wait.until(
            EC.visibility_of_element_located(self.CANDIDATE_PROFILE_HEADING_LOCATOR)
        )

    def is_candidate_profile_displayed(self):
        candidate_profile_heading = self.wait.until(
            EC.visibility_of_element_located(self.CANDIDATE_PROFILE_HEADING_LOCATOR)
        )
        return candidate_profile_heading.is_displayed()

    def open_add_candidate_form(self):
        add_button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_BUTTON_LOCATOR)
        )
        add_button.click()

    def upload_resume(self, file_path):
        file_input = self.wait.until(
            EC.presence_of_element_located(self.RESUME_FILE_INPUT_LOCATOR)
        )
        file_input.send_keys(file_path)

    def is_attachment_size_exceeded_displayed(self):
        message = self.wait.until(
            EC.visibility_of_element_located(self.ATTACHMENT_SIZE_EXCEEDED_LOCATOR)
        )
        return message.is_displayed()

    def shortlist_candidate(self):
        shortlist_button = self.wait.until(
            EC.element_to_be_clickable(self.SHORTLIST_BUTTON_LOCATOR)
        )
        shortlist_button.click()

        save_button = self.wait.until(
            EC.element_to_be_clickable(self.SAVE_BUTTON_LOCATOR)
        )
        save_button.click()

        self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_TOAST_LOCATOR)
        )

        self.wait.until(
            EC.visibility_of_element_located(self.CANDIDATE_PROFILE_HEADING_LOCATOR)
        )

    def is_schedule_interview_button_displayed(self):
        schedule_interview_button = self.wait.until(
            EC.visibility_of_element_located(self.SCHEDULE_INTERVIEW_BUTTON_LOCATOR)
        )
        return schedule_interview_button.is_displayed()

    def schedule_interview(self, interview_title, interviewer, interview_date):
        schedule_interview_button = self.wait.until(
            EC.element_to_be_clickable(self.SCHEDULE_INTERVIEW_BUTTON_LOCATOR)
        )
        schedule_interview_button.click()

        interviewer_field = self.wait.until(
            EC.visibility_of_element_located(self.INTERVIEWER_FIELD_LOCATOR)
        )
        interviewer_field.send_keys(interviewer)
        interviewer_option = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[contains(@class, 'oxd-autocomplete-option') and normalize-space()='{interviewer}']"
                )
            )
        )
        interviewer_option.click()

        interview_title_field = self.wait.until(
            EC.visibility_of_element_located(self.INTERVIEW_TITLE_FIELD_LOCATOR)
        )
        interview_title_field.send_keys(interview_title)

        interview_date_field = self.wait.until(
            EC.element_to_be_clickable(self.INTERVIEW_DATE_FIELD_LOCATOR)
        )
        interview_date_field.click()
        interview_date_field.send_keys(interview_date)

        save_button = self.wait.until(
            EC.element_to_be_clickable(self.SAVE_BUTTON_LOCATOR)
        )
        save_button.click()

        self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_TOAST_LOCATOR)
        )

        self.wait.until(
            EC.visibility_of_element_located(self.CANDIDATE_PROFILE_HEADING_LOCATOR)
        )

    def is_mark_interview_passed_displayed(self):
        mark_interview_passed_button = self.wait.until(
            EC.visibility_of_element_located(self.MARK_INTERVIEW_PASSED_BUTTON_LOCATOR)
        )
        return mark_interview_passed_button.is_displayed()
























