#!/usr/bin/python3
"""
Fabric script that distributes an archive to the web servers.
"""

from fabric.api import env, put, run
from os.path import exists

env.hosts = ['34.224.63.237', '52.86.3.5']


def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        folder_name = file_name.split(".")[0]
        path = f"/data/web_static/releases/{folder_name}"

        if put(archive_path, f"/tmp/{file_name}").failed:
            return False

        if run(f"mkdir -p {path}").failed:
            return False

        if run(f"tar -xzf /tmp/{file_name} -C {path}").failed:
            return False

        if run(f"rm /tmp/{file_name}").failed:
            return False

        if run(f"mv {path}/web_static/* {path}/").failed:
            return False

        if run(f"rm -rf {path}/web_static").failed:
            return False

        if run("rm -rf /data/web_static/current").failed:
            return False

        if run(f"ln -s {path} /data/web_static/current").failed:
            return False

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
