h# Enterprise AI Document & Risk Management Platform

A production-style full-stack web application for managing **projects, business documents, risks, permissions, and AI-powered document analysis**.

The goal of this project is to build a realistic enterprise application while practicing the software engineering skills required for modern technology consulting and software engineering roles.

---

## Project Goal

Companies and consulting teams work with large amounts of business documents. These documents can be difficult to organize, search, and analyze manually.

This platform aims to provide one secure application where users can:

* Create and manage projects
* Manage project members and permissions
* Upload business documents
* Search and filter documents
* Track document metadata and activity
* Manage business risks
* Ask questions about company documents
* Receive AI answers with document references
* View useful business analytics
* Track important actions through audit history

The final system will combine a traditional business application with an AI/RAG document assistant.

---

## Main Users

The platform supports different user roles:

* **Admin** — manages the platform and users
* **Manager** — manages projects and project members
* **Member** — works with project documents
* **Viewer** — can view permitted information

Role-based authorization will control what each user can access and modify.

---

## Core Architecture

The application will use a layered architecture:

```text
┌──────────────────────────────┐
│        React + TypeScript    │
│        Material UI           │
└──────────────┬───────────────┘
               │
               │ REST API / JSON
               ▼
┌──────────────────────────────┐
│        FastAPI Backend       │
│                              │
│ API → Services → Repository  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│          PostgreSQL          │
│                              │
│ Users / Projects / Documents │
│ Risks / Audit Logs           │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│          AI / RAG            │
│                              │
│ Extraction → Chunking →      │
│ Embeddings → Vector Search   │
│ → LLM → Answer + Sources     │
└──────────────────────────────┘
```

The architecture is intentionally built in stages. The MVP will be completed before advanced AI, microservices, Kubernetes, Terraform, or other infrastructure is added.

---

## Technology Stack

### Backend

* **Python**
* **FastAPI**
* **Pydantic**
* **SQLAlchemy**
* **PostgreSQL**
* RESTful API
* JWT authentication
* Role-based authorization
* Pytest

### Frontend

* **React**
* **TypeScript**
* **Material UI**
* REST API integration
* Jest
* React Testing Library

### Engineering

* Git
* GitHub
* Linux / Bash
* Clean Code
* Object-Oriented Programming
* SOLID principles
* Repository Pattern
* Dependency Injection
* Automated testing

### DevOps / Cloud

Planned after the MVP:

* Docker
* Docker Compose
* Redis
* GitHub Actions
* CI/CD
* GCP

### AI

Planned after the core application:

* Document text extraction
* Chunking
* Embeddings
* Vector search
* RAG
* LLM integration
* Source references

---

## Current Database Design

The first version of the relational database contains:

```text
users
├── id
├── name
├── email
└── role

projects
├── id
├── name
├── description
└── owner_id → users.id

documents
├── id
├── name
└── project_id → projects.id
```

Relationships:

```text
User
  │
  │ owns
  ▼
Project
  │
  │ contains
  ▼
Document
```

Example:

```text
AHMED
  │
  ▼
AI Platform
  │
  └── report.pdf
```

Database migrations will eventually be used so that the database can be created and updated consistently.

---

## Backend Structure

The target backend structure is:

```text
backend/
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── logging.py
│   │
│   ├── api/
│   │   └── v1/
│   │       ├── auth.py
│   │       ├── users.py
│   │       ├── projects.py
│   │       ├── documents.py
│   │       ├── risks.py
│   │       ├── search.py
│   │       └── ai.py
│   │
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── repositories/
│   └── utils/
│
├── tests/
├── migrations/
├── Dockerfile
└── requirements.txt
```

The current repository is being built gradually toward this structure.

---

## REST API

The planned API will use a versioned prefix such as:

```text
/api/v1
```

### Authentication

```text
POST /api/v1/auth/register
POST /api/v1/auth/login
POST /api/v1/auth/refresh
```

### Users

```text
GET   /api/v1/users/me
GET   /api/v1/users
PATCH /api/v1/users/{id}
```

### Projects

