import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('redsoft', 'stardust')

while not wlan.isconnected():
    pass
print(wlan.ifconfig())