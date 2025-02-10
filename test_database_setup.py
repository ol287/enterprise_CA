import os
import unittest
import sqlite3

class TestDatabaseSetup(unittest.TestCase):
    def test_database_created(self):
        self.assertTrue(os.path.exists("tracks.db"))

    def test_tracks_table_exists(self):
        with sqlite3.connect("tracks.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tracks'")
            result = cursor.fetchone()
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()