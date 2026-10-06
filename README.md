# 🎓 Smart Campus & Student Career Management System

A full-stack web application designed to help students manage their academic journey, explore career opportunities, and track job applications through a single platform.

## 🚀 Overview

**Smart Campus & Student Career Management System** is a student-focused platform developed using HTML, CSS, JavaScript, Python, and FastAPI.

The platform provides a simple workflow for students to register, log in, manage their profile, explore technical courses, discover career opportunities, apply for jobs, and track their applications.

## ✨ Key Features

### 👤 Student Registration & Login

Students can create an account and log in to access the Smart Campus platform.

### 📊 Student Dashboard

A centralized dashboard provides quick access to profile, courses, career opportunities, and applications.

### 👤 Profile Management

Students can view their educational information, technical skills, and career goals.

### 📚 Course Management

Students can explore courses with:

* Course level
* Duration
* Skills covered
* Course modules
* Learning progress
* Hands-on project information

### 💼 Career Opportunities

Students can explore entry-level opportunities such as:

* Python Developer
* Junior Backend Developer
* Python Full Stack Developer
* Junior Data Analyst

### 🔍 Job Details

Students can view:

* Company
* Location
* Salary
* Employment type
* Experience
* Required skills
* Job description
* Eligibility criteria

### 📝 Job Applications

Students can apply for available opportunities directly through the platform.

The system also prevents duplicate applications for the same job.

### 📋 Application Tracking

Students can view their submitted applications and application status in one place.

## 🛠️ Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* FastAPI
* REST APIs

### Additional Skills

* Django
* SQL
* Git
* GitHub
* Machine Learning
* Deep Learning

## 🏗️ Project Architecture

```text
                Smart Campus Platform
                         |
                         v
              +----------------------+
              |      Frontend        |
              | HTML / CSS / JS      |
              +----------+-----------+
                         |
                         | REST APIs
                         v
              +----------------------+
              |    FastAPI Backend   |
              |       Python         |
              +----------+-----------+
                         |
                         v
                 Application Data
```

## 🔄 Application Workflow

```text
Register
   ↓
Login
   ↓
Student Dashboard
   ├── My Profile
   ├── Courses
   │     └── Course Details
   ├── Career Opportunities
   │     ├── View Job Details
   │     └── Apply Now
   └── My Applications
   ↓
Logout
```

## 📁 Project Structure

```text
Smart-Campus-Student-Career/
│
├── backend/
│   └── main.py
│
├── index.html
├── Login.html
├── register.html
├── studentdashboard.html
├── profile.html
├── courses.html
├── course-details.html
├── career.html
├── applications.html
├── style.css
└── README.md
```

## ⚙️ How to Run

### Step 1 — Clone the Repository

```bash
git clone https://github.com/PrathibhaRoshi/Smart-Campus-Student-Career.git
```

### Step 2 — Open the Project

```bash
cd Smart-Campus-Student-Career
```

### Step 3 — Start FastAPI Backend

Open a terminal inside the `backend` folder:

```bash
cd backend
py -3.13 -m uvicorn main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

### Step 4 — Start Frontend

Open another terminal in the main project folder:

```bash
py -m http.server 5500 --bind 127.0.0.1
```

Frontend:

```text
http://127.0.0.1:5500/
```

## 🧪 Tested Features

* Student Registration
* Login
* Student Dashboard
* Profile
* Course Browsing
* Course Details
* Career Opportunities
* Job Details
* Job Application Submission
* Duplicate Application Prevention
* My Applications
* Logout
* FastAPI REST API integration

## 🎯 Project Objective

The main objective of this project is to provide students with one platform to manage their academic information, develop technical skills, explore career opportunities, and track job applications.

The project also demonstrates practical knowledge of **full-stack web development, Python backend development, FastAPI, REST APIs, frontend development, Git, and GitHub**.

## 🔮 Future Enhancements

* Database integration with SQLite or MySQL
* JWT authentication
* Admin dashboard
* Resume upload
* Job search and filtering
* Email notifications
* AI-powered career recommendations
* Cloud deployment

## 👩‍💻 Developer

### Roshigalla Prathibha

**B.Tech – Computer Science Engineering | 2025 Graduate**

**Skills:**
Python | FastAPI | Django | REST APIs | SQL | HTML | CSS | JavaScript | Git | GitHub | Machine Learning

### Connect with Me

**LinkedIn:**
https://www.linkedin.com/in/roshigalla-prathibha-606569284

**GitHub:**
https://github.com/PrathibhaRoshi

---

⭐ Built as a practical full-stack project to demonstrate software development and problem-solving skills.
