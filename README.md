# 💼 JobPortal

### 🚀 A Modern Recruitment & Job Management REST API

> A professional, scalable **Job Portal backend** built with **Django + Django REST Framework**, connecting candidates and employers through a structured recruitment workflow.

<p align="center">
  <a href="https://github.com/waqaralisoomro915-cloud/JobPortal">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-5.x-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/DRF-REST%20API-A30000?style=for-the-badge" alt="DRF">
  <img src="https://img.shields.io/badge/JWT-Authentication-black?style=for-the-badge&logo=jsonwebtokens" alt="JWT">
</p>

---

## 🌟 Overview

**JobPortal** is a backend REST API designed to power a modern recruitment platform.

The system provides separate workflows for:

* 👨‍💼 Employers
* 👨‍💻 Candidates
* 🛡️ Administrators

It focuses on **clean architecture, secure authentication, role-based authorization, relational database design, and real-world recruitment workflows**.

---

# ✨ Core Features

<table>
<tr>
<td width="50%">

### 🔐 Authentication

* JWT Authentication
* Custom User Model
* Role-Based Access Control
* Protected API Endpoints
* Secure Authorization

</td>

<td width="50%">

### 🏢 Company Management

* Company Profiles
* Company Employees
* Ownership Management
* Employer Access Control
* Employee Roles

</td>
</tr>

<tr>
<td>

### 👤 Candidate Management

* Candidate Profiles
* Skills
* Resume
* Professional Links
* Profile Management

</td>

<td>

### 💼 Job Management

* Create Jobs
* Update Jobs
* Delete Jobs
* Required Skills
* Company-Based Jobs

</td>
</tr>

<tr>
<td>

### 📄 Applications

* Apply for Jobs
* Application Tracking
* Employer Review
* Application Status
* Access Control

</td>

<td>

### 📅 Interviews

* Interview Scheduling
* Interview Management
* Candidate Interviews
* Employer Interviews
* Interview Status

</td>
</tr>

<tr>
<td>

### 🔔 Notifications

* Application Updates
* Interview Notifications
* Recruitment Events
* User Notifications

</td>

<td>

### 📚 API Documentation

* OpenAPI Schema
* Swagger UI
* RESTful API
* Structured Endpoints

</td>
</tr>
</table>

---

# 🏗️ Architecture

```text
                         ┌────────────────────┐
                         │      CLIENT        │
                         │   Next.js / Mobile │
                         └─────────┬──────────┘
                                   │
                                   │ REST API
                                   ▼
                    ┌──────────────────────────┐
                    │     Django REST API      │
                    └────────────┬─────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
              ▼                  ▼                  ▼
        ┌───────────┐      ┌───────────┐      ┌───────────┐
        │ Accounts  │      │ Companies │      │ Candidates│
        └───────────┘      └───────────┘      └───────────┘
              │                  │                  │
              └──────────────────┼──────────────────┘
                                 │
                                 ▼
                         ┌──────────────┐
                         │     Jobs     │
                         └──────┬───────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │  Applications   │
                       └────────┬────────┘
                                │
                                ▼
                         ┌────────────┐
                         │ Interviews │
                         └─────┬──────┘
                               │
                               ▼
                        ┌──────────────┐
                        │ Notifications│
                        └──────────────┘
```

---

# 👥 User Roles

### 🛡️ Admin

Platform-level management.

```text
Admin
 ├── Manage Users
 ├── Manage Companies
 ├── Manage Jobs
 ├── Manage Applications
 └── Platform Oversight
```

### 🏢 Employer

Recruitment management.

```text
Employer
 ├── Manage Company
 ├── Manage Employees
 ├── Create Jobs
 ├── Manage Jobs
 ├── Review Applications
 └── Manage Interviews
```

### 👨‍💻 Candidate

Job seeker workflow.

```text
Candidate
 ├── Manage Profile
 ├── Add Skills
 ├── Upload Resume
 ├── Browse Jobs
 ├── Apply for Jobs
 ├── Track Applications
 └── View Interviews
```

---

# 🔄 Recruitment Workflow

```text
┌──────────────┐
│   Candidate  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Create Profile│
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Find a Job  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Apply for Job│
└──────┬───────┘
       │
       ▼
┌──────────────────┐
│ Employer Reviews │
└────────┬─────────┘
         │
         ▼
   ┌─────────────┐
   │  Shortlist  │
   └──────┬──────┘
          │
          ▼
   ┌─────────────┐
   │  Interview  │
   └──────┬──────┘
          │
          ▼
   ┌─────────────┐
   │ Notification │
   └─────────────┘
```

---

# 🛠️ Tech Stack

