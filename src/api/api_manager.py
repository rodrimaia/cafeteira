from flask import Flask, jsonify
from logger import logger

coffee_app = None
api_flask = Flask(__name__)


@api_flask.route("/")
def hello():
    logger.debug('Root opened!')
    return 'Api da Cafeteira'


@api_flask.route("/cafe", methods=['GET'])
def get_status():
    logger.debug('Get coffe status by API')
    return jsonify(status=coffee_app.get_machine_status().name)


@api_flask.route("/calendario", methods=['GET'])
def get_times():
    return jsonify(times=coffee_app.get_schedule_times())


@api_flask.route("/cafe", methods=['POST'])
def post_start_machine():
    logger.debug('Start coffe machine by API')
    coffee_app.start_coffee_routine_async()
    return get_status()


def start():
    logger.debug('API start')
    api_flask.run(debug=True, port=3000, host='0.0.0.0')


class ApiManager:
    def __init__(self, app):
        global coffee_app
        coffee_app = app
        self.api_flask = api_flask

    def start(self):
        start()
