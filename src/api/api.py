from flask import Flask


class Api:

    app = Flask(__name__)

    def __init__(self):
        pass

    @app.route("/")
    def hello():
        return "Hello World!"

    def start(self):
        self.app.run()
