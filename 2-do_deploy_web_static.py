#!/usr/bin/python3
"""
Fabric script that distributes an archive to the web servers
"""

from fabric.api import env, put, local, run
from os.path import exists, isdir
from datetime import datetime
import os

env.hosts = ['34.224.63.237', '52.86.3.5']


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        fil_nm = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(fil_nm))
        return fil_nm
    except Exception:
        return None


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = os.path.basename(archive_path)
        folder_name = file_name.split(".")[0]
        path = "/data/web_static/releases/"

        put(archive_path, "/tmp/")
        run(f"mkdir -p {path}{folder_name}/")
        run(f"tar -xzf /tmp/{file_name} -C {path}{folder_name}/")
        run(f"rm /tmp/{file_name}")
        run(f"mv {path}{folder_name}/web_static/* {path}{folder_name}/")
        run(f"rm -rf {path}{folder_name}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {path}{folder_name}/ /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception:
        return False
