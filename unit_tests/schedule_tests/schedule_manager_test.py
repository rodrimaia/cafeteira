import unittest
from schedule.schedule_manager import ScheduleManager
from freezegun import freeze_time


class ScheduleManagerTest(unittest.TestCase):
    def setUp(self):
        self.target = ScheduleManager(['15:00', '10:00'])

    @freeze_time("2015-10-10 10:00:00")
    def test_manager_should_format_actual_time(self):
        self.assertEqual(self.target.get_actual_time(), '10:00')

    @freeze_time("2015-10-10 10:00:00")
    def test_manager_should_return_true_if_its_scheduled_time(self):
        self.assertTrue(self.target.its_time())

    @freeze_time("2015-10-10 09:59:00")
    def test_manager_should_return_false_if_its_scheduled_time(self):
        self.assertFalse(self.target.its_time())
