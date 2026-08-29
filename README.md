# Enterprise AI Document & Risk Management Platform

A production-style full-stack web application for managing **projects, business documents, risks, permissions, and AI-powered document analysis**.

The goal of this project is to build a realistic enterprise application while practicing the software engineering skills required for modern software engineering and technology consulting roles.

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
* View business analytics
* Track important actions through audit history

The final system will combine a traditional business application with an AI/RAG document assistant.

---

## Main Users

The platform will support different user roles:

| Role        | Description                          |
| ----------- | ------------------------------------ |
| **Admin**   | Manages the platform and users       |
| **Manager** | Manages projects and project members |
| **Member**  | Works with project documents         |
| **Viewer**  | Can view permitted information       |

Role-based authorization will control what each user can access and modify.

---

## Architecture

The application will use a layered architecture:

```text
┌─────────────────────────────────┐
│       React + TypeScript        │
│          Material UI            │
└───────────────┬─────────────────┘
                │
                │ REST API / JSON
                ▼
┌─────────────────────────────────┐
│          FastAPI Backend        │
│                                 │
│    API → Services → Repository  │
└───────────────┬─────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│           PostgreSQL            │
│                                 │
│ Users / Projects / Documents    │
│ Risks / Audit Logs              │
└───────────────┬─────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│             AI / RAG            │
│                                 │
│ Extraction → Chunking           │
│ → Embeddings → Vector Search    │
│ → LLM → Answer + Sources        │
└─────────────────────────────────┘
```

The architecture will be built incrementally.

The **MVP will be completed before advanced infrastructure such as microservices, Kubernetes, Terraform, or complex cloud architecture is introduced.**

---

# Technology Stack

## Backend

* Python
* FastAPI
* Pydantic
* SQLAlchemy
* PostgreSQL
* REST API
* JWT authentication
* Role-based authorization
* Pytest

## Frontend

* React
* TypeScript
* Material UI
* REST API integration
* Jest
* React Testing Library

## Engineering

* Git
* GitHub
* Linux / Bash
* Clean Code
* Object-Oriented Programming
* SOLID principles
* Repository Pattern
* Dependency Injection
* Automated testing

## DevOps / Cloud

Planned after the MVP:

* Docker
* Docker Compose
* Redis
* GitHub Actions
* CI/CD
* GCP

## AI

Planned after the core application:

* Document text extraction
* Text cleaning
* Chunking
* Embeddings
* Vector search
* RAG
* LLM integration
* Source references

---

# Database Design

The first version of the relational database contains three main entities:

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

### Relationships

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
Ahmed
  │
  ▼
AI Platform
  │
  └── report.pdf
```

Database migrations will be used to create and update the database consistently.

---

# Backend Structure

The backend will progressively evolve toward the following structure:

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
└── pyproject.toml
```

The repository will be built gradually toward this structure rather than creating every component at once.

---

# REST API

The API will use a versioned prefix:

```text
/api/v1
```

## Authentication

```text
POST /api/v1/auth/register
POST /api/v1/auth/login
POST /api/v1/auth/refresh
```

## Users

```text
GET   /api/v1/users/me
GET   /api/v1/users
PATCH /api/v1/users/{id}
```

## Projects

```text
POST   /api/v1/projects
GET    /api/v1/projects
GET    /api/v1/projects/{id}
PATCH  /api/v1/projects/{id}
DELETE /api/v1/projects/{id}
```

## Documents

```text
POST   /api/v1/projects/{project_id}/documents
GET    /api/v1/projects/{project_id}/documents
GET    /api/v1/documents/{id}
PATCH  /api/v1/documents/{id}
DELETE /api/v1/documents/{id}
```

## Risks

```text
POST   /api/v1/projects/{project_id}/risks
GET    /api/v1/projects/{project_id}/risks
GET    /api/v1/risks/{id}
PATCH  /api/v1/risks/{id}
DELETE /api/v1/risks/{id}
```

These endpoints will be implemented progressively.

---

# Security

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

Secrets must never be stored directly in source code or committed to GitHub.

---

# Document Management

The platform will eventually support:

* PDF
* DOCX
* TXT

Documents will contain metadata such as:

* File name
* Project
* Owner / uploader
* Upload date
* File type
* File size
* Processing status

Planned document operations:

* Upload
* Search
* Filtering
* Pagination
* Metadata viewing
* Document deletion

