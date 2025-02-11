import sqlite3

def init_db():
    """Initialize the SQLite database with a tracks table."""
    with sqlite3.connect("tracks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tracks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                artist TEXT NOT NULL,
                album TEXT,
                genre TEXT,
                duration INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        )
        conn.commit()

def add_track(title, artist, album=None, genre=None, duration=None):
    """Add a new track to the database."""
    with sqlite3.connect("tracks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tracks (title, artist, album, genre, duration) 
            VALUES (?, ?, ?, ?, ?)
        """, (title, artist, album, genre, duration))
        conn.commit()
        return cursor.lastrowid

def get_tracks():
    """Retrieve all tracks from the database."""
    with sqlite3.connect("tracks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tracks")
        return cursor.fetchall()

def remove_track(track_id):
    """Remove a track from the database by ID."""
    with sqlite3.connect("tracks.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tracks WHERE id = ?", (track_id,))
        conn.commit()

if __name__ == "__main__":
    init_db()
    print("Database initialized.")