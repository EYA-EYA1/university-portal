# User Stories - MVP

### US-01: Log in
As a user, I want to log in with my email and password
so that I can use the portal.

Acceptance criteria:
- [ ] I can log in with a correct email and password.
- [ ] If the password is wrong, I see the message "Email or password is incorrect".
- [ ] The message does not say which one is wrong (email or password).
- [ ] Passwords are never saved as plain text in the database.
- [ ] If I am not logged in, I cannot open any page except the login page.

### US-02: View my grades
As a student, I want to view my grades
so that I can track my academic performance.

Acceptance criteria:
- [ ] I must be logged in.
- [ ] I see only my own grades.
- [ ] Each grade shows the course name.
- [ ] If I try to open another student's grades, I am refused.
- [ ] If I have no grades yet, I see a message like "No grades yet".

### US-03: Create a course
As an admin, I want to create a course
so that students can be enrolled in it.

Acceptance criteria:
- [ ] I must be logged in as an admin.
- [ ] A course has a name and a code (for example: INF101).
- [ ] I cannot create two courses with the same code.
- [ ] I cannot save a course with an empty name.
- [ ] A student or a teacher cannot open the page to create a course.
### US-04: Create user accounts
As an admin, I want to create teacher and student accounts
so that they can log in to the portal.

Acceptance criteria:
- [ ] I must be logged in as an admin.
- [ ] I choose the role of the new user: student or teacher.
- [ ] I cannot create two accounts with the same email.
- [ ] The password is saved in a protected form, never as plain text.
- [ ] A student or a teacher cannot open the page to create accounts.

### US-05: Enroll a student in a course
As an admin, I want to enroll a student in a course
so that the student is officially registered in it.

Acceptance criteria:
- [ ] I must be logged in as an admin.
- [ ] I choose one student and one course.
- [ ] I cannot enroll the same student in the same course twice.
- [ ] After enrolling, the student sees the course in their list.
- [ ] A student cannot enroll other students.

### US-06: Enter a grade
As a teacher, I want to enter a grade for a student in my course
so that the student can see their result.

Acceptance criteria:
- [ ] I must be logged in as a teacher.
- [ ] I can enter grades only for courses that I teach.
- [ ] I can enter grades only for students enrolled in that course.
- [ ] A grade must be a number between 0 and 20.
- [ ] If I type a letter or a number like 25, I see an error and nothing is saved.
- [ ] A student cannot enter or change a grade.

### US-07: View my courses
As a student, I want to see the list of my courses
so that I know what I am enrolled in.

Acceptance criteria:
- [ ] I must be logged in.
- [ ] I see only the courses I am enrolled in.
- [ ] Each course shows its name and its code.
- [ ] If I am not enrolled in any course, I see a message like "No courses yet".
### US-08: Create a department
As an admin, I want to create a department
so that courses can be organized.

Acceptance criteria:
- [ ] I must be logged in as an admin.
- [ ] A department has a name (for example: Computer Science).
- [ ] I cannot save a department with an empty name.
- [ ] I cannot create two departments with the same name.
- [ ] After saving, the new department appears in the list of departments.
- [ ] A student or a teacher cannot open the page to create a department.