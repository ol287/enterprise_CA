from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TRACK_SERVICE_URL = "http://localhost:5001"
AUDIO_SERVICE_URL = "http://localhost:5002"

@app.route("/tracks", methods=["GET", "POST"])
def handle_tracks():
    if request.method == "GET":
        response = requests.get(f"{TRACK_SERVICE_URL}/tracks")
    else:
        response = requests.post(f"{TRACK_SERVICE_URL}/tracks", json=request.json)
    return jsonify(response.json()), response.status_code

@app.route("/tracks/<int:track_id>", methods=["DELETE"])
def delete_track(track_id):
    response = requests.delete(f"{TRACK_SERVICE_URL}/tracks/{track_id}")
    return jsonify(response.json()), response.status_code

@app.route("/recognize", methods=["POST"])
def recognize_audio():
    response = requests.post(f"{AUDIO_SERVICE_URL}/recognize", files=request.files)
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(port=5000, debug=True)
