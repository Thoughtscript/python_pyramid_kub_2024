from pyramid import testing
import unittest
from mymath import MathApi

class IntegrationEncapsulatedAdditionTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_add_and_encapsulate_vals_endpoint(self):
        request = testing.DummyRequest(method="POST", params={'x': '2', 'y': '3'})
        view = MathApi(request)
        response = view.add_and_encapsulate_vals_endpoint()
        expected = "200 OK\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length: 72\r\n\r\n[ status: 200 message: ADD_AND_ENCAPSULATE_VALS content: {'result': 5} ]"
        self.assertEqual(str(response), expected)

class IntegrationBasicAdditionTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_basic_addition_endpoint(self):
        request = testing.DummyRequest(method="POST", params={'x': '5', 'y': '2'})
        view = MathApi(request)
        response = view.basic_addition_endpoint()
        expected = "200 OK\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length: 45\r\n\r\n[ status: 200 message: BASIC_ADD content: 7 ]"
        self.assertEqual(str(response), expected)

if __name__ == '__main__':
    unittest.main()