import unittest
import json
from api.api import Api
from mock import MagicMock, Mock
from machine.machine_manager import MachineStatus


class ApiTest(unittest.TestCase):

    def setUp(self):
        cafeteira = Mock()
        cafeteira.get_machine_status = MagicMock(
            return_value=MachineStatus.stand_by)
        self.tester = Api(cafeteira).api_flask.test_client(self)

    def test_hello_api(self):
        r = self.tester.get('/')
        self.assertEqual(r.data, 'Api da Cafeteira')

    def test_cafe_should_return_machine_status(self):
        r = self.tester.get('/cafe')
        expected = json.dumps({'status': 'stand_by'}, indent=2)
        self.assertEqual(r.data, expected)
