import sqlite3

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

if __name__ == "__main__":
    init_db()
    print("Database initialized.")