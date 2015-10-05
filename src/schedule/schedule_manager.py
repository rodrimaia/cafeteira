from datetime import datetime

class ScheduleManager():

    def get_actual_time(self):
        now = datetime.now()
        return "%02d:%02d" % (now.hour,now.minute)

