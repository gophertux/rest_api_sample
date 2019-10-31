import json
import unittest

from api import app

class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_api_path(self):
        resp = self.client.get(path='/v0/launchpad_info', content_type="application/json")
        self.assertEqual(resp.status_code, 200)

if __name__ == '__main__':
    unittest.main()
