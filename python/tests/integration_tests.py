from pyramid import testing
import unittest
from helpers import add_and_encapsulate_vals

class IntegrationTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_addition_view(self):
        request = testing.DummyRequest(params={'x': '2', 'y': '3'})
        x = int(request.params.get('x', 0))
        y = int(request.params.get('y', 0))
        response = add_and_encapsulate_vals(x, y)
        self.assertEqual(response['result'], 5)

if __name__ == '__main__':
    unittest.main()