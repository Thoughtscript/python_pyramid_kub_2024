import unittest
import requests

EXAMPLE_TEST_URL = 'http://localhost:8000/api/example/all'

METHOD_TEST_URL = 'http://localhost:8000/api/methods'

class FunctionalExampleScanTest(unittest.TestCase):
    def setUp(self):
        self.response = requests.get(EXAMPLE_TEST_URL)

    def tearDown(self):
        self.response.close()

    def test_response(self):
        self.assertIn('[ status: 200 message: SCANNED content: dict_values([]) ]', self.response.text)
        self.assertIs(200, self.response.status_code)

class FunctionalMethodGetTest(unittest.TestCase):
    def setUp(self):
        self.response = requests.get(METHOD_TEST_URL)

    def tearDown(self):
        self.response.close()

    def test_response(self):
        self.assertIn('GET', self.response.text)
        self.assertIs(200, self.response.status_code)

class FunctionalMethodDeleteTest(unittest.TestCase):
    def setUp(self):
        self.response = requests.delete(METHOD_TEST_URL)

    def tearDown(self):
        self.response.close()

    def test_response(self):
        self.assertIn('DELETE', self.response.text)
        self.assertIs(200, self.response.status_code)

class FunctionalMethodPostTest(unittest.TestCase):
    def setUp(self):
        self.response = requests.post(METHOD_TEST_URL)

    def tearDown(self):
        self.response.close()

    def test_response(self):
        self.assertIn('POST', self.response.text)
        self.assertIs(200, self.response.status_code)

if __name__ == '__main__':
    unittest.main()