import unittest
from api.api import Api
from mock import MagicMock


class ApiTest(unittest.TestCase):

    def setUp(self):
        self.tester = Api(MagicMock()).app.test_client(self)

    def test_hello_api(self):
        r = self.tester.get('/')
        self.assertEqual(r.data, 'Api da Cafeteira')