```text
POST   /api/v1/projects
GET    /api/v1/projects
GET    /api/v1/projects/{id}
PATCH  /api/v1/projects/{id}
DELETE /api/v1/projects/{id}
```

### Documents

```text
POST   /api/v1/projects/{project_id}/documents
GET    /api/v1/projects/{project_id}/documents
GET    /api/v1/documents/{id}
PATCH  /api/v1/documents/{id}
DELETE /api/v1/documents/{id}
```

### Risks

```text
POST   /api/v1/projects/{project_id}/risks
GET    /api/v1/projects/{project_id}/risks
GET    /api/v1/risks/{id}
PATCH  /api/v1/risks/{id}
DELETE /api/v1/risks/{id}
```

These endpoints will be implemented progressively.

---

## Security

Security is an important part of the project.

Planned security features include:

* JWT authentication
* Password hashing
* Role-based access control
* Project-level permissions
* Input validation
* Secure file upload validation
* Environment variables for secrets
* Protection against common OWASP risks
* Audit logging for important actions
* No passwords or API keys committed to Git

Secrets will never be stored directly in the source code or committed to GitHub.

---

## Document Management

Users will eventually be able to upload:

* PDF
* DOCX
* TXT

Documents will have metadata such as:

* File name
* Project
* Owner/uploader
* Upload date
* File type
* File size
* Processing status

The application will support:

* Upload
* Search
* Filtering
* Pagination
* Metadata viewing
* Document deletion

---

## AI / RAG Pipeline

The AI functionality will be implemented **after the core application works**.

The planned pipeline is:

```text
Document Upload
      ↓
Text Extraction
      ↓
Text Cleaning
      ↓
Chunking
      ↓
Embeddings
      ↓
Vector Store
      ↓
Similarity Search
      ↓
Relevant Context
      ↓
LLM
      ↓
Answer + Sources
```

Example:

```text
User:

"What is the company's refund policy?"

        ↓

RAG retrieves relevant document chunks

        ↓

LLM receives the question + context

        ↓

Answer:

"The refund policy allows ..."

Sources:
- policy.pdf
- Page 4
- Section: Refund Policy
```

The goal is for AI answers to include document/page/section references when available.

---

## Testing Strategy

Testing will be part of development, not something added only at the end.

### Backend

Using **Pytest**:

* User registration
* Login
* Invalid credentials
* Project CRUD
* Document upload validation
* Authorization rules
* Risk CRUD
* AI endpoint behavior
* Error cases

### Frontend

Using **Jest + React Testing Library**:

* Login form
* Protected routes
* Project components
* Document list
* Loading states
* Error states
* Important user interactions

The project should have automated tests for important functionality before being considered complete.

---

## Git Workflow

Git will be used throughout development.

The main branch should remain stable.

Feature branches will be used for important changes.

Example:

```bash
git checkout -b feature/database-layer
```

Example commit messages:

```text
feat: add database connection
feat: add project API
feat: add document upload
feat: add JWT authentication
test: add project API tests
fix: validate document ownership
refactor: move database logic to repository
docs: update setup guide
```

Before merging changes:

```text
Code
  ↓
Test
  ↓
Review diff
  ↓
Commit
  ↓
Merge
```

---

## Development Roadmap

### Phase 1 — Backend Foundation

* [x] Create PostgreSQL database
* [x] Create users table
* [x] Create projects table
* [x] Create documents table
* [x] Create foreign-key relationships
* [ ] Database connection from Python
* [ ] SQLAlchemy models
* [ ] Database migrations
* [ ] Repository layer
* [ ] Service layer
* [ ] FastAPI application
* [ ] API versioning
* [ ] Users CRUD
* [ ] Projects CRUD
* [ ] Documents CRUD

### Phase 2 — Authentication & Authorization

* [ ] User registration
* [ ] Password hashing
* [ ] Login
* [ ] JWT access tokens
* [ ] Refresh tokens
* [ ] Role-based authorization
* [ ] Project permissions
* [ ] Protected API routes

### Phase 3 — Frontend MVP

