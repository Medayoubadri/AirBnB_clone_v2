#!/usr/bin/python3
"""
Fabric script that distributes an archive to the web servers
"""

from fabric.api import env, put, run
from os.path import exists
import os.path

env.hosts = ['34.224.63.237', '52.86.3.5']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    file_name = archive_path.split("/")[-1]
    path = "/data/web_static/releases/"
    folder_name = file_name.split(".")[0]

    if put(archive_path, "/tmp/").failed is True:
        return False
    if run(f"rm -rf /data/web_static/releases/{file_name}").failed is True:
        return False
    if run(f"mkdir -p {path}{folder_name}").failed is True:
        return False
    if run(
        f"tar -xzf /tmp/{file_name} -C {path}{folder_name}"
        ).failed is True:
        return False
    if run(f"rm /tmp/{file_name}").failed is True:
        return False
    if run(
        f"mv {path}{folder_name}/web_static/* {path}{folder_name}/"
        ).failed is True:
        return False
    if run(f"rm -rf {path}{folder_name}/web_static").failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run(f"ln -s {path}{folder_name} /data/web_static/current").failed is True:
        return False
    print("New version deployed!")
    return True
