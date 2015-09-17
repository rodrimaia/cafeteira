from gpiocrust import  Header, OutputPin

class CoffeeMachine:
    relay = OutputPin(13)

    def __init__(self):
        Header()

    def start(self):
        self.relay.value = True

    def stop(self):
        self.relay.value = False


