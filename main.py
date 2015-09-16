import schedule
import time
from twitter_wrapper import TwitterWrapper

twitter = TwitterWrapper()
a = 1
def job():
    global a
    twitter.update_status("Que dia EXPLENDIDO %d" % a)
    a += 1

def main():
    job()
    #schedule.every(1).minutes.do(job)
    #while True:
    #    schedule.run_pending()
    #    time.sleep(1)

if __name__ == "__main__":
    main()
