from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/kur")
def kur():
    r = requests.get("https://finans.truncgil.com/v4/today.json")
    return jsonify(r.json())

app.run(host="0.0.0.0", port=10000)

