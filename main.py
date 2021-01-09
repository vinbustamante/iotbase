import time
import machine
from service.Wifi import Wifi
from service.ConfigService import ConfigService
from service.Button import Button

PIN_BUTTON = 0
PIN_LED = 2

# CONNECT TO NETWORK
wlan = Wifi("redsoft", "stardust", 2)
wlan.connect()
while wlan.is_connected() == False:
    pass
ipadd=wlan.info()
print(wlan.info())


# LOAD UI MANAGEMENT ONLY IF ENABLE
configService = ConfigService()
if configService.is_webmode():
    from service.Led import Led
    led = Led(PIN_LED)
    from service.WebServer import WebServer
    led.on()
    webServer = WebServer()
    webServer.run()    
else:
    button = Button(PIN_BUTTON)
    while True:
        if button.is_press():
            from service.Led import Led
            led = Led(PIN_LED)
            configService.enable_webmode()
            led.blink()
            led.off()
            machine.reset()

        time.sleep(1.0)