| Technology                   | Purpose              |
| ---------------------------- | -------------------- |
| 🐍 **Python**                | Backend Language     |
| 🟢 **Django**                | Web Framework        |
| 🔴 **Django REST Framework** | REST API             |
| 🔑 **SimpleJWT**             | Authentication       |
| 🗄️ **SQLite**               | Development Database |
| 📖 **DRF Spectacular**       | OpenAPI / Swagger    |
| 🔀 **Git**                   | Version Control      |
| ☁️ **GitHub**                | Repository           |

---

# 📁 Project Structure

```text
JobPortal/
│
├── apps/
│   │
│   ├── accounts/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── permissions.py
│   │
│   ├── companies/
│   │
│   ├── candidates/
│   │
│   ├── skills/
│   │
│   ├── jobs/
│   │
│   ├── applications/
│   │
│   ├── interviews/
│   │
│   └── notifications/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirement.txt
├── .gitignore
└── README.md
```

---

# 🔗 API Modules

The API is organized around independent resources:

```text
/api/accounts/
/api/companies/
/api/candidates/
/api/skills/
/api/jobs/
/api/applications/
/api/interviews/
/api/notifications/
```

Each module follows the Django REST Framework architecture using:

```text
Model
   ↓
Serializer
   ↓
ViewSet
   ↓
Permission
   ↓
Router
   ↓
REST API
```

---

# 🔐 Permission Architecture

One of the main goals of the project is **proper authorization rather than simply hiding endpoints**.

```text
                    ┌───────────────┐
                    │ Authenticated │
                    │     User      │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  Check Role   │
                    └───────┬───────┘
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
          ADMIN         EMPLOYER       CANDIDATE
             │              │              │
             ▼              ▼              ▼
        Platform       Recruitment      Job Seeking
         Access          Access           Access
```

The system also applies **object-level ownership rules** where required.

---

# ⚙️ Installation

### 1️⃣ Clone

```bash
git clone https://github.com/waqaralisoomro915-cloud/JobPortal.git
cd JobPortal
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### 3️⃣ Activate

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirement.txt
```

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create Admin

```bash
python manage.py createsuperuser
```

### 7️⃣ Start Server

```bash
python manage.py runserver
```

---

# 📖 API Documentation

The project uses **DRF Spectacular** for API documentation.

Once the server is running, access the configured Swagger/OpenAPI endpoints from the project's URL configuration.

Typical configuration:

```text
Schema
/api/schema/

Swagger
/api/docs/
```

---

# 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

Testing areas include:

```text
Authentication
     ↓
Permissions
     ↓
Company Access
     ↓
Candidate Access
     ↓
Job Management
     ↓
Applications
     ↓
Interviews
     ↓
Notifications
```

---

# 🚧 Development Roadmap

### ✅ Completed / In Progress

* [x] Django project setup
* [x] Custom user model
* [x] User roles
* [x] JWT authentication
* [x] Company management
* [x] Company employees
* [x] Candidate profiles
* [x] Skills
* [x] Job management
* [x] Application management
* [ ] Interview module
* [ ] Notification module
* [ ] Automated tests
* [ ] Production deployment

### 🔮 Future

* [ ] Advanced job search
* [ ] Job filtering
* [ ] Job recommendations
* [ ] Email notifications
* [ ] Real-time notifications
* [ ] Celery + Redis
* [ ] Resume parsing
* [ ] AI candidate matching
* [ ] AI job recommendations
* [ ] PostgreSQL
* [ ] Docker
* [ ] CI/CD
* [ ] Cloud deployment

---

# 🎯 Project Goals

This project is being developed with a focus on **industry-level backend engineering practices**.

### Key objectives

```text
Clean Architecture
       +
REST API Design
       +
Database Relationships
       +
Authentication
       +
Authorization
       +
Business Logic
       +
Testing
       +
Documentation
       ↓
Production-Ready Backend
```

---

# 📸 Screenshots

> Screenshots and API documentation previews will be added as the frontend and API documentation are finalized.

```text
Coming Soon 🚀
```

---

# 🔮 Future Frontend

The backend is designed to be consumed by a modern frontend application.

Planned frontend:

```text
Next.js
   │
   ▼
REST API
   │
   ▼
Django REST Framework
   │
   ▼
Database
```

This separation allows the backend and frontend to be developed and deployed independently.

---

# 👨‍💻 Author

## Waqar Ali

**Software Engineer | Django & Python Developer**

Focused on building scalable backend systems, REST APIs, and production-oriented software.

<p>
  <a href="https://github.com/waqaralisoomro915-cloud">
    <img src="https://img.shields.io/badge/GitHub-Waqar%20Ali-181717?style=for-the-badge&logo=github" />
  </a>
</p>

---

# ⭐ Support

If you find this project useful or interesting, consider giving it a ⭐ on GitHub.

---

<div align="center">

### 💼 JobPortal

**Build. Apply. Connect. Get Hired. 🚀**

Made with ❤️ using Django & Django REST Framework

</div>
