import unittest
from schedule.schedule_reader import ScheduleReader


class ScheduleReaderIntegrationTest(unittest.TestCase):

    def setUp(self):
        self.target = ScheduleReader('integration_tests/schedule_test.txt')

    def test_schedule_reader_should_read_times_from_text_file(self):
        times = self.target.read_scheduled_times()
        self.assertEqual(times, ['19:33', '04:20'])

if __name__ == 'main':
    unittest.main()
