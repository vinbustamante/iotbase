import time
from service.Led import Led

# from machine import Pin

# led=Pin(2,Pin.OUT)

led = Led(2)
while True:
    led.toggle()
    time.sleep(0.1)
 
# while True:
#     led.value(1)
#     time.sleep(0.5)
#     led.value(0)
#     time.sleep(0.5)