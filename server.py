from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/kur")
def kur():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; ESP8266; +https://github.com/truncgil/Finans)"
        }
        r = requests.get("https://finans.truncgil.com/v4/today.json", headers=headers, timeout=5)
        r.raise_for_status()  # HTTP hatalarını yakalar
        data = r.json()  # JSON'a çevir
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
