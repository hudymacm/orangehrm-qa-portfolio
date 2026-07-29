# Employee Management Test Cases

## Employee Creation

### EMP-001

**Title**

Add an employee with valid data.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Employee Management page.

**Test Data**

| Field      | Value |
|------------|-------|
| First Name | John  |
| Last Name  | Smith |

**Steps**

1. Click Add.
2. Enter the test data.
3. Click Save.

**Expected Result**

- New employee is created successfully.
- New employee profile is displayed.
- New employee appears in the employee list.

### EMP-002

**Title**

Add an employee without a first name.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Employee Management page.

**Test Data**

| Field     | Value |
|-----------|-------|
| Last Name | Smith |

**Steps**

1. Click Add.
2. Enter the test data.
3. Click Save.

**Expected Result**

- A validation message appears in the First Name field indicating that the First Name field is required.
- New employee is not created.
- The user remains on the Add employee page.

### EMP-003

**Title**

Add an employee with a duplicate Employee ID.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Employee Management page.
- A different employee with Employee ID '0295' already exists.

**Test Data**

| Field       | Value |
|-------------|-------|
| First Name  | John  |
| Last Name   | Smith |
| Employee ID | 0295  |

**Steps**

1. Click Add.
2. Enter the test data.
3. Click Save.

**Expected Result**

- A validation message appears in the Employee ID field indicating that the current Employee ID already exists.
- New employee is not created.
- The user remains on the Add employee page.

## Employee Search

### EMP-004

**Title**

Search for an existing employee.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Employee Management page.
- An employee with Employee Name 'John Smith' already exists.

**Test Data**

| Field         | Value      |
|---------------|------------|
| Employee Name | John Smith |

**Steps**

1. Enter the test data into the search form.
2. Click Search.

**Expected Result**

- Search results are displayed.
- Employee with Employee Name 'John Smith' appears in the results.
- No employees that do not match the search criteria are displayed.

### EMP-005

**Title**

Search for a non-existent employee.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Employee Management page.
- No employee with Employee Name 'John Snow' exists in the system.

**Test Data**

| Field         | Value     |
|---------------|-----------|
| Employee Name | John Snow |

**Steps**

1. Enter the test data into the search form.
2. Click Search.

**Expected Result**

- Search results are displayed.
- Search results contain no entries.
- 'No records found.' message appears.

### EMP-006

**Title**

Search using a partial Employee Name.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Employee Management page.
- An employee with Employee Name 'John Smith' already exists.

**Test Data**

| Field         | Value   |
|---------------|---------|
| Employee Name | John Sm |

**Steps**

1. Enter the test data into the search form.
2. Click Search.

**Expected Result**

- Search results are displayed.
- Employee with Employee Name 'John Smith' appears in the results.
- All displayed employees match the search criteria.

### EMP-007

**Title**

Reset the search filters.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Employee Management page.

**Test Data**

| Field         | Value      |
|---------------|------------|
| Employee Name | John Smith |

**Steps**

1. Enter the test data into the search form.
2. Click Search.
3. Verify that the search results are displayed.
4. Click Reset.

**Expected Result**

- Search filters are removed.
- Search fields are cleared.
- Employee list displays all records.

### EMP-008

**Title**

Search using a valid Employee Name and a non-matching Employee ID.

**Priority**

Medium

**Preconditions**

- User is logged in as Admin.
- User is on the Employee Management page.
- Employee with Employee Name 'John Smith' already exists.
- A different employee with Employee ID '0652' already exists.

**Test Data**

| Field         | Value      |
|---------------|------------|
| Employee Name | John Smith |
| Employee ID   | 0652       |

**Steps**

1. Enter the test data into the search form.
2. Click Search.

**Expected Result**

- Search results are displayed.
- Search results contain no entries.
- 'No records found.' message appears.

## Employee Editing

### EMP-009

**Title**

Edit an existing employee.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Employee Management page.
- Employee with Employee Name 'John Smith' already exists.

**Test Data**

| Field              | Original Value | New Value |
|--------------------|----------------|-----------|
| Employee Name      | John Smith     | John Snow |

**Steps**

1. Search for an employee with Employee Name 'John Smith'.
2. Click Edit.
3. Update the employee using the test data.
4. Click Save.
5. Return to the Employee Management Page
6. Search for employee 'John Snow'.

**Expected Result**

- A confirmation message 'Update successful' appears.
- Employee profile displays updated Employee Full Name 'John Snow'.
- The changes are saved successfully.

### EMP-010

**Title**

Edit an employee using a duplicate Employee ID.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Employee Management page.
- Employee with Employee Name 'John Smith' and Employee ID '1234' already exists.
- A different employee with Employee ID '0295' already exists.

**Test Data**

| Field              | Original Value | New Value |
|--------------------|----------------|-----------|
| Employee ID        | 1234           | 0295      |

**Steps**

1. Search for an employee with Employee Name 'John Smith'.
2. Click Edit.
3. Update the Employee ID using the test data.
4. Click Save.

**Expected Result**

- Validation message indicating Employee ID already exists appears in the Employee ID field.
- Employee ID is not updated.
- Changes are not saved.

## Employee Deletion

### EMP-011

**Title**

Delete an existing employee.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Employee Management page.
- Employee with Employee Name 'John Smith' already exists.

**Test Data**

| Field              | Value          |
|--------------------|----------------|
| Employee Name      | John Smith     |

**Steps**

1. Search for an employee with Employee Name 'John Smith'.
2. Click Delete.
3. Confirm the deletion.
4. Search for an employee with Employee Name 'John Smith'.

**Expected Result**

- Employee is successfully deleted.
- A confirmation message 'Deleted Successfully' appears.
- Employee with Employee Name 'John Smith' does not appear in the employee list.

### EMP-012

**Title**

Cancel the deletion of an employee.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Employee Management page.
- Employee with Employee Name 'John Smith' already exists.

**Test Data**

| Field              | Value          |
|--------------------|----------------|
| Employee Name      | John Smith     |

**Steps**

1. Search for an employee with Employee Name 'John Smith'.
2. Click Delete.
3. Click Cancel.

**Expected Result**

- The deletion confirmation dialog is closed.
- Employee is not deleted.
- Employee with Employee Name 'John Smith' remains in the employee list.