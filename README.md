#   EMPLOYEE MANAGEMENT SYSTEM - Backend

## A Backend Application built with **Django, Django REST Framework, and PostgreSQL.

It provided a structured way to handle employee data, departmental hierarchy and other company related tasks.



##  Tech Stack
- Backend Framework: Django 5 + Django REST Framework
- Database: PostgreSQL 14(Docker container)
- Cache / Message Broker: Redis 7 (Docker container)
- Background Jobs: Celery (using Redis broker)
- Containerization: Docker + Docker Compose

## 🛠 Local Development Setup

### 1. Clone the repo

```bash
 

git clone https://github.com/YOUR_USERNAME/employee-management-Backend.git
cd employee-management-Backend
```
---

### 2. Environment setup


All services run in containers (Django, Postgres, Redis, Celery).

```
docker-compose up --build
```

This will start:

web → Django (http://localhost:8000)


Then apply migrations:
```bash
docker exec -it employee-management-backend-web-1 python manage.py migrate
```


Create superuser:

```bash
docker exec -it employee-management-backend-web-1 python manage.py createsuperuser
```

```bash
docker exec -it employee-management-backend-web-1 pip freeze 
```
---
### API TEST


[System design document](Documentation/SDD.md)
