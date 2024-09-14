# Sprint Plan for Class Management Project

## **Sprint 1: Project Setup and Basic Models**

### **Goals:**
- Set up the FastAPI project.
- Define basic database models and configuration.
- Implement initial database setup.

### **Tasks:**
1. **Project Initialization**
   - Create a new FastAPI project.
   - Set up the project structure (`models`, `routes`, `config`, `auth`, etc.).

2. **Database Configuration**
   - Set up SQLAlchemy with MySQL.
   - Create a `config/db.py` file for database configuration.

3. **Define Basic Models**
   - Create models for `User`, `Class`, and `Subject`.
   - Implement basic fields and relationships.

4. **Initialize Database**
   - Create a script to generate tables based on the models.
   - Test table creation and ensure the database schema is correct.

5. **Create Initial Migrations**
   - Set up Alembic for database migrations (optional but recommended).

## **Sprint 2: User Roles and Default User Setup**

### **Goals:**
- Implement the user role management system.
- Set up default roles and the default manager user.

### **Tasks:**
1. **Create User Role Model**
   - Implement the `UserRole` model to manage different user roles.

2. **Update User Model**
   - Modify the `User` model to reference the `UserRole` table.

3. **Default Data Insertion**
   - Create a script to insert default roles (`manager`, `principal`, `teacher`, `student`).
   - Insert a default `manager` user with appropriate credentials.

4. **Testing**
   - Verify that default roles and the manager user are correctly inserted into the database.

## **Sprint 3: Authentication and Authorization**

### **Goals:**
- Implement JWT authentication and authorization.
- Set up routes and middleware for user login and role-based access.

### **Tasks:**
1. **JWT Authentication**
   - Implement JWT generation and verification.
   - Create utility functions for encoding and decoding JWTs.

2. **Authentication Middleware**
   - Develop middleware to protect routes and validate JWT tokens.

3. **User Authentication Routes**
   - Implement `sign up` and `login` endpoints.
   - Handle JWT issuance upon successful authentication.

4. **Authorization Checks**
   - Implement role-based access control for different user roles (Manager, Principal, Teacher, Student).

5. **Testing**
   - Ensure that JWT authentication and authorization work as expected.

## **Sprint 4: User Approval Workflow**

### **Goals:**
- Implement user approval workflow based on roles.
- Ensure that only approved users can perform actions based on their role.

### **Tasks:**
1. **Approval Workflow Implementation**
   - Implement logic for user approval:
     - Principal needs approval from the Manager.
     - Teachers need approval from the Principal.
     - Students need approval from both the Teacher and Principal.

2. **Approval Routes**
   - Create endpoints for managers and principals to approve users.

3. **Access Control**
   - Restrict actions based on user approval status.

4. **Testing**
   - Test the approval workflow and ensure users are correctly approved.

## **Sprint 5: Class Management Functionality**

### **Goals:**
- Implement class management features for Principals and Teachers.
- Allow class assignment and status updates.

### **Tasks:**
1. **Class Management Routes**
   - Create endpoints for adding, updating, and deleting classes.
   - Implement class assignment to teachers and status updates.

2. **Subject Management**
   - Create functionality for adding and assigning subjects to classes.

3. **Remark Option**
   - Implement remark options for class activities.

4. **Testing**
   - Verify class management and subject assignment functionality.

## **Sprint 6: Teacher and Student Features**

### **Goals:**
- Implement features for Teachers and Students.
- Allow Teachers to manage class assignments and complaints.
- Allow Students to view their class details.

### **Tasks:**
1. **Teacher Features**
   - Create endpoints for checking assigned classes, updating status, and raising complaints.

2. **Student Features**
   - Create endpoints for viewing class dates, teacher names, and attendance status.

3. **Testing**
   - Test Teacher and Student functionalities to ensure correct operation.

## **Sprint 7: Finalization and Deployment**

### **Goals:**
- Finalize the application.
- Prepare for deployment and handle any remaining issues.

### **Tasks:**
1. **Code Review and Refactoring**
   - Review code for any improvements or refactoring needs.

2. **Documentation**
   - Document API endpoints, authentication methods, and user workflows.

3. **Testing**
   - Conduct comprehensive testing (unit tests, integration tests).

4. **Deployment Preparation**
   - Prepare the application for deployment (e.g., containerization, cloud deployment).

5. **Deployment**
   - Deploy the application to a production environment.

6. **Post-Deployment Testing**
   - Verify that the application is functioning as expected in the production environment.
