# Development of a Modular Task Management System Based on Software Engineering Components

A modular web-based Task Management System developed as a Software Engineering Components project.

The application allows users to register and log in, create and manage tasks, update task statuses, delete tasks, and receive notifications about upcoming tasks.

---

## 1. Project Overview

The project demonstrates the practical use of component-based software engineering principles in a web application.

The system is divided into independent components with clearly defined responsibilities:

- **User Component** – User registration and login
- **Task Component** – Task creation and management
- **Notification Component** – Upcoming task notifications
- **Database Component** – SQLite database operations
- **REST API** – Communication between frontend and backend
- **Frontend UI** – User interface and interaction

### Main Architecture

```text
User
  │
  ▼
React Frontend
  │
  │ HTTP / REST API
  ▼
Flask Backend
  │
  ├── User Component
  ├── Task Component
  ├── Notification Component
  │
  ▼
Database Component
  │
  ▼
SQLite Database
```

---

# 2. Technologies

## Frontend

- React
- Vite
- JavaScript
- HTML
- CSS

## Backend

- Python
- Flask
- Flask-CORS

## Database

- SQLite

## Testing

- PyTest
- Postman

---

# 3. Project Structure

```text
TaskManagementSystem
│
├── backend
│   │
│   ├── components
│   │   ├── user
│   │   │   └── user_service.py
│   │   │
│   │   ├── task
│   │   │   └── task_service.py
│   │   │
│   │   └── notification
│   │       └── notification_service.py
│   │
│   ├── database
│   │   └── database.py
│   │
│   ├── routes
│   │   ├── user_routes.py
│   │   ├── task_routes.py
│   │   └── notification_routes.py
│   │
│   ├── tests
│   │   ├── test_user_service.py
│   │   ├── test_task_service.py
│   │   ├── test_api_integration.py
│   │   └── test_white_box.py
│   │
│   ├── venv
│   └── app.py
│
└── frontend
    ├── src
    ├── public
    ├── package.json
    └── ...
```

---

# 4. Requirements

Before running the project, make sure the following software is installed:

- Python
- Node.js
- npm
- Git

You can verify the installations with:

```bash
python --version
node --version
npm --version
```

---

# 5. Backend Setup

The backend is developed using Python and Flask.

Open a terminal and navigate to the backend directory:

```bash
cd backend
```

## 5.1. Create a Virtual Environment

If a virtual environment does not already exist:

```bash
python -m venv venv
```

## 5.2. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

After activation, the terminal should show something similar to:

```text
(venv)
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

# 6. Install Backend Dependencies

Install the required Python packages:

```bash
pip install flask flask-cors pytest
```

If the project contains a `requirements.txt` file, the dependencies can instead be installed with:

```bash
pip install -r requirements.txt
```

---

# 7. Start the Backend

Make sure the terminal is inside the `backend` directory and the virtual environment is activated.

Run:

```bash
python app.py
```

The Flask server will start locally.

The default backend address is:

```text
http://127.0.0.1:5000
```

You can also open the root endpoint in a browser:

```text
http://127.0.0.1:5000/
```

The API should return:

```json
{
  "message": "Task Management System API is running"
}
```

---

# 8. Database

The project uses SQLite.

The database is initialized automatically when the Flask application starts.

The database contains two main tables:

## Users

```text
users
├── id
├── username
└── password
```

## Tasks

```text
tasks
├── id
├── user_id
├── title
├── description
├── due_date
├── status
└── created_at
```

The `user_id` field connects each task to its corresponding user.

No manual database creation is required.

---

# 9. Frontend Setup

Open another terminal.

Navigate to the frontend directory:

```bash
cd frontend
```

Install the JavaScript dependencies:

```bash
npm install
```

Start the Vite development server:

```bash
npm run dev
```

Vite will provide a local development address, normally similar to:

```text
http://localhost:5173
```

Open the displayed address in your browser.

---

# 10. Running the Complete Application

Two terminals should be used.

### Terminal 1 – Backend

```bash
cd backend
venv\Scripts\activate
python app.py
```

### Terminal 2 – Frontend

```bash
cd frontend
npm install
npm run dev
```

The application works as follows:

```text
Browser
   │
   ▼
React Frontend
   │
   │ HTTP Requests
   ▼
Flask REST API
   │
   ▼
Backend Components
   │
   ▼
