from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
users = {}

@app.route('/')
def home():
    return "Welcome to the User Management API!"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = len(users) + 1
    users[user_id] = data
    return jsonify({"message": "User added", "id": user_id}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.get_json()
        users[user_id].update(data)
        return jsonify({"message": "User updated"})
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

if __name__== '_main_':
    app.run(debug=True)
