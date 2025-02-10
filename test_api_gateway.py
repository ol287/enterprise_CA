import unittest
import requests

BASE_URL = "http://localhost:5000"

class TestAPIGateway(unittest.TestCase):
    def test_list_tracks(self):
        response = requests.get(f"{BASE_URL}/tracks")
        self.assertEqual(response.status_code, 200)

    def test_add_track_through_gateway(self):
        response = requests.post(f"{BASE_URL}/tracks", json={"title": "Gateway Song", "artist": "Gateway Artist"})
        self.assertEqual(response.status_code, 201)

if __name__ == "__main__":
    unittest.main()
