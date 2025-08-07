# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and test RESTful APIs using the FastAPI framework in Python. By the end of this assignment, you'll understand how to create endpoints, handle requests, and return responses in a modern web API.

## 📝 Tasks

### 🛠️	Create a Simple FastAPI Application

#### Description
Set up a FastAPI project and create a basic API with at least two endpoints (e.g., `/hello` and `/items`).

#### Requirements
Completed program should:

- Use FastAPI to create a web API
- Implement a `/hello` endpoint that returns a greeting message
- Implement a `/items` endpoint that returns a list of items (hardcoded or from a simple data structure)
- Run locally and respond to HTTP requests

### 🛠️	Add CRUD Operations for Items

#### Description
Expand your API to support Create, Read, Update, and Delete (CRUD) operations for items using HTTP methods (GET, POST, PUT, DELETE).

#### Requirements
Completed program should:

- Allow clients to add new items (POST)
- Retrieve items (GET)
- Update items (PUT)
- Delete items (DELETE)
- Use appropriate request/response formats (JSON)

### 🛠️	Bonus: Add Data Validation and Error Handling

#### Description
Improve your API by validating input data and handling errors gracefully.

#### Requirements
Completed program could:

- Use Pydantic models for request validation
- Return helpful error messages for invalid requests
- Document endpoints using FastAPI's automatic docs (Swagger UI)
