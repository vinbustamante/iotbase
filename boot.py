# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

# import webrepl
# webrepl.start()


import network
try:
  import usocket as socket
except:
  import socket

wlan = network.WLAN(network.AP_IF)
wlan.active(True)
wlan.config(essid='dev-ice', password='dev-ice')

ipadd=wlan.ifconfig()


while wlan.active() == False:
    pass

print(wlan.ifconfig())


import picoweb
app = picoweb.WebApp(__name__)

@app.route('/hello')
def html(req, res):
  sensor={"tmpr": 1,"hmdty": 1}
  yield from picoweb.start_response(res, content_type = "text/html")
  yield from app.render_template(res, "hello.tpl", (sensor,))

app.run(debug=True, host =ipadd[0])