---

# AI / RAG Pipeline

AI functionality will be implemented **after the core application is working**.

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

Retrieve relevant document chunks

        ↓

Send question + context to the LLM

        ↓

Generate grounded answer

        ↓

Return answer + sources
```

Example response:

```text
Answer:
The refund policy allows ...

Sources:
- policy.pdf
- Page 4
- Section: Refund Policy
```

The goal is for AI answers to include document, page, and section references whenever this information is available.

---

# Testing Strategy

Testing will be part of development rather than something added only at the end.

## Backend

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

## Frontend

Using **Jest + React Testing Library**:

* Login form
* Protected routes
* Project components
* Document list
* Loading states
* Error states
* Important user interactions

Important business logic and API behavior should have automated tests before the project is considered complete.

---

# Git Workflow

The main branch should remain stable.

Feature branches will be used for important changes.

Example:

```bash
git checkout -b feature/database-layer
```

### Commit Convention

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

Before merging:

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

# Development Roadmap

## Phase 1 — Backend Foundation

* [ ] Create PostgreSQL database
* [ ] Create users table
* [ ] Create projects table
* [ ] Create documents table
* [ ] Create foreign-key relationships
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

## Phase 2 — Authentication & Authorization

* [ ] User registration
* [ ] Password hashing
* [ ] Login
* [ ] JWT access tokens
* [ ] Refresh tokens
* [ ] Role-based authorization
* [ ] Project permissions
* [ ] Protected API routes

## Phase 3 — Frontend MVP

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

## Phase 4 — Quality & Engineering

* [ ] Pytest tests
* [ ] Jest tests
* [ ] Error handling
* [ ] Structured logging
* [ ] Clean architecture review
* [ ] SOLID review
* [ ] Repository Pattern
* [ ] Dependency Injection
* [ ] Audit logs
* [ ] Health endpoint

## Phase 5 — DevOps

* [ ] Docker
* [ ] Docker Compose
* [ ] Redis
* [ ] GitHub Actions
* [ ] CI pipeline
* [ ] Production configuration
* [ ] GCP deployment

## Phase 6 — AI / RAG

* [x] PDF text extraction
* [x] DOCX text extraction
* [x] TXT processing
* [x] Chunking
* [x] Embeddings
* [ ] Vector search
* [ ] RAG question answering
* [ ] Source references
* [ ] AI endpoint
* [ ] Optional AI microservice

## Phase 7 — Final Product

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

# Problem-Solving Approach

For important features, the development process will be:

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

The goal is to solve a real business problem instead of simply adding technologies.

---

# Project Principles

### 1. Build the MVP First

The core application must work before advanced technologies are introduced.

### 2. Keep Code Clean

Classes and functions should have clear responsibilities.

### 3. Test Important Features

Important business logic and API behavior should have automated tests.

### 4. Protect User Data

Authentication, authorization, validation, and secure configuration are part of the design.

### 5. Explain Technical Decisions

Important architectural decisions should have a clear reason.

### 6. Use Technology Because It Solves a Problem

Docker, Redis, microservices, cloud, and AI should be introduced when they provide a real benefit.

---

# Skills Demonstrated

| Skill           | Project Evidence                      |
| --------------- | ------------------------------------- |
| Python          | FastAPI backend and services          |
| OOP             | Models, services, and domain logic    |
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
| Linux / Bash    | Development and scripts               |
| Docker          | Containerized application             |
| CI/CD           | GitHub Actions                        |
| Cloud           | GCP deployment                        |
| AI              | RAG document assistant                |
| Problem Solving | Architecture decisions and trade-offs |

---

# Project Status

**Status:** 🚧 In Development

The project is being developed incrementally.

Current development direction:

```text
PostgreSQL
    ↓
Python Backend
    ↓
FastAPI
    ↓
CRUD APIs
    ↓
Authentication
    ↓
React Frontend
    ↓
Testing
    ↓
DevOps
    ↓
