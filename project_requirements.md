# Project Name: Class Management

## **Overview**
A class management system with user roles: Manager, Principal, Teacher, and Student. It includes features for managing classes, subjects, and user approvals.

## **User Roles and Approval Workflow**

### **Roles**
1. **Manager**
2. **Principal**
3. **Teacher**
4. **Student**

### **Approval Workflow**
- **Principal**: Needs approval from the Manager.
- **Teacher**: Needs approval from the Principal.
- **Student**: No need for approval.

## **Features and Functionality**

### **Principal Activities**
- View all activities of teachers and students.
- Manage class master list and subject master list.
- Assign classes to teachers.
- Reschedule classes, change teacher assignments, and cancel classes.
- Add remarks for each activity.

### **Teacher Activities**
- View assigned classes date-wise.
- Change class activity status (Attained, Not Attained).
- Raise complaints about students’ work tasks, behavior, etc.

### **Student Activities**
- View class details date-wise.
- Check teacher names and class status (attained/absent).

## **Database Schema**

### **Tables**
1. **User Roles**
   - `role_id` (INT, Primary Key)
   - `role_name` (VARCHAR, Unique)

2. **Users**
   - `user_id` (INT, Primary Key)
   - `email` (VARCHAR, Unique)
   - `password` (VARCHAR)
   - `role_id` (INT, Foreign Key)
   - `status` (VARCHAR)
   - `created_at` (TIMESTAMP)
   - `updated_at` (TIMESTAMP)

3. **Classes**
   - `class_id` (INT, Primary Key)
   - `class_name` (VARCHAR)
   - `status` (VARCHAR)
   - `created_at` (TIMESTAMP)
   - `updated_at` (TIMESTAMP)

4. **Subjects**
   - `subject_id` (INT, Primary Key)
   - `subject_name` (VARCHAR)
   - `created_at` (TIMESTAMP)
   - `updated_at` (TIMESTAMP)

5. **Class Assignments**
   - `assignment_id` (INT, Primary Key)
   - `class_id` (INT, Foreign Key)
   - `teacher_id` (INT, Foreign Key)
   - `subject_id` (INT, Foreign Key)
   - `schedule` (DATETIME)
   - `status` (VARCHAR)
   - `remark` (TEXT)

6. **Complaints**
   - `complaint_id` (INT, Primary Key)
   - `teacher_id` (INT, Foreign Key)
   - `student_id` (INT, Foreign Key)
   - `complaint_text` (TEXT)
   - `created_at` (TIMESTAMP)

## **Authentication and Authorization**

- **JWT Authentication**
  - Tokens are generated during login and used for accessing protected routes.
  - Tokens include claims for user roles and approval status.

- **Authorization**
  - Route access is controlled based on user roles and approval status.
