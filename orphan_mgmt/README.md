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
- **Goals** (coming soon)
  - Set and track goals for each orphan
- **Enrollments** (coming soon)
  - Enroll orphans in courses and track progress
- **Authentication** (optional, future)
  - Register and login for admin/trainers

## 📂 Project Structure

orphan_mgmt/
├── orphan_mgmt/ # Main Django project
├── orphans/ # App handling orphans, courses, goals, enrollments
│ ├── models.py # Database models
│ ├── serializers.py # Convert models <-> JSON
│ ├── views.py # API endpoints logic
│ ├── urls.py # App routes
│ └── ...

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