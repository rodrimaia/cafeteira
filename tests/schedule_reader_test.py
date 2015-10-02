import unittest
from mock import MagicMock
from schedule.schedule_reader import ScheduleReader

class ScheduleReaderTest(unittest.TestCase):
    def setUp(self):
        self.target = ScheduleReader()
        self.target.open_file = MagicMock(return_value=['   10:00           ', '  11:00'])


    def test_read_schedule_should_remove_empty_spaces(self):
        self.assertEqual(self.target.read_scheduled_times(), ['10:00','11:00'])

    def test_read_schedule_should_not_return_invalid_times(self):
        self.assertNotEqual(self.target.read_scheduled_times(), ['10:00','14:00'])

