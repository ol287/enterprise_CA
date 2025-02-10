from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    with sqlite3.connect("tracks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tracks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                artist TEXT NOT NULL
            )
        """)
        conn.commit()

@app.route("/tracks", methods=["GET"])
def list_tracks():
    with sqlite3.connect("tracks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, artist FROM tracks")
        tracks = [{"id": row[0], "title": row[1], "artist": row[2]} for row in cursor.fetchall()]
    return jsonify(tracks)

@app.route("/tracks", methods=["POST"])
def add_track():
    data = request.json
    if "title" not in data or "artist" not in data:
        return jsonify({"error": "Missing title or artist"}), 400

    with sqlite3.connect("tracks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tracks (title, artist) VALUES (?, ?)", (data["title"], data["artist"]))
        conn.commit()
    
    return jsonify({"message": "Track added"}), 201

@app.route("/tracks/<int:track_id>", methods=["DELETE"])
def remove_track(track_id):
    with sqlite3.connect("tracks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tracks WHERE id = ?", (track_id,))
        conn.commit()

    return jsonify({"message": "Track removed"}), 200

if __name__ == "__main__":
    init_db()
    app.run(port=5001, debug=True)
