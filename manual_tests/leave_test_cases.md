# Leave Test Cases

## LEV-001

**Title**

Assign leave to an employee with valid dates.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Leave page.
- An employee with Employee Name 'John Smith' already exists.

**Test Data**

| Field         | Value       |
|---------------|-------------|
| Employee Name | John Smith  |
| Leave Type    | Bereavement |
| From Date     | 2026-08-03  |
| To Date       | 2026-08-05  |

**Steps**

1. Click Assign Leave.
2. Enter the test data.
3. Click Assign.
4. Click Leave List.

**Expected Result**

- The leave is successfully assigned to employee 'John Smith'.
- A confirmation message is displayed.
- Employee with Employee Name 'John Smith' appears in the Leave List.

## LEV-002

**Title**

Assign leave without selecting a Leave Type.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Leave page.
- An employee with Employee Name 'John Smith' already exists.

**Test Data**

| Field         | Value       |
|---------------|-------------|
| Employee Name | John Smith  |
| From Date     | 2026-08-03  |
| To Date       | 2026-08-05  |

**Steps**

1. Click Assign Leave.
2. Enter the test data.
3. Leave the Leave Type field empty.
4. Click Assign.

**Expected Result**

- The leave is not assigned.
- A validation message indicating that the Leave Type field is required is displayed.
- The user remains on the Assign Leave page.

## LEV-003

**Title**

Assign leave where the end date is before the start date.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Leave page.
- An employee with Employee Name 'John Smith' already exists.

**Test Data**

| Field         | Value       |
|---------------|-------------|
| Employee Name | John Smith  |
| Leave Type    | Bereavement |
| From Date     | 2026-08-05  |
| To Date       | 2026-08-03  |


**Steps**

1. Click Assign Leave.
2. Enter the test data.
3. Click Assign.

**Expected Result**

- The leave is not assigned.
- A validation message indicating that 'To date' should be after the 'From date' is displayed.
- The user remains on the Assign Leave page.

## LEV-004

**Title**

Assign leave to a non-existent employee.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Leave page.
- An employee with Employee Name 'John Snow' does not exist.

**Test Data**

| Field         | Value       |
|---------------|-------------|
| Employee Name | John Snow   |
| Leave Type    | Bereavement |
| From Date     | 2026-08-03  |
| To Date       | 2026-08-05  |


**Steps**

1. Click Assign Leave.
2. Enter the test data.
3. Click Assign.

**Expected Result**

- No matching employee is suggested.
- A validation message indicating that the Employee Name is invalid is displayed.
- The leave is not assigned.

## LEV-005

**Title**

Search for an existing leave request in the Leave List.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Leave page.
- An employee with Employee Name 'John Smith' has a pending Bereavement leave request from 2026-08-03 to 2026-08-05.

**Test Data**

| Field                       | Value       |
|-----------------------------|-------------|
| Employee Name               | John Smith  |
| Leave Type                  | Bereavement |
| From Date                   | 2026-08-03  |
| To Date                     | 2026-08-05  |
| Show Leave with Status      | Pending     |

**Steps**

1. Click Leave List.
2. Enter the test data.
3. Click Search.

**Expected Result**

- The matching leave request for employee with Employee Name 'John Smith' is displayed.
- The leave type, dates, and status match the search criteria.
- No leave requests that do not match the search criteria are displayed.

## LEV-006

**Title**

Search for a non-existent leave request in the Leave List.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Leave page.
- An employee with Employee Name 'John Smith' does not have a pending Bereavement leave request from 2026-08-03 to 2026-08-05.

**Test Data**

| Field                       | Value       |
|-----------------------------|-------------|
| Employee Name               | John Smith  |
| Leave Type                  | Bereavement |
| From Date                   | 2026-08-03  |
| To Date                     | 2026-08-05  |
| Show Leave with Status      | Pending     |

**Steps**

1. Click Leave List.
2. Enter the test data.
3. Click Search.

**Expected Result**

- No leave requests are displayed.
- A message indicating that no records were found is displayed.

## LEV-007

**Title**

Approve a pending leave request.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Leave page.
- An employee with Employee Name 'John Smith' has a pending Bereavement leave request from 2026-08-03 to 2026-08-05.

**Test Data**

| Field                       | Value       |
|-----------------------------|-------------|
| Employee Name               | John Smith  |
| Leave Type                  | Bereavement |
| From Date                   | 2026-08-03  |
| To Date                     | 2026-08-05  |
| Show Leave with Status      | Pending     |

**Steps**

1. Click Leave List.
2. Enter the test data.
3. Click Search.
4. Click Approve for the matching leave request.

**Expected Result**

- The leave request is successfully approved.
- A message indicating approval was successful is displayed.
- The leave request status is updated to 'Approved'.
- When searching with the status filter set to 'Pending', the leave request is no longer displayed.

## LEV-008

**Title**

Reject a pending leave request.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Leave page.
- An employee with Employee Name 'John Smith' has a pending Bereavement leave request from 2026-08-03 to 2026-08-05.

**Test Data**

| Field                       | Value       |
|-----------------------------|-------------|
| Employee Name               | John Smith  |
| Leave Type                  | Bereavement |
| From Date                   | 2026-08-03  |
| To Date                     | 2026-08-05  |
| Show Leave with Status      | Pending     |

**Steps**

1. Click Leave List.
2. Enter the test data.
3. Click Search.
4. Click Reject for the matching leave request.

**Expected Result**

- The leave request is successfully rejected.
- A message indicating that the leave request was rejected is displayed.
- The leave request status is updated to 'Rejected'.
- When searching with the status filter set to 'Pending', the leave request is no longer displayed.