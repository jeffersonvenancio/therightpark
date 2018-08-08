from flask import Flask, request, session, url_for
from flask_cors import CORS
from werkzeug.utils import redirect
from requests_toolbelt.adapters import appengine
from google.appengine.ext import ndb

appengine.monkeypatch()

import json
import re

from car.controller import cars as cars_controller
from slot.controller import slots as slots_controller
from park.controller import parks as parks_controller

app = Flask(__name__, static_folder='web')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(cars_controller, url_prefix='/api/cars')
app.register_blueprint(slots_controller, url_prefix='/api/slots')
app.register_blueprint(parks_controller, url_prefix='/api/parks')

@app.route('/')
def main():
    return app.send_static_file('index.html')

@app.route('/meuIp/')
def meu_ip():
    return json.dumps(request.headers.get('X-Forwarded-For', request.remote_addr))

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
    return 'Sorry, unexpected error: {}'.format(e), 500
