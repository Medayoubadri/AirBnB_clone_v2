#!/usr/bin/python3
"""
Fabric script that distributes an archive to the web servers
"""

from fabric.api import env, put, run
from os.path import exists

env.hosts = ['34.224.63.237', '52.86.3.5']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        folder_name = file_name.split(".")[0]
        path = "/data/web_static/releases/"

        put(archive_path, "/tmp/")
        run("mkdir -p {}{}".format(path, folder_name))
        run("tar -xzf /tmp/{} -C {}{}".format(file_name, path, folder_name))
        run("rm /tmp/{}".format(file_name))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, folder_name))
        run("rm -rf {}{}/web_static".format(path, folder_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, folder_name))
        print("New version deployed!")
        return True
    except Exception:
        return False
