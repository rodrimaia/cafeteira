class ScheduleReader:

    def __init__(self, file_name = "schedule_coffee.txt"):
        self.FILE_NAME = file_name

    def open_file(self):
        return open(self.FILE_NAME)
 
    def read_scheduled_times(self):
        lines = [line.strip() for line in self.open_file() ]
        return lines