RAG / AI
```

Features will only be marked as complete after they have been implemented and tested.

---

# Final Goal

The final application should allow a new developer to:

1. Clone the repository
2. Follow the README
3. Configure the environment
4. Start the application
5. Create an account# Enterprise AI Document & Risk Management Platform

A production-style full-stack web application for managing **projects, business documents, risks, permissions, and AI-powered document analysis**.

The goal of this project is to build a realistic enterprise application while practicing the software engineering skills required for modern software engineering and technology consulting roles.

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

The platform will support different user roles:

| Role        | Description                          |
| ----------- | ------------------------------------ |
| **Admin**   | Manages the platform and users       |
| **Manager** | Manages projects and project members |
| **Member**  | Works with project documents         |
| **Viewer**  | Can view permitted information       |

Role-based authorization will control what each user can access and modify.

---

# Core Architecture

The application will use a layered architecture:

```text
┌─────────────────────────────────┐
│       React + TypeScript        │
│          Material UI            │
└───────────────┬─────────────────┘
                │
                │ REST API / JSON
                ▼
┌─────────────────────────────────┐
│          FastAPI Backend        │
│                                 │
│    API → Services → Repository  │
└───────────────┬─────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│           PostgreSQL            │
│                                 │
│ Users / Projects / Documents    │
│ Risks / Audit Logs              │
└───────────────┬─────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│             AI / RAG            │
│                                 │
│ Extraction → Chunking           │
│ → Embeddings → Vector Search    │
│ → LLM → Answer + Sources        │
└─────────────────────────────────┘
```

The architecture will be built incrementally.

The **MVP will be completed before advanced infrastructure such as microservices, Kubernetes, Terraform, or complex cloud architecture is introduced.**

---

# Technology Stack

## Backend

* Python
* FastAPI
* Pydantic
* SQLAlchemy
* PostgreSQL
* REST API
* JWT authentication
* Role-based authorization
* Pytest

## Frontend

* React
* TypeScript
* Material UI
* REST API integration
* Jest
* React Testing Library

## Engineering

* Git
* GitHub
* Linux / Bash
* Clean Code
* Object-Oriented Programming
* SOLID principles
* Repository Pattern
* Dependency Injection
* Automated testing

## DevOps / Cloud

Planned after the MVP:

* Docker
* Docker Compose
* Redis
* GitHub Actions
* CI/CD
* GCP

## AI

Planned after the core application:

* Document text extraction
* Text cleaning
* Chunking
* Embeddings
* Vector search
* RAG
* LLM integration
* Source references

---

# Database Design

The first version of the application models three main entities:

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

### Relationships

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
Ahmed
  │
  ▼
AI Platform
  │
  └── report.pdf
```

The current implementation starts with Python domain objects. The application will later migrate to PostgreSQL using SQLAlchemy and Alembic.

---

# Backend Structure

The backend will progressively evolve toward the following structure:

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
└── pyproject.toml
```

The repository is being built gradually toward this structure rather than creating every component at once.

---

# REST API

The API will use a versioned prefix:

```text
/api/v1
```

## Authentication

```text
POST /api/v1/auth/register
POST /api/v1/auth/login
POST /api/v1/auth/refresh
```

## Users

```text
GET   /api/v1/users/me
GET   /api/v1/users
PATCH /api/v1/users/{id}
```

## Projects

```text
POST   /api/v1/projects
GET    /api/v1/projects
GET    /api/v1/projects/{id}
PATCH  /api/v1/projects/{id}
DELETE /api/v1/projects/{id}
```

## Documents

```text
POST   /api/v1/projects/{project_id}/documents
GET    /api/v1/projects/{project_id}/documents
GET    /api/v1/documents/{id}
PATCH  /api/v1/documents/{id}
DELETE /api/v1/documents/{id}
```

## Risks

```text
POST   /api/v1/projects/{project_id}/risks
GET    /api/v1/projects/{project_id}/risks
GET    /api/v1/risks/{id}
PATCH  /api/v1/risks/{id}
DELETE /api/v1/risks/{id}
```

These endpoints will be implemented progressively.

---

# Security

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

Secrets must never be stored directly in source code or committed to GitHub.

---

# Document Management

The platform will eventually support:

* PDF
* DOCX
* TXT

Documents will contain metadata such as:

* File name
* Project
* Owner / uploader
* Upload date
* File type
* File size
* Processing status

Planned document operations:

* Upload
* Search
* Filtering
* Pagination
* Metadata viewing
* Document deletion
* Document renaming
* Moving documents between projects

---

# AI / RAG Pipeline

AI functionality will be implemented **after the core application is working**.

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

Retrieve relevant document chunks

        ↓

Send question + context to the LLM

        ↓

Generate grounded answer

        ↓

Return answer + sources
```

