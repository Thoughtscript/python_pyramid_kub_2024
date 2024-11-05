from pyramid import testing
import unittest

def test_view(request):
    x = int(request.params.get('x', 0))
    y = int(request.params.get('y', 0))
    return {'result': x + y}

class IntegrationTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_test_view(self):
        request = testing.DummyRequest(params={'x': '2', 'y': '3'})
        response = test_view(request)
        self.assertEqual(response['result'], 5)

if __name__ == '__main__':
    unittest.main()