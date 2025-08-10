# flask-rest-api

## 📌 Overview
A simple REST API built with Flask to manage user data using in-memory storage.

## 🚀 Features
- GET: Fetch all users or a single user
- POST: Add new user
- PUT: Update existing user
- DELETE: Remove user

## 🛠 Installation
1. Clone the repository
   ```bash
   git clone <https://github.com/Rajeshwari1294/flask-rest-api.git>
   cd flask-rest-api
2. Install dependecies
   pip install -r requirements.txt
3. Run the server
   python app.py

## Testing

Use Postman or cURL to test:

1.GET all users: GET /users

2.GET single user: GET /users/<id>

3.POST new user: POST /users (JSON body: { "name": "John", "email": "john@example.com" })

4.PUT update user: PUT /users/<id>

5.DELETE user: DELETE /users/<id>
