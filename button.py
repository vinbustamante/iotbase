import time
from service.Button import Button

PIN_BUTTON = 0

button = Button(PIN_BUTTON)
while True:
    if button.is_press():
        print('Button pressed!')
    time.sleep(1.0)
    