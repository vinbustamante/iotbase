import network

class Wifi:
    def __init__(self, ssid, pwd, mode = 2):
        self.MODE_AP = 1
        self.MODE_STA = 2
        self._mode = mode
        self._ssid = ssid
        self._pwd = pwd
        if self.get_mode() == self.MODE_AP:
            self._network = network.WLAN(network.AP_IF)
        else:
            self._network = network.WLAN(network.STA_IF)

    def get_mode(self):
        return self._mode

    def is_connected(self):
        connected = False
        if self.get_mode() == self.MODE_AP:
            connected = self._network.active()
        else:
            connected = self._network.isconnected()
        return connected

    def connect(self):
        self._network.active(True)
        if self.get_mode() == self.MODE_AP:
            self._network.config(essid = self._ssid, password= self._pwd)
        else:
            self._network.connect(self._ssid, self._pwd)

    def info(self):
        return self._network.ifconfig()