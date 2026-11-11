from flask import Flask, request, jsonify, Response
import json

app = Flask(__name__)

VALID_API_KEY = "MY_FREE_KEY_123"

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
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
    callback = request.args.get('callback')

    if api_key != VALID_API_KEY:
        result = {"success": False, "error": "Invalid ya Missing API Key!"}
    elif not uid:
        result = {"success": False, "error": "UID parameter dalna zaroori hai!"}
    else:
        result = {
            "success": True,
            "uid": uid,
            "server": server,
            "message": f"Request successfully processed for UID {uid} on {server} server."
        }

    # Agar website JSONP callback bhejti hai toh seedha JS script mein jawab dega (No CORS issue ever!)
    if callback:
        js_response = f"{callback}({json.dumps(result)})"
        return Response(js_response, mimetype="application/javascript")

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
