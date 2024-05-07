#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static
"""

from fabric.operations import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static directory.

    This function creates a .tgz archive of the web_static directory,
    naming it with the current date and time.
    The archive is saved in the 'versions' directory on the local machine.

    Returns:
        The result of the tar command execution.
    """
    local('mkdir -p versions')
    d_form = datetime.now().strftime("%Y%m%d%H%M%S")
    x = local(f"tar -czvf versions/web_static_{d_form}.tgz web_static/")
    if x.failed:
        return None
    else:
        return x
        d_size = os.path.getsize(x)
        print(f"web_static packed: {x} -> {d_size}Bytes")
