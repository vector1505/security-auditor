from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check_website():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    payload = {
        "client": {
            "clientId": "guardify",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": url}
            ]
        }
    }

    api_key = os.getenv("GOOGLE_API_KEY")
    response = requests.post(
        f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}",
        json=payload
    )

    if response.status_code != 200:
        return jsonify({"error": "Safe Browsing API request failed"}), 500

    result = response.json()

    if "matches" in result:
        return jsonify({"safe": False, "details": result["matches"]})
    else:
        return jsonify({"safe": True, "details": "No threats detected."})


if __name__ == '__main__':
    app.run(debug=True)

