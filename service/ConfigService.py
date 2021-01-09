import json

CONFIG_FILE_WEB_MODE = "/config/webmode"
CONFIG_FILE_SETTINGS_FILE = "/config/settings.json"

class ConfigService:
    def __init__(self):
        pass
    
    def is_webmode(self):
        webmode = False
        try:
            f = open(CONFIG_FILE_WEB_MODE, "r")
            webmode = True
            f.close()
        except OSError:
            webmode = False
        return webmode

    def enable_webmode(self):
        f = open(CONFIG_FILE_WEB_MODE, "w")
        f.close()

    def disable_webmode(self):
        try:
            import os
            os.remove(CONFIG_FILE_WEB_MODE)
        except OSError:
            pass

    def load_config(self):
        with open(CONFIG_FILE_SETTINGS_FILE, "r") as json_file:
            self._settings = json.load(json_file)
    
    def get_button_pin(self):
        pin = 0 # default onboard
        try:
            pin = self._settings["sensor"]["button"]
            pin = int(pin)
        except:
            pin = 0 # default onboard
            pass
        return pin

    def get_led_pin(self):
        pin = 2 # default onboard
        try:
            pin = self._settings["sensor"]["led"]
            pin = int(pin)
        except:
            pin = 2 # default onboard
            pass
        return pin

    def get_network_ssid(self):
        return self._settings["network"]["ssid"]

    def get_network_pwd(self):
        return self._settings["network"]["pwd"]

    def get_network_mode(self):
        mode = 2 # station connect to wifi
        try:
            mode = self._settings["network"]["mode"]
            mode = int(mode)
        except:
            mode = 2 # station connect to wifi
            pass
        return mode