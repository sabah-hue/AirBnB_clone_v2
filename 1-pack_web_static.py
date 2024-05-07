#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static
"""

from fabric import Connection
from datetime import datetime


def do_pack():
    """ generates a .tgz archive """
    servers = ["100.25.41.212", "100.25.103.239"]
    for server in servers:
        d_form = datetime.now().strftime("%Y%m%d%H%M%S")
        with Connection(host=server, user="ubuntu",
                        connect_kwargs={
                            "key_filename": "/root/.ssh/id_rsa"}) as c:
            c.local('mkdir -p versions')
            x = c.local("tar -czvf versions/web_static_{}.tgz web_static/"
                        .format(d_form))
            return x
