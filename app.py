from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# ✅ Allow CORS from your GitHub Pages domain
CORS(app, resources={r"/*": {"origins": "https://vinayakiit.github.io"}})

@app.route("/analyze", methods=["POST"])
def analyze_password():
    data = request.get_json()
    password = data.get("password", "")
    # ... (your analysis logic)
    return jsonify({
        "score": 72,
        "length": len(password),
        "hasUpper": any(c.isupper() for c in password),
        "hasLower": any(c.islower() for c in password),
        "hasNumber": any(c.isdigit() for c in password),
        "hasSpecial": any(not c.isalnum() for c in password),
        "isCommon": password.lower() in ["password", "123456", "qwerty"],
        "hasSequential": "123" in password or "abc" in password,
        "hasRepeated": len(set(password)) < len(password)
    })

