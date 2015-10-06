import unittest
from api.api import Api


class ApiTest(unittest.TestCase):

    def setUp(self):
        self.tester = Api().app.test_client(self)

    def test_hello_api(self):
        r = self.tester.get('/')
        self.assertEqual(r.data, 'Hello World!')