Example response:

```text
Answer:
The refund policy allows ...

Sources:
- policy.pdf
- Page 4
- Section: Refund Policy
```

The goal is for AI answers to include document, page, and section references whenever this information is available.

---

# Testing Strategy

Testing will be part of development rather than something added only at the end.

## Current Testing

The current implementation contains basic testing and verification of the domain behavior, including:

* User creation
* Project creation
* Document creation
* User role changes
* Adding documents to projects
* Duplicate document handling
* Document removal
* Safe document removal
* Document renaming
* Moving documents between projects
* Moving a document to the same project
* Document/project relationships

These are currently basic application-level tests and verification. A dedicated automated Pytest test suite will be added later.

## Backend

Using **Pytest**:

* [ ] User registration
* [ ] Login
* [ ] Invalid credentials
* [ ] Project CRUD
* [ ] Document upload validation
* [ ] Authorization rules
* [ ] Risk CRUD
* [ ] AI endpoint behavior
* [ ] Error cases

## Frontend

Using **Jest + React Testing Library**:

* [ ] Login form
* [ ] Protected routes
* [ ] Project components
* [ ] Document list
* [ ] Loading states
* [ ] Error states
* [ ] Important user interactions

Important business logic and API behavior should have automated tests before the project is considered complete.

---

# Git Workflow

Git will be used throughout development.

The main branch should remain stable.

Feature branches will be used for important changes.

Example:

```bash
git checkout -b feature/database-layer
```

### Commit Convention

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

# Development Roadmap

## Phase 1 — Domain Model & Application Foundation

### Application Structure

* [x] Create initial Python application
* [x] Create the main application entry point
* [x] Create the application package structure
* [x] Separate domain classes into dedicated modules
* [x] Define a basic application execution flow

### User Domain

* [x] Create the `User` class
* [x] Define user identity attributes
* [x] Define user role information
* [x] Create users in the application
* [x] Display user information
* [x] Change a user's role
* [x] Validate user role changes

### Project Domain

* [x] Create the `Project` class
* [x] Define project attributes
* [x] Associate a project with an owner
* [x] Create projects in the application
* [x] Display project information
* [x] Associate users with projects
* [x] Validate project ownership

### Document Domain

* [x] Create the `Document` class
* [x] Define document attributes
* [x] Create documents in the application
* [x] Display document information
* [x] Associate documents with projects
* [x] List documents belonging to a project
* [x] Prevent duplicate documents
* [x] Safely remove documents from a project
* [x] Handle removal of a document that does not exist
* [x] Rename documents
* [x] Move documents between projects
* [x] Handle moving a document to its current project
* [x] Validate document/project relationships

### Domain Behavior Testing

* [x] Test user creation
* [x] Test project creation
* [x] Test document creation
* [x] Test user role changes
* [x] Test adding documents to projects
* [x] Test duplicate document handling
* [x] Test document removal
* [x] Test safe document removal
* [x] Test document renaming
* [x] Test moving documents between projects
* [x] Test moving a document to the same project
* [x] Test project/document relationships

---

# Phase 2 — Persistence Layer

## Database Setup

* [ ] Choose PostgreSQL as the production database
* [ ] Create the PostgreSQL database
* [ ] Configure database connection settings
* [ ] Store database configuration in environment variables
* [ ] Create a reusable database connection
* [ ] Configure SQLAlchemy
* [ ] Create SQLAlchemy Base
* [ ] Configure database sessions

## Database Models

* [ ] Create the SQLAlchemy `User` model
* [ ] Create the SQLAlchemy `Project` model
* [ ] Create the SQLAlchemy `Document` model
* [ ] Define primary keys
* [ ] Define required fields
* [ ] Define unique constraints
* [ ] Define foreign keys
* [ ] Define User → Project relationship
* [ ] Define Project → Document relationship
* [ ] Define cascade behavior
* [ ] Add database indexes where useful

## Database Migrations

* [ ] Install Alembic
* [ ] Initialize Alembic
* [ ] Configure Alembic with SQLAlchemy
* [ ] Create the initial migration
* [ ] Create database tables through migrations
* [ ] Apply migrations successfully
* [ ] Test migration rollback
* [ ] Document the migration workflow

---

# Phase 3 — Repository Layer

## User Repository

* [ ] Create the user repository
* [ ] Create a user
* [ ] Find a user by ID
* [ ] Find a user by email
* [ ] List users
* [ ] Update a user
* [ ] Delete a user

