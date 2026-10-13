# Agile Project Plan: Student Management System

**Course:** Agile Software Development | **FA2** | B.Tech Final Year IT, PCCOE
**Team:** Rahul Hile (Roll No: ____) and <Student 2 Name> (Roll No: ____)
**Tools:** Python, GitHub, GitHub Actions

## 1. Product Vision
A simple system that lets college staff manage student records and lets students' marks be tracked and analysed.

## 2. User Stories (Product Backlog)

| ID | User Story | Priority | Story Points |
|----|-----------|----------|--------------|
| US1 | As an admin, I want to add a student with roll number, name, department and marks so that the record is stored. | High | 3 |
| US2 | As a teacher, I want to search students by name or department so that I can find records quickly. | High | 3 |
| US3 | As a teacher, I want to update a student's marks so that results stay correct. | High | 3 |
| US4 | As an admin, I want to delete a student record so that outdated data is removed. | Medium | 2 |
| US5 | As a teacher, I want to see the average marks and the topper so that I can analyse performance. | Low | 3 |

## 3. Sprint Planning

**Sprint length:** 1 week | **Team velocity (assumed):** 12 points

### Sprint 1 (Goal: Core student records)
| Story | Tasks | Owner |
|-------|-------|-------|
| US1 | Create Student/StudentManager classes, add_student with validation, unit tests | Student 1 |
| US2 | Implement search and department listing, unit tests | Student 2 |
| US3 | Implement update_marks with marks validation, unit tests | Student 1 |
| CI/CD | Create GitHub Actions workflow (build, test, lint, deploy) | Student 2 |

### Sprint 2 (Goal: Cleanup and analysis)
| Story | Tasks | Owner |
|-------|-------|-------|
| US4 | Implement delete_student, unit tests | Student 2 |
| US5 | Implement average_marks and topper, unit tests | Student 1 |
| Polish | Fix lint issues, improve coverage, update README | Both |

**Sprint ceremonies:** Sprint Planning (day 1), Daily Stand-up (15 min), Sprint Review and Retrospective (last day).

## 4. Definition of Done (DoD)
A story is "Done" only when:
1. Code is written and pushed to GitHub.
2. Unit tests are written and all pass.
3. Test coverage is at least 80%.
4. Code passes the flake8 lint check with no errors.
5. The GitHub Actions pipeline is green (build, test, quality, deploy).
6. Acceptance criteria are verified.
7. README/docs are updated.

## 5. Acceptance Criteria

**US3: Update a student's marks**
- **Given** a student exists, **when** the teacher enters marks between 0 and 100, **then** the student's marks are updated.
- **Given** marks below 0 or above 100, **when** the teacher tries to update, **then** the system rejects the request with an error.
- **Given** a roll number that does not exist, **when** the teacher tries to update, **then** the system reports "Student not found".

**US1: Add a student**
- **Given** a unique roll number, name and department, **when** the admin adds the student, **then** the record is saved.
- **Given** a duplicate roll number or a missing field, **when** the admin adds the student, **then** the system rejects it with an error.

## 6. CI/CD Workflow
`GitHub (push/PR) -> Build -> Automated Testing (pytest) -> Code Quality Check (flake8) -> Deployment`
