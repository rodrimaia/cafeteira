import unittest
import json
from api.api import Api
from mock import MagicMock, Mock
from machine.machine_manager import MachineStatus


class ApiTest(unittest.TestCase):

    def setUp(self):
        self.cafeteira = Mock()
        self.cafeteira.get_machine_status = MagicMock(
            return_value=MachineStatus.stand_by)
        self.cafeteira.start_coffee_routine_async = MagicMock()
        self.tester = Api(self.cafeteira).api_flask.test_client(self)

    def test_hello_api(self):
        r = self.tester.get('/')
        self.assertEqual(r.data, 'Api da Cafeteira')

    def test_cafe_should_return_machine_status(self):
        r = self.tester.get('/cafe')
        expected = json.dumps({'status': 'stand_by'}, indent=2)
        self.assertEqual(r.data, expected)

    def test_cafe_should_start_make_coffee(self):
        self.tester.post('/cafe')
        self.assertTrue(self.cafeteira.start_coffee_routine_async.called)
        self.assertTrue(self.cafeteira.get_machine_status.called)
