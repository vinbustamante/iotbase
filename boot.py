# This file is executed on every boot (including wake-boot from deepsleep)
import gc #active
gc.collect() # active


#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

# import webrepl
# webrepl.start()

# import picoweb
# app = picoweb.WebApp(__name__)

# @app.route('/hello')
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

# app.run(debug=True, host =ipadd[0])

