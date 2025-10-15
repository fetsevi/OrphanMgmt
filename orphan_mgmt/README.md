# Orphan Management System

## 📌 Overview
The Orphan Management System is a backend project built with **Django + Django REST Framework (DRF)**.  
Its purpose is to manage orphan identity, their courses, goals, and track their progress until they achieve their dreams.  

This project is part of my **Backend Development training**.

---

## 🚀 Features
- **Orphans**
  - Create, update, delete, and list orphans
- **Courses**
  - Create, update, delete, and list courses
- **Goals** 
  - Set and track goals for each orphan
- **Enrollments** 
  - Enroll orphans in courses and track progress
- **Authentication** 
  - Register and login for admin/trainers

## 📂 Project Structure

orphan_mgmt/
├── orphan_mgmt/              # Main Django project settings
├── orphans/                  # App handling orphans, courses, goals, enrollments
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── renderers.py
├── templates/
│   └── home.html             # Simple homepage
├── manage.py
├── requirements.txt
└── README.md

## 🔑 API Endpoints

### Orphans
- `GET /api/orphans/` → List all orphans  
- `POST /api/orphans/` → Create new orphan  
- `GET /api/orphans/{id}/` → Get orphan details  
- `PUT /api/orphans/{id}/` → Update orphan  
- `DELETE /api/orphans/{id}/` → Delete orphan  

### Courses
- `GET /api/courses/` → List all courses  
- `POST /api/courses/` → Create new course  
- `GET /api/courses/{id}/` → Get course details  
- `PUT /api/courses/{id}/` → Update course  
- `DELETE /api/courses/{id}/` → Delete course  

### Goals

- `POST /api/orphans/1/goal/` → create goal for orphan 1
- `GET /api/goals/1/` → get goal details
- `PUT /api/goals/1/` → update goal (e.g., mark as achieved)
- `DELETE /api/goals/1/` → delete goal

### Enrollments

- `POST /api/enrollments/` → enroll orphan in a course
- `GET /api/enrollments/` → list all enrollments
- `GET /api/enrollments/1/` → get details of enrollment
- `PUT /api/enrollments/1/` → update progress
- `DELETE /api/enrollments/1/` → remove orphan from course

### Authentication

- `POST /api/auth/register/` → Register User
- `POST /api/auth/login/` → Login and get JWT token
- `POST /api/auth/logout/` → Logout user

### Browsable API Access

- Visit: http://127.0.0.1:8000/ → Homepage
- Visit: http://127.0.0.1:8000/api/orphans/ → API view
- Login via Django Admin: http://127.0.0.1:8000/admin/

### ERD Diagram (Database Design)

Entities:

- Orphan (id, name, age, nationality)
- Course (id, title, description)
- Goal (id, description, status, orphan_id)
- Enrollment (id, orphan_id, course_id, progress)

Relationships:

- One Orphan → Many Goals
- Many Orphans ↔ Many Courses (through Enrollments)

### Future Improvements

- Add a frontend dashboard (React or Django Templates)
- Implement role-based access (Admin / Trainer)
- Generate PDF progress reports
- Deploy API to Render or PythonAnywhere

### Author

👤 Francois Etsevi

- Backend Developer (ALX Africa Trainee)
- Networking Engineer at IPMC Ghana
- Passionate about training orphans to achieve their goals through IT and education

📧 Email: etsevifrancois@gmail.com
🔗 GitHub: https://github.com/fetsevi