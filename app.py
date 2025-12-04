from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# ------------------------------
# 1. Basic Message
# ------------------------------
@app.route("/api/message")
def message():
    return jsonify({"message": "Hello from Backend API!"})


# ------------------------------
# 2. Current Server Time
# ------------------------------
@app.route("/api/time")
def current_time():
    return jsonify({
        "server_time": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    })


# ------------------------------
# 3. Simple Add Function (GET)
# Example: /api/add?x=5&y=10
# ------------------------------
@app.route("/api/add")
def add_numbers():
    try:
        x = float(request.args.get("x", 0))
        y = float(request.args.get("y", 0))
        return jsonify({
            "x": x,
            "y": y,
            "result": x + y
        })
    except:
        return jsonify({"error": "Invalid input"}), 400


# ------------------------------
# 4. Sample Users List (Static)
# ------------------------------
@app.route("/api/users")
def list_users():
    users = [
        {"id": 1, "name": "Alice", "role": "Admin"},
        {"id": 2, "name": "Bob", "role": "Editor"},
        {"id": 3, "name": "Charlie", "role": "Viewer"}
    ]
    return jsonify(users)


# ------------------------------
# 5. Health Check for Load Balancer / CodeDeploy
# ------------------------------
@app.route("/api/health")
def health():
    return jsonify({"status": "healthy"}), 200


# ------------------------------
# Run App
# ------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
