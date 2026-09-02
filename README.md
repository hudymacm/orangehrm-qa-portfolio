# OrangeHRM QA Portfolio

## About

A QA portfolio project based on the OrangeHRM public demo application.

The project demonstrates manual testing and UI test automation using
Python, Selenium, pytest, and the Page Object Model.

The test coverage focuses on several OrangeHRM modules and includes
positive and negative test scenarios.

## Technologies

- Python
- Selenium WebDriver
- pytest
- Page Object Model
- Git / GitHub

## Automation Approach

The automated test suite uses the Page Object Model to separate test
scenarios from UI interaction logic.

The tests use:

- Explicit waits for UI synchronization
- Reusable Page Object methods
- Unique test data for the shared demo environment
- pytest fixtures for browser setup and cleanup

## Test Coverage

### Employee Management

Manual and automated tests covering:

- Employee creation
- Required field validation
- Duplicate employee ID validation
- Employee search
- Employee editing
- Employee deletion

### Recruitment

Manual and automated tests covering:

- Candidate creation
- Resume file size validation
- Candidate shortlisting
- Interview scheduling

### Login

Automated tests covering:

- Valid login
- Invalid login

### Leave

Manual test scenarios covering the Leave module.

## Project Structure

    orangehrm-qa-portfolio/
    ├── manual_tests/       # Manual test cases
    ├── pages/              # Page Object classes
    ├── test_data/          # Test files used by automated tests
    ├── tests/              # pytest automated tests
    ├── conftest.py         # pytest fixtures
    ├── requirements.txt    # Python dependencies
    └── README.md

## Running the Automated Tests

1. Clone the repository.

2. Create and activate a virtual environment.

3. Install the dependencies:

       pip install -r requirements.txt

4. Run the test suite:

       pytest

## Test Environment

The automated tests run against the
[OrangeHRM public demo](https://opensource-demo.orangehrmlive.com/).

Because the application is a shared public demo environment, occasional
server-side errors or instability may occur independently of the automated
tests.