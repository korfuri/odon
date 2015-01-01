#!/usr/bin/env python

import os
from flask import Flask
from stem.control import Controller

app = Flask(__name__)

def new_hidden_service(target_port):
    try:
        with Controller.from_port(port = 9051) as controller:
            controller.authenticate(password='salutlesamis')
            directory = os.path.join(controller.get_conf('DataDirectory'),
                                     'odon')
            r = controller.create_hidden_service(directory, 80, target_port=target_port)
            if r.hostname:
                return r.hostname
    except e:
        app.logger.error(e)
        raise e
    app.logger.error('fuck fuck fuck')
    raise 'Unable to create a service'

@app.route('/advertise')
def advertise():
    hostname = new_hidden_service(target_port=5000)
    return 'http://%s' % hostname

@app.route('/')
def index():
    hostname = new_hidden_service(target_port=8080)
    return 'http://%s' % hostname

@app.route('/ping')
def ping():
    return 'pong'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
