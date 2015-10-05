class ScheduleReader:

    FILE_NAME = "schedule_coffee.txt"

    def __init__(self):
        self

    def open_file(self):
        return open(FILE_NAME)
 
    def read_scheduled_times(self):
        lines = [line.strip() for line in self.open_file() ]
        return lines
