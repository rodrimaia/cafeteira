from flask import Flask, jsonify


class ApiData:
    def __init__(self):
        self.machine = None


class Api:
    def __init__(self, machine):
        dados.machine = machine
        self.app = app

    def start(self):
        start()


app = Flask(__name__)
dados = ApiData()


@app.route("/")
def hello():
    return 'Api da Cafeteira'


@app.route("/cafe", methods=['GET'])
def get_status():
    return jsonify(status=dados.machine.machine_status.name)


@app.route("/cafe", methods=['POST'])
def post_start_machine():
    dados.machine.start_coffee_routine_async()
    return get_status()


def start():
    app.run(debug=True, port=3000, host='0.0.0.0')
