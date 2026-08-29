from pages.employee_management_page import EmployeeManagementPage
from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
from pathlib import Path

import uuid

pdf_path = Path(__file__).parent.parent / "test_data" / "oversized_test_cv.pdf"


def test_add_candidate(driver):
    login_page = LoginPage(driver)
    recruitment_page = RecruitmentPage(driver)

    login_page.open()
    login_page.login("Admin", "admin123")

    recruitment_page.navigate_to_recruitment()
    recruitment_page.create_candidate("John", "Testcandidate", "john.testcandidate@example.com", "Junior Account Assistant")

    assert recruitment_page.is_candidate_profile_displayed()

def test_add_candidate_oversized_pdf(driver):
    login_page = LoginPage(driver)
    recruitment_page = RecruitmentPage(driver)

    login_page.open()
    login_page.login("Admin", "admin123")

    recruitment_page.navigate_to_recruitment()
    recruitment_page.open_add_candidate_form()
    recruitment_page.upload_resume(str(pdf_path))

    assert recruitment_page.is_attachment_size_exceeded_displayed()

def test_shortlist_candidate(driver):
    #occasionally fails due to demo instability
    login_page = LoginPage(driver)
    recruitment_page = RecruitmentPage(driver)

    login_page.open()
    login_page.login("Admin", "admin123")

    recruitment_page.navigate_to_recruitment()
    recruitment_page.create_candidate("John", "Testcandidate3", "john.testcandidate3@example.com", "Payroll Administrator")
    recruitment_page.shortlist_candidate()

    assert recruitment_page.is_schedule_interview_button_displayed()

def test_schedule_interview(driver):
    unique_name = f"Test{uuid.uuid4().hex[:8]}"

    login_page = LoginPage(driver)
    recruitment_page = RecruitmentPage(driver)
    employee_management_page = EmployeeManagementPage(driver)

    login_page.open()
    login_page.login("Admin", "admin123")

    employee_management_page.navigate_to_pim()
    employee_management_page.create_employee("John", unique_name)

    recruitment_page.navigate_to_recruitment()
    recruitment_page.create_candidate(
        "Jane",
        f"Candidate{unique_name}",
        f"jane.{unique_name.lower()}@example.com",
        "Payroll Administrator"
    )
    recruitment_page.shortlist_candidate()
    interviewer_name = f"John {unique_name}"
    recruitment_page.schedule_interview("Entry Interview", interviewer_name, "2026-01-10")

    assert recruitment_page.is_mark_interview_passed_displayed()
