SQLite Database
```

The backend must be running while using the frontend because the frontend communicates with the Flask REST API.

---

# 11. How the Application Works

## 11.1. Registration

A new user enters a username and password.

The frontend sends a request to:

```text
POST /api/users/register
```

The User Component checks the information and stores the new user in the SQLite database.

---

## 11.2. Login

The user enters their username and password.

The frontend sends:

```text
POST /api/users/login
```

The backend checks the credentials.

If the credentials are correct, the backend returns the user information.

The frontend stores the basic logged-in user information in `localStorage`.

This allows the application to restore the user interface after a browser refresh.

---

# 12. Task Management

After logging in, the user can manage their tasks.

The available operations are:

- Create a task
- View tasks
- Edit a task
- Complete a task
- Delete a task

Each task contains:

```text
Title
Description
Due Date
Status
Creation Date
```

A task normally starts with:

```text
Pending
```

When completed, its status becomes:

```text
Completed
```

---

# 13. Notifications

The Notification Component checks pending tasks with approaching due dates.

The system considers pending tasks whose due dates are within the next three days.

The notification endpoint is:

```text
GET /api/notifications/{user_id}
```

If upcoming tasks exist, the API returns their information.

If there are no upcoming tasks, the system returns a message indicating that there are no upcoming tasks.

---

# 14. REST API Endpoints

| Method | Endpoint                         | Description         |
| ------ | -------------------------------- | ------------------- |
| POST   | `/api/users/register`            | Register a new user |
| POST   | `/api/users/login`               | Login               |
| POST   | `/api/tasks/{user_id}`           | Create a task       |
| GET    | `/api/tasks/{user_id}`           | Get all user tasks  |
| GET    | `/api/tasks/{user_id}/{task_id}` | Get a specific task |
| PUT    | `/api/tasks/{user_id}/{task_id}` | Update a task       |
| DELETE | `/api/tasks/{user_id}/{task_id}` | Delete a task       |
| GET    | `/api/notifications/{user_id}`   | Get notifications   |

---

# 15. Testing

The project includes automated tests using PyTest.

Navigate to the backend directory:

```bash
cd backend
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Run all tests:

```bash
python -m pytest tests -v
```

The final test execution produced:

```text
17 passed in 0.37s
```

The test suite includes:

- Unit tests
- Integration tests
- White box tests

Black box API testing was performed separately using Postman.

---

# 16. Testing Structure

The project uses several testing approaches.

## Unit Testing

Individual service functions are tested independently.

Examples include:

- User registration
- User login
- Task creation
- Task retrieval
- Task update
- Task deletion

## Integration Testing

Integration tests verify communication between:

```text
API
 ↓
Service
 ↓
Database
```

Examples include:

- Register → Login
- Create Task → Retrieve Task
- Update Task → Retrieve → Delete
- Notification API

## Black Box Testing

Postman is used to test the API from an external client's perspective.

Test cases include:

- Successful registration
- Missing username
- Successful login
- Incorrect password
- Invalid task title

## White Box Testing

White box tests examine selected internal conditions and branches of the backend services.

---

# 17. Postman

Postman can be used to manually test the REST API.

First start the backend:

```bash
python app.py
```

Then create requests using the API endpoints described above.

For example:

```text
POST http://127.0.0.1:5000/api/users/login
```

With JSON data:

```json
{
  "username": "example",
  "password": "123456"
}
```

---

# 18. Main Features

The application currently provides:

- User registration
- User login
- Task creation
- Task listing
- Task editing
- Task completion
- Task deletion
- Upcoming task notifications
- REST API communication
- SQLite database storage
- Automated testing
- Black box API testing
- White box testing
- Integration testing
- Persistent basic login state using localStorage

---

# 19. Component Responsibilities

### User Component

Handles:

- User registration
- User login
- User validation

### Task Component

Handles:

- Task creation
- Task retrieval
- Task updating
- Task deletion

### Notification Component

Handles:

- Finding upcoming pending tasks
- Returning notification information

### Database Component

Handles:

- SQLite connection
- Database initialization
- Database tables

### REST API

Handles:

- HTTP requests
- Request validation
- Communication between frontend and backend

### Frontend

Handles:

- User interface
- User interaction
- API requests
- Task display
- Task operations
- Login state

---

# 20. Future Improvements

Possible future improvements include:

- Password hashing
- Token-based authentication
- Role-based authorization
- PostgreSQL or MySQL database support
- Email notifications
- Push notifications
- Task priorities
- Task categories
- Recurring tasks
- Calendar integration
- File attachments
- Task comments
- Performance and load testing
- Deployment to a production server

---

# 21. Project Goal

The main goal of this project is not only to create a task management application, but also to demonstrate how software engineering components can be used to design, implement, integrate, and test a modular software system.

The project demonstrates the complete development process from requirements analysis to implementation and testing.

---

# 22. Author

**Abdullah Başal**

Software Engineering Student

**Project:** Development of a Modular Task Management System Based on Software Engineering Components
