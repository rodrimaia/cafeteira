from gpiocrust import  Header, OutputPin

class CoffeeMachine:

    def __init__(self):
	self.header = Header()
        self.relay = OutputPin(13)

    def start(self):
        self.relay.value = True

    def stop(self):
        self.relay.value = False


