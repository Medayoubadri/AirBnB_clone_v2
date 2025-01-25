#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo, using the function do_pack.
"""

import os
import time
from fabric.api import local


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        local("mkdir -p versions")

        current_time = time.strftime("%Y%m%d%H%M%S")
        output = f"versions/web_static_{current_time}.tgz"

        local(f"tar -cvzf {output} web_static")

        return output
    except Exception:
        return None


if __name__ == "__main__":
    result = do_pack()
    if result:
        print(
            f"web_static packed: {result} -> {os.path.getsize(result)} Bytes")
    else:
        print("Packing web_static failed")
