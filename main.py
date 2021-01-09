import time
import machine
from service.Wifi import Wifi
from service.ConfigService import ConfigService
from service.Button import Button

# LOAD CONFIG
configService = ConfigService()
configService.load_config()

PIN_BUTTON = configService.get_button_pin()
PIN_LED = configService.get_led_pin()
button = Button(PIN_BUTTON)


def connect_to_network():
    wlan = Wifi(configService.get_network_ssid(), configService.get_network_pwd(), configService.get_network_mode())
    wlan.connect()
    while wlan.is_connected() == False:
        pass
    print(wlan.info())

def load_web_server():
    from service.Led import Led
    led = Led(PIN_LED)
    from service.WebServer import WebServer
    led.on()
    webServer = WebServer()
    webServer.run()    

def on_button_click():
    from service.Led import Led
    led = Led(PIN_LED)
    configService.enable_webmode()
    led.blink()
    led.off()
    machine.reset()


connect_to_network()  
if configService.is_webmode():
    load_web_server() 
else:    
    while True:
        if button.is_press():
            on_button_click()
        time.sleep(1.0)