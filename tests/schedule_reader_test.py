import unittest
from mock import MagicMock
from schedule.schedule_reader import ScheduleReader

class ScheduleReaderTest(unittest.TestCase):
    def setUp(self):
        self.target = ScheduleReader()
        self.target.open_file = MagicMock(return_value=['   10:00           '])


    def test_read_schedule_should_remove_empty_spaces(self):
        self.assertEqual(self.target.read_schedule(), ['10:00'])
