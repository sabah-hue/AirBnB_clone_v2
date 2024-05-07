#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static
"""

from fabric import Connection
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static directory.

    This function creates a .tgz archive of the web_static directory,
    naming it with the current date and time.
    The archive is saved in the 'versions' directory on the local machine.

    Returns:
        The result of the tar command execution.
    """
    with Connection(host="100.25.41.212", user="ubuntu",
                    connect_kwargs={
                        "key_filename": "/root/.ssh/id_rsa"}) as c:
        """ connect to host"""
        c.local('mkdir -p versions')
        d_form = datetime.now().strftime("%Y%m%d%H%M%S")
        x = c.local(f"tar -czvf versions/web_static_{d_form}.tgz web_static/")
        return x


if __name__ == "__main__":
    """run in terminal"""
    do_pack()
