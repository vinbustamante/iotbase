CONFIG_FILE_OS_MODE = "/config/webmode"

class ConfigService:
    def __init__(self):
        pass
    
    def is_webmode(self):
        webmode = False
        try:
            f = open(CONFIG_FILE_OS_MODE, "r")
            webmode = True
            f.close()
        except OSError:
            webmode = False
        return webmode

    def enable_webmode(self):
        f = open(CONFIG_FILE_OS_MODE, "w")
        f.close()