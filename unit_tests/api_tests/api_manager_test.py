import unittest
import json
from api.api_manager import ApiManager
from mock import MagicMock, Mock
from machine.machine_manager import MachineStatus


class ApiManagerTest(unittest.TestCase):

    def setUp(self):
        self.coffee_file = Mock()
        self.coffee_file.get_machine_status = MagicMock(
            return_value=MachineStatus.stand_by)
        self.coffee_file.get_schedule_times = MagicMock(
            return_value=['09:00'])
        self.coffee_file.start_coffee_routine_async = MagicMock()
        self.target = ApiManager(self.coffee_file).api_flask.test_client(self)

    def test_api_should_given_information_about_app(self):
        result = self.target.get('/')
        self.assertEqual(result.data, 'Api da Cafeteira')

    def test_api_should_return_machine_status(self):
        result = self.target.get('/cafe')
        expected = json.dumps({'status': 'stand_by'}, indent=2)
        self.assertEqual(result.data, expected)

    def test_api_should_return_schedule_times(self):
        result = self.target.get('/calendario')
        expected = json.dumps(
            {'times': ['09:00']}, indent=2,  separators=(',', ': '))
        self.assertEqual(result.data, expected)

    def test_api_should_start_make_coffee(self):
        self.target.post('/cafe')
        self.assertTrue(self.coffee_file.start_coffee_routine_async.called)
        self.assertTrue(self.coffee_file.get_machine_status.called)