## Project Repository

* [ ] Create the project repository
* [ ] Create a project
* [ ] Find a project by ID
* [ ] List projects
* [ ] Update a project
* [ ] Delete a project
* [ ] Find projects owned by a user

## Document Repository

* [ ] Create the document repository
* [ ] Create a document
* [ ] Find a document by ID
* [ ] List project documents
* [ ] Update document metadata
* [ ] Delete a document
* [ ] Search documents by name

---

# Phase 4 — Service Layer

## User Service

* [ ] Create the user service
* [ ] Implement user creation logic
* [ ] Implement user update logic
* [ ] Implement user role management
* [ ] Validate user business rules
* [ ] Handle user-related errors

## Project Service

* [ ] Create the project service
* [ ] Implement project creation
* [ ] Implement project update
* [ ] Implement project deletion
* [ ] Validate project ownership
* [ ] Validate project business rules

## Document Service

* [ ] Create the document service
* [ ] Implement document creation
* [ ] Implement document update
* [ ] Implement document deletion
* [ ] Implement document rename
* [ ] Implement document/project assignment
* [ ] Prevent duplicate documents
* [ ] Validate project ownership
* [ ] Handle document-related errors

---

# Phase 5 — FastAPI REST API

## FastAPI Foundation

* [ ] Create the FastAPI application
* [ ] Configure application settings
* [ ] Create API version `v1`
* [ ] Create API router structure
* [ ] Configure dependency injection
* [ ] Add database session dependency
* [ ] Add API error handling
* [ ] Add health endpoint

## User API

* [ ] Create user schemas
* [ ] Create user routes
* [ ] Implement user creation endpoint
* [ ] Implement user listing endpoint
* [ ] Implement user retrieval endpoint
* [ ] Implement user update endpoint
* [ ] Implement user deletion endpoint

## Project API

* [ ] Create project schemas
* [ ] Create project routes
* [ ] Implement project creation endpoint
* [ ] Implement project listing endpoint
* [ ] Implement project retrieval endpoint
* [ ] Implement project update endpoint
* [ ] Implement project deletion endpoint

## Document API

* [ ] Create document schemas
* [ ] Create document routes
* [ ] Implement document creation endpoint
* [ ] Implement project document listing
* [ ] Implement document retrieval endpoint
* [ ] Implement document update endpoint
* [ ] Implement document deletion endpoint
* [ ] Implement document rename
* [ ] Implement document/project reassignment

---

# Phase 6 — Automated Backend Testing

## Test Infrastructure

* [ ] Configure Pytest
* [ ] Create test configuration
* [ ] Create test database
* [ ] Create test fixtures
* [ ] Configure isolated test data

## API Tests

* [ ] Test user endpoints
* [ ] Test project endpoints
* [ ] Test document endpoints
* [ ] Test validation errors
* [ ] Test not-found errors
* [ ] Test duplicate resources
* [ ] Test invalid relationships
* [ ] Test database behavior

## Business Logic Tests

* [ ] Test user business rules
* [ ] Test project business rules
* [ ] Test document business rules
* [ ] Test document/project relationships
* [ ] Test authorization rules

---

# Phase 7 — Authentication & Authorization

## Authentication

* [ ] Design authentication flow
* [ ] Add password hashing
* [ ] Implement user registration
* [ ] Implement login
* [ ] Implement JWT access tokens
* [ ] Implement refresh tokens
* [ ] Implement token validation
* [ ] Protect authentication secrets

## Authorization

* [ ] Define application roles
* [ ] Implement role-based access control
* [ ] Implement project-level permissions
* [ ] Restrict project access
* [ ] Restrict document access
* [ ] Validate resource ownership
* [ ] Test unauthorized access
* [ ] Test forbidden operations

---

# Phase 8 — Frontend MVP

## Frontend Foundation

* [ ] Create React application
* [ ] Configure TypeScript
* [ ] Configure Material UI
* [ ] Create frontend project structure
* [ ] Configure API client
* [ ] Configure application routing
* [ ] Create reusable UI components

## Authentication UI

* [ ] Create login page
* [ ] Create registration page
* [ ] Implement authentication state
* [ ] Implement protected routes
* [ ] Implement logout

## Project UI

