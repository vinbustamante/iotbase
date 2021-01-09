import picoweb
import machine
import time
from service.ConfigService import ConfigService
from service.Led import Led
class WebServer:
    def __init__(self):
        pass

    def run(self):        
        # @app.route('/')
        # def html(req, res):
        #   sensor={"tmpr": 1,"hmdty": 1}
        #   yield from picoweb.start_response(res, content_type = "text/html")
        #   yield from app.render_template(res, "hello.tpl", (sensor,))

        # @app.route('/update-network')
        # def renderConfig(req, res):
        #   yield from picoweb.start_response(res, content_type = "text/html")
        #   await req.read_form_data()
        #   print(req.form.items())
        #   # req.form.items()
        #   yield from res.awrite(str(req.form.items()))

        ROUTES = [
          ("/",  lambda req, res:  self.index(req, res) ),
          ("/blink_led",  lambda req, res:  self.blink_led(req, res) ),
          ("/restart",  lambda req, res:  self.restart(req, res) ),
          ("/set_normal_boot",  lambda req, res:  self.set_normal_boot(req, res) )
        ]
        self._app = picoweb.WebApp(__name__, ROUTES)
        self._app.run(debug=True, host="0.0.0.0", port=80)
    
    def index(self, req, res):
          sensor={"tmpr": 1,"hmdty": 1}
          yield from picoweb.start_response(res, content_type = "text/html")
          yield from self._app.render_template(res, "hello.tpl", (sensor,))

    def restart(self, req, res):
      led = Led()
      yield from picoweb.start_response(res, content_type = "text/html")
      yield from res.awrite("done")
      machine.reset()

    def blink_led(self,req, res):
      yield from picoweb.start_response(res, content_type = "text/html")
      await req.read_form_data()
      count = req.form["count"]
      if not count:
        count = 5
      else:
        count = int(count)
      led = Led()
      led.blink(count)
      led.on()
      yield from res.awrite("done")

    def set_normal_boot(self, req, res):     
      led = Led()
      configService = ConfigService()
      configService.disable_webmode()
      led.blink()
      led.on()
      yield from picoweb.start_response(res, content_type = "text/html")
      yield from res.awrite("done")
        
