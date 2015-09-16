import RPi.GPIO as GPIO
import time

activated = False
twitter = TwitterWrapper()
a = 12

def job():
    global twitter
    global a
    twitter.update_status("Que dia EXPLENDIDO %s" % a)
    a += 1

def buttonHandler(pin):
    print "detectei"
    global activated
    global job
    if(activated):
	activated = False
    else:
	activated = True
        job()

BUTTON_PIN = 15

GPIO.setmode(GPIO.BOARD)
relayPin = 13
GPIO.setup(relayPin, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=buttonHandler, bouncetime=800)
#GPIO.add_event_callback(BUTTON_PIN,buttonHandler)

def budega():
    global activated
    time.sleep(10)
    GPIO.output(relayPin, True)
    job()
    time.sleep(10)
    GPIO.output(relayPin, False)

while(True):
      budega()
      print activated

