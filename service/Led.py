from machine import Pin

class Led:
    def __init__(self, pin = 2):
        self._led = Pin(pin, Pin.OUT)
        self.off()

    def off(self):
        self._value = 0
        self._led.value(0)
    
    def on(self):
        self._value = 1
        self._led.value(1)

    def toggle(self):
        if self._value == 0:
            self.on()
        else:
            self.off()