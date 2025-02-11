from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

AUDD_API_KEY = os.environ["AUDIO_API_KEY"]

@app.route("/recognize", methods=["POST"])
def recognize_audio():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    response = requests.post(
        "https://api.audd.io/",
        data={"api_token": AUDD_API_KEY, "return": "spotify"},
        files={"file": file}
    )

    return response.json()

if __name__ == "__main__":
    app.run(port=5002, debug=True)
