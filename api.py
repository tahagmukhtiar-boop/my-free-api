from flask import Flask, request, jsonify

app = Flask(__name__)

VALID_API_KEY = "MY_FREE_KEY_123"

# Yeh function har browser aur website ko API use karne ki ijazat (CORS) deta hai
@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "Meri Free API kamyabi se chal rahi hai!"
    })

@app.route('/api/process', methods=['GET', 'OPTIONS'])
def process_request():
    if request.method == 'OPTIONS':
        return jsonify({"status": "ok"}), 200

    uid = request.args.get('uid')
    server = request.args.get('server', 'PK')
    api_key = request.args.get('key')

    if api_key != VALID_API_KEY:
        return jsonify({"success": False, "error": "Invalid ya Missing API Key!"}), 401

    if not uid:
        return jsonify({"success": False, "error": "UID parameter dalna zaroori hai!"}), 400

    return jsonify({
        "success": True,
        "uid": uid,
        "server": server,
        "message": f"Request successfully processed for UID {uid} on {server} server."
    })

if __name__ == '__main__':
    app.run(debug=True, port=8000)
