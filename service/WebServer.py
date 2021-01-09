class WebServer:
    def __init__(self):
        pass

    def run(self):
        import picoweb
        app = picoweb.WebApp(__name__)

        @app.route('/')
        def html(req, res):
          sensor={"tmpr": 1,"hmdty": 1}
          yield from picoweb.start_response(res, content_type = "text/html")
          yield from app.render_template(res, "hello.tpl", (sensor,))

        @app.route('/update-network')
        def renderConfig(req, res):
          yield from picoweb.start_response(res, content_type = "text/html")
          await req.read_form_data()
          print(req.form.items())
          # req.form.items()
          yield from res.awrite(str(req.form.items()))

        app.run(debug=True, host="0.0.0.0", port=80)
