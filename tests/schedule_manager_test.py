import unittest
from mock import MagicMock
from schedule.schedule_manager import ScheduleManager
from freezegun import freeze_time

class ScheduleManagerTest(unittest.TestCase):
    def setUp(self):
        self.target = ScheduleManager()

    @freeze_time("2015-10-10 10:00:00")
    def test_manager_should_format_actual_time(self):
        self.assertEqual(self.target.get_actual_time(), '10:00')

