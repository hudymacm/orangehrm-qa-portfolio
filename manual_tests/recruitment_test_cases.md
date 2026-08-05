# Recruitment Test Cases

## REC-001

**Title**

Add a candidate.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Recruitment page.

**Test Data**

| Field      | Value             |
|------------|-------------------|
| Full Name  | John Smith        |
| Vacancy    | Software Engineer |
| Email      | jsmith@gmail.com  |

**Steps**

1. Click Add.
2. Enter the test data.
3. Select the consent checkbox.
4. Click Save.
5. Navigate to the Recruitment page.
6. Search for the candidate using the test data.

**Expected Result**

- A new candidate with Full Name 'John Smith' is successfully created.
- A confirmation message 'Successfully Saved' is displayed.
- The candidate profile page is displayed.
- A candidate with Full Name 'John Smith' appears in the search results.

## REC-002

**Title**

Add a candidate using a resume exceeding the file size limit.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Recruitment page.

**Test Data**

| Field      | Value             |
|------------|-------------------|
| Full Name  | John Smith        |
| Vacancy    | Software Engineer |
| Email      | jsmith@gmail.com  |
| Resume     | PDF file larger than the maximum allowed upload size (e.g. 'resume_2mb.pdf') |


**Steps**

1. Click Add.
2. Enter the test data.
3. Upload the resume file.
4. Select the consent checkbox.
5. Click Save.

**Expected Result**

- A new candidate is not created.
- A validation message indicating that the maximum allowed file size has been exceeded is displayed.
- The user remains on the candidate creation page.
- The resume field remains highlighted as invalid.

## REC-003

**Title**

Edit a candidate.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Recruitment page.
- A candidate with Full Name 'John Smith' already exists.

**Test Data**

| Field      | Original Value      | New Value           |
|------------|---------------------|---------------------|
| Full Name  | John Smith          |                     |
| Vacancy    | Software Engineer   |                     |
| Email      | jsmith@gmail.com    | johnsmith@gmail.com |


**Steps**

1. Search for the candidate using the test data.
2. Click the View icon for the candidate.
3. Click Edit.
4. Update the Email field using the test data.
5. Click Save.
6. Navigate to the Recruitment page.
7. Search for the candidate using the test data.

**Expected Result**

- The candidate with Full Name 'John Smith' is successfully updated with a new email address.
- A confirmation message 'Updated Successfully' is displayed.
- The user remains on the candidate profile page.
- The candidate appears in the candidate list with the updated email address.

## REC-004

**Title**

Shortlist a candidate.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Recruitment page.
- A candidate with Full Name 'John Smith' already exists.

**Test Data**

| Field      | Value               |
|------------|---------------------|
| Full Name  | John Smith          |                     
| Vacancy    | Software Engineer   |                     


**Steps**

1. Search for the candidate using the test data.
2. Click the View icon for the candidate.
3. Click Shortlist.
4. Click Save.

**Expected Result**

- The candidate with Full Name 'John Smith' is successfully shortlisted.
- A confirmation message 'Saved Successfully' is displayed.
- The user remains on the candidate profile page.
- The 'Shortlist' button is replaced with the 'Schedule Interview' button on the candidate profile page. 

## REC-005

**Title**

Schedule an interview.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Recruitment page.
- A candidate with Full Name 'John Smith' already exists and is shortlisted.
- An interviewer with Full Name 'Joe Snow' already exists.

**Test Data**

| Field            | Value                     |
|------------------|---------------------------|
| Full Name        | John Smith                |
| Vacancy          | Software Engineer         |
| Interview Title  | Entry Interview           |
| Interviewer      | Joe Snow                  |
| Date             | 2026-08-10                |



**Steps**

1. Search for the candidate using the test data.
2. Click the View icon for the candidate.
3. Click Schedule Interview.
4. Enter the test data.
5. Click Save.
6. Navigate to the Recruitment page.
7. Search for the candidate using the test data.

**Expected Result**

- An interview is successfully scheduled.
- A confirmation message 'Saved Successfully' is displayed.
- The user is redirected to the candidate profile page.
- The 'Schedule Interview' button is replaced with the 'Mark Interview Failed' and 'Mark Interview Passed' buttons.
- The candidate with Full Name 'John Smith' appears in the candidate list with the status updated to 'Interview Scheduled'.

## REC-006

**Title**

Search for a candidate.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Recruitment page.
- A candidate with Full Name 'John Smith' already exists.

**Test Data**

| Field            | Value                     |
|------------------|---------------------------|
| Full Name        | John Smith                |
| Vacancy          | Software Engineer         |

**Steps**

1. Enter the test data.
2. Click Search.

**Expected Result**

- The candidate with Full Name 'John Smith' appears in the search results.
- No candidates that do not match the search criteria are displayed.

## REC-007

**Title**

Delete a candidate.

**Priority**

High

**Preconditions**

- User is logged in as Admin.
- User is on the Recruitment page.
- A candidate with Full Name 'John Smith' already exists.

**Test Data**

| Field            | Value                     |
|------------------|---------------------------|
| Full Name        | John Smith                |
| Vacancy          | Software Engineer         |

**Steps**

1. Search for the candidate using the test data.
2. Click Delete for the matching candidate.
3. Confirm the deletion.
4. Search for a candidate using the test data.

**Expected Result**

- The candidate with Full Name 'John Smith' is successfully deleted.
- A confirmation message 'Successfully Deleted' is displayed.
- The candidate  with Full Name 'John Smith' does not appear in the search results.