* [ ] Create dashboard
* [ ] Create projects page
* [ ] Create project details page
* [ ] Create project form
* [ ] Implement project CRUD
* [ ] Display project members

## Document UI

* [ ] Create document list
* [ ] Create document details
* [ ] Implement document upload
* [ ] Implement document deletion
* [ ] Implement document rename
* [ ] Implement document search
* [ ] Implement document filtering
* [ ] Implement pagination
* [ ] Add loading states
* [ ] Add error states

---

# Phase 9 — Document Processing

* [ ] Design document storage strategy
* [ ] Implement secure file uploads
* [ ] Validate file types
* [ ] Validate file sizes
* [ ] Generate document metadata
* [ ] Store uploaded files
* [ ] Track document processing status
* [ ] Extract PDF text
* [ ] Extract DOCX text
* [ ] Process TXT files
* [ ] Handle document processing errors

---

# Phase 10 — Risk Management

## Risk Domain

* [ ] Create the `Risk` model
* [ ] Define risk attributes
* [ ] Associate risks with projects
* [ ] Create risks
* [ ] Update risks
* [ ] Delete risks
* [ ] List project risks

## Risk Management

* [ ] Define risk severity
* [ ] Define risk probability
* [ ] Calculate risk level
* [ ] Add risk status
* [ ] Add mitigation information
* [ ] Add risk owner
* [ ] Add risk filtering
* [ ] Add risk search

---

# Phase 11 — Audit & Business Analytics

## Audit Logging

* [ ] Design audit log model
* [ ] Record important user actions
* [ ] Record project changes
* [ ] Record document changes
* [ ] Record permission changes
* [ ] Store timestamps
* [ ] Store the user responsible for each action
* [ ] Create audit history API
* [ ] Create audit history UI

## Analytics

* [ ] Define useful business metrics
* [ ] Count projects
* [ ] Count documents
* [ ] Track document activity
* [ ] Track project activity
* [ ] Track risks
* [ ] Create analytics API
* [ ] Create analytics dashboard

---

# Phase 12 — RAG / AI

## Document Preparation

* [ ] Clean extracted text
* [ ] Split documents into chunks
* [ ] Preserve document metadata
* [ ] Preserve page information
* [ ] Preserve section information

## Embeddings

* [ ] Choose an embedding model
* [ ] Generate document embeddings
* [ ] Store embeddings
* [ ] Choose a vector database
* [ ] Index document chunks

## Retrieval

* [ ] Implement similarity search
* [ ] Retrieve relevant chunks
* [ ] Filter results by project permissions
* [ ] Tune retrieval parameters
* [ ] Evaluate retrieval quality

## Generation

* [ ] Choose an LLM
* [ ] Design the RAG prompt
* [ ] Send question + retrieved context to the LLM
* [ ] Generate grounded answers
* [ ] Return document references
* [ ] Return page references
* [ ] Return section references
* [ ] Handle questions with no relevant information

## AI API

* [ ] Create AI schemas
* [ ] Create AI service
* [ ] Create AI endpoint
* [ ] Connect frontend to AI endpoint
* [ ] Create document Q&A interface
* [ ] Display AI sources
* [ ] Test RAG responses

---

# Phase 13 — DevOps & Production

## Docker

* [ ] Create backend Dockerfile
* [ ] Create frontend Dockerfile
* [ ] Create Docker Compose configuration
* [ ] Containerize PostgreSQL
* [ ] Configure environment variables
* [ ] Test the complete application with Docker

## CI/CD

* [ ] Configure GitHub Actions
* [ ] Run backend tests in CI
* [ ] Run frontend tests in CI
* [ ] Add linting
* [ ] Add formatting checks
* [ ] Add build checks
* [ ] Prevent broken code from being merged

## Production

* [ ] Create production configuration
* [ ] Configure secure secrets
* [ ] Configure logging
* [ ] Configure health checks
* [ ] Configure monitoring
* [ ] Deploy the application
* [ ] Configure GCP infrastructure
* [ ] Document deployment

---

# Phase 14 — Final Quality Review

* [ ] Review architecture
* [ ] Review SOLID principles
* [ ] Review repository pattern
* [ ] Review dependency injection
* [ ] Review database design
* [ ] Review API design
* [ ] Review security
* [ ] Review error handling
* [ ] Review logging
* [ ] Review test coverage
* [ ] Review performance
* [ ] Review documentation
* [ ] Fix technical debt

