import unittest
import requests

BASE_URL = "http://localhost:5002"

class TestAudioRecognition(unittest.TestCase):
    def test_no_file_uploaded(self):
        response = requests.post(f"{BASE_URL}/recognize", files={})
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