* [ ] React + TypeScript setup
* [ ] Material UI
* [ ] Login page
* [ ] Register page
* [ ] Dashboard
* [ ] Projects page
* [ ] Documents page
* [ ] REST API integration
* [ ] Role-based UI
* [ ] Upload documents
* [ ] Search
* [ ] Filtering
* [ ] Pagination

### Phase 4 — Quality & Engineering

* [ ] Pytest tests
* [ ] Jest tests
* [ ] Error handling
* [ ] Structured logging
* [ ] Clean architecture
* [ ] SOLID review
* [ ] Repository Pattern
* [ ] Dependency Injection
* [ ] Audit logs
* [ ] Health endpoint

### Phase 5 — DevOps

* [ ] Docker
* [ ] Docker Compose
* [ ] Redis
* [ ] GitHub Actions
* [ ] CI pipeline
* [ ] Production configuration
* [ ] GCP deployment

### Phase 6 — AI / RAG

* [ ] PDF text extraction
* [ ] DOCX text extraction
* [ ] TXT processing
* [ ] Chunking
* [ ] Embeddings
* [ ] Vector search
* [ ] RAG question answering
* [ ] Source references
* [ ] AI endpoint
* [ ] Optional AI microservice

### Phase 7 — Final Product

* [ ] Analytics dashboard
* [ ] Risk management
* [ ] Audit history
* [ ] Security review
* [ ] Architecture diagram
* [ ] Database ER diagram
* [ ] API documentation
* [ ] Screenshots
* [ ] Deployment documentation
* [ ] Known limitations
* [ ] Future improvements
* [ ] Final demo

---

## Problem-Solving Approach

For important features, I will follow this process:

```text
Problem
   ↓
Scope
   ↓
Requirements
   ↓
Possible Solutions
   ↓
Technical Decision
   ↓
Implementation
   ↓
Testing
   ↓
Review
   ↓
Improvement
```

This helps keep the project focused on solving a real problem instead of simply adding technologies.

---

## Project Principles

### 1. Build the MVP first

The core application must work before adding advanced technologies.

### 2. Keep code clean

Classes and functions should have clear responsibilities.

### 3. Test important features

Important business logic and API behavior should have automated tests.

### 4. Protect user data

Authentication, authorization, validation, and secure configuration are part of the design.

### 5. Explain technical decisions

Important architectural decisions should have a clear reason.

### 6. Use technology because it solves a problem

Docker, Redis, microservices, cloud, and AI should be added when they provide a real benefit.

---

## Skills Demonstrated

This project is designed to demonstrate:

| Skill           | Project Evidence                      |
| --------------- | ------------------------------------- |
| Python          | FastAPI backend and services          |
| OOP             | Models, services and domain logic     |
| Clean Code      | Layered architecture                  |
| Design Patterns | Repository and Dependency Injection   |
| FastAPI         | REST API                              |
| REST            | Versioned API endpoints               |
| PostgreSQL      | Relational database                   |
| React           | Web application                       |
| TypeScript      | Frontend code                         |
| Material UI     | UI components                         |
| Testing         | Pytest + Jest                         |
| Git             | Feature branches and commits          |
| Linux/Bash      | Development and scripts               |
| Docker          | Containerized application             |
| CI/CD           | GitHub Actions                        |
| Cloud           | GCP deployment                        |
| AI              | RAG document assistant                |
| Problem Solving | Architecture decisions and trade-offs |

---

## Project Status

**Status:** 🚧 In Development

The project is being developed incrementally.

The current focus is:

```text
PostgreSQL
    ↓
Python backend
    ↓
FastAPI
    ↓
CRUD APIs
    ↓
Authentication
    ↓
React frontend
    ↓
Testing
    ↓
DevOps
    ↓
RAG / AI
```

Features are marked as complete only after they have been implemented and tested.

---

## Final Goal

The final application should allow a new developer to:

1. Clone the repository
2. Follow the README
3. Configure the environment
4. Start the application
5. Create an account
6. Create a project
7. Upload documents
8. Search documents
9. Manage risks
10. Ask questions about documents
11. Receive AI answers with sources

The project should demonstrate not only that I can write code, but that I can **understand a business problem, design a solution, build it, test it, explain technical decisions, and improve the system over time.**