---

# Phase 15 — Final Product

* [ ] Complete analytics dashboard
* [ ] Complete risk management
* [ ] Complete audit history
* [ ] Complete document management
* [ ] Complete authentication
* [ ] Complete authorization
* [ ] Complete RAG assistant
* [ ] Create architecture diagram
* [ ] Create database ER diagram
* [ ] Complete API documentation
* [ ] Add application screenshots
* [ ] Write deployment documentation
* [ ] Document known limitations
* [ ] Document future improvements
* [ ] Prepare final demo

---

# Problem-Solving Approach

For important features, the development process will be:

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

This process helps keep the project focused on solving real problems instead of simply adding technologies.

---

# Project Principles

## 1. Build the MVP First

The core application must work before advanced technologies are introduced.

## 2. Keep Code Clean

Classes and functions should have clear responsibilities.

## 3. Test Important Features

Important business logic and API behavior should have automated tests.

## 4. Protect User Data

Authentication, authorization, validation, and secure configuration are part of the design.

## 5. Explain Technical Decisions

Important architectural decisions should have a clear reason.

## 6. Use Technology Because It Solves a Problem

Docker, Redis, microservices, cloud, and AI should be introduced when they provide a real benefit.

---

# Skills Demonstrated

| Skill           | Project Evidence                                                |
| --------------- | --------------------------------------------------------------- |
| Python          | Backend and domain logic                                        |
| OOP             | User, Project, and Document domain models                       |
| Clean Code      | Separation of responsibilities                                  |
| Design Patterns | Planned Repository and Dependency Injection                     |
| FastAPI         | Planned REST API                                                |
| REST            | Versioned API endpoints                                         |
| PostgreSQL      | Planned relational database                                     |
| React           | Planned web application                                         |
| TypeScript      | Planned frontend                                                |
| Material UI     | Planned UI components                                           |
| Testing         | Current domain testing + planned Pytest/Jest                    |
| Git             | Version control and feature-based development                   |
| Linux / Bash    | Development environment                                         |
| Docker          | Planned containerization                                        |
| CI/CD           | Planned GitHub Actions pipeline                                 |
| Cloud           | Planned GCP deployment                                          |
| AI              | Planned RAG document assistant                                  |
| Problem Solving | Requirements, architecture, implementation, testing, and review |

---

# Current Project Status

**Status:** 🚧 In Development

The project is currently in the **Domain Model & Application Foundation** stage.

Completed:

```text
User
  ↓
Project
  ↓
Document
  ↓
Relationships
  ↓
Business Operations
  ↓
Validation
  ↓
Basic Testing
```

Next major stage:

```text
PostgreSQL
    ↓
SQLAlchemy
    ↓
Alembic
    ↓
Repository Layer
    ↓
Service Layer
    ↓
FastAPI
    ↓
Automated Tests
    ↓
Authentication
    ↓
React
    ↓
Document Processing
    ↓
Risk Management
    ↓
RAG / AI
    ↓
DevOps
    ↓
Production
```

Features are marked as complete only after they have been implemented and verified.

---

# Final Goal

The final application should allow a new developer to:

1. Clone the repository
2. Follow the README
3. Configure the environment
4. Start the application
5. Create an account
6. Create a project
7. Add project members
8. Upload documents
9. Search documents
10. Manage risks
11. Ask questions about documents
12. Receive AI answers with sources
13. Review project activity
14. View useful business analytics

The project should demonstrate not only the ability to write code, but also the ability to:

* Understand a business problem
* Define requirements
* Design a solution
* Choose appropriate technologies
* Build the system incrementally
* Test the system
* Handle security and permissions
* Explain technical decisions
* Improve the system over time

---

# Author

**Mohamed Chati**

GitHub: [mchati42](https://github.com/mchati42)

---

# License

This project is currently developed as a personal learning and portfolio project.

6. Create a project
7. Upload documents
8. Search documents
9. Manage risks
10. Ask questions about documents
11. Receive AI answers with sources

The project should demonstrate not only the ability to write code, but also the ability to:

* Understand a business problem
* Design a solution
* Build the system
* Test the system
* Explain technical decisions
* Handle security and permissions
* Improve the system over time

---

## Author

**Mohamed Chati**

GitHub: [mchati42](https://github.com/mchati42)

---

## License

This project is currently developed as a personal learning and portfolio project.
