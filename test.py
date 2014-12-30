#!/usr/bin/env python

import os
from stem.control import Controller

def add_hidden_service(c):
    print controller.create_hidden_service(os.path.join(controller.get_conf('DataDirectory'), 'odon'), 80, target_port = 5000)

with Controller.from_port(port = 9051) as controller:

    controller.authenticate(password='salutlesamis')

    bytes_read = controller.get_info("traffic/read")
    bytes_written = controller.get_info("traffic/written")

    print "My Tor relay has read %s bytes and written %s." % (bytes_read, bytes_written)

    add_hidden_service(controller)
