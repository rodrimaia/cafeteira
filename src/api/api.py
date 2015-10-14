from flask import Flask, jsonify

coffee_app = None
api_flask = Flask(__name__)


@api_flask.route("/")
def hello():
    return 'Api da Cafeteira'


@api_flask.route("/cafe", methods=['GET'])
def get_status():
    return jsonify(status=coffee_app.get_machine_status().name)


@api_flask.route("/cafe", methods=['POST'])
def post_start_machine():
    coffee_app.start_coffee_routine_async()
    return get_status()


def start():
    api_flask.run(debug=True, port=3000, host='0.0.0.0')


class Api:
    def __init__(self, app):
        global coffee_app
        coffee_app = app
        self.api_flask = api_flask

    def start(self):
        start()
