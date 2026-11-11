from flask import Flask, request, jsonify

app = Flask(__name__)

VALID_API_KEY = "MY_FREE_KEY_123"

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "Meri Free API kamyabi se chal rahi hai!"
    })

@app.route('/api/process', methods=['GET'])
def process_request():
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
