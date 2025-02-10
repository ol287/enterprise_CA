import unittest
import requests

BASE_URL = "http://localhost:5001"

class TestTrackCatalogue(unittest.TestCase):
    def test_add_track(self):
        response = requests.post(f"{BASE_URL}/tracks", json={"title": "Test Song", "artist": "Test Artist"})
        self.assertEqual(response.status_code, 201)

    def test_list_tracks(self):
        response = requests.get(f"{BASE_URL}/tracks")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_remove_track(self):
        response = requests.post(f"{BASE_URL}/tracks", json={"title": "Delete Me", "artist": "Test"})
        track_id = requests.get(f"{BASE_URL}/tracks").json()[-1]["id"]
        response = requests.delete(f"{BASE_URL}/tracks/{track_id}")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
