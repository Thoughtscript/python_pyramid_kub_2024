import unittest
import requests

class FunctionalMethodGetTest(unittest.TestCase):
    def setUp(self):
        self.response = requests.get('http://localhost:8000/api/methods')

    def tearDown(self):
        self.response.close()

    def test_response(self):
        self.assertIn('GET', self.response.text)
        self.assertIs(200, self.response.status_code)

class FunctionalMethodDeleteTest(unittest.TestCase):
    def setUp(self):
        self.response = requests.delete('http://localhost:8000/api/methods')

    def tearDown(self):
        self.response.close()

    def test_response(self):
        self.assertIn('DELETE', self.response.text)
        self.assertIs(200, self.response.status_code)

class FunctionalMethodPostTest(unittest.TestCase):
    def setUp(self):
        self.response = requests.post('http://localhost:8000/api/methods')

    def tearDown(self):
        self.response.close()

    def test_response(self):
        self.assertIn('POST', self.response.text)
        self.assertIs(200, self.response.status_code)


if __name__ == '__main__':
    unittest.main()