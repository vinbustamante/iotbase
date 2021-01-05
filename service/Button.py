import machine

class Button:
    def __init__(self, pin = 0):
        self._button = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP)

    def is_press(self):
        return not self._button.value()