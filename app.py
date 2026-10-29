
from flask import Flask, request, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "owner": "Cyber Deepak",
        "status": "online",
        "message": "Welcome to my API"
    })

@app.get("/api/status")
def status():
    return jsonify({
        "status": "success",
        "service": "Deepak API",
        "time": datetime.now(timezone.utc).isoformat()
    })

@app.post("/api/sms-test")
def sms_test():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    if not isinstance(message, str) or not message.strip():
        return jsonify({
            "status": "error",
            "message": "Message is required"
        }), 400

    if len(message) > 500:
        return jsonify({
            "status": "error",
            "message": "Message too long"
        }), 400

    return jsonify({
        "status": "success",
        "mode": "demo",
        "message": "Validated; no SMS sent."
    })

if __name__ == "__main__":
    app.run()
