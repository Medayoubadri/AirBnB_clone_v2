#!/usr/bin/python3
"""
Fabric script that distributes an archive to the web servers
"""

from fabric.api import env, put, run
import os.path

env.hosts = ['34.224.63.237', '52.86.3.5']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        folder_name = file_name.split(".")[0]
        path = "/data/web_static/releases/"

        put(archive_path, "/tmp/")
        run(f"mkdir -p {path}{folder_name}")
        run(f"tar -xzf /tmp/{file_name} -C {path}{folder_name}")
        run(f"rm -rf /data/web_static/releases/{file_name}")
        run(f"rm /tmp/{file_name}")
        run(f"mv {path}{folder_name}/web_static/* {path}{folder_name}/")
        run(f"rm -rf {path}{folder_name}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {path}{folder_name} /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception:
        return False
