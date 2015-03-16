#!/usr/bin/env python

import os
import random
import string
from flask import Flask
from stem.control import Controller

app = Flask(__name__)

class OdonException(Exception):
    pass

class UnableToCreateHiddenServiceException(OdonException):
    pass

class HiddenServiceConfigurationDirectoryUnreadableException(OdonException):
    pass

def new_hidden_service(target_port, config_id_prefix='odon'):
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password='salutlesamis')
        config_id = '%s%s' % (
            config_id_prefix,
            ''.join(random.choice(string.hexdigits) for n in range(15)))
        directory = os.path.join(controller.get_conf('DataDirectory'),
                                 config_id)
        print 'Creating %s' % directory
        r = controller.create_hidden_service(directory, 80, target_port=target_port)
        if not r:
            raise UnableToCreateHiddenServiceException()
        if not r.hostname:
            raise HiddenServiceConfigurationDirectoryUnreadableException()
        return (config_id, r.hostname)

@app.route('/advertise')
def advertise():
    _, hostname = new_hidden_service(target_port=5000)
    return 'http://%s' % hostname

@app.route('/')
def index():
    _, hostname = new_hidden_service(target_port=8080)
    return 'http://%s' % hostname

@app.route('/ping')
def ping():
    return 'pong'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
