from flask import Flask, jsonify, request

app = Flask(__name__)

users = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    user = request.json
    users.append(user)
    return jsonify(user), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
