#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to the web servers
"""

from fabric.api import env, local, put, run, runs_once
from datetime import datetime
from os.path import exists, isdir

env.hosts = ['34.224.63.237', '52.86.3.5']


@runs_once
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
        file_name = archive_path.split("/")[-1]
        folder_name = file_name.split(".")[0]
        path = "/data/web_static/releases/"

        put(archive_path, "/tmp/")
        run(f"mkdir -p {path}{folder_name}")
        run(f"tar -xzf /tmp/{file_name} -C {path}{folder_name}")
        run(f"rm /tmp/{file_name}")
        run(f"mv {path}{folder_name}/web_static/* {path}{folder_name}/")
        run(f"rm -rf {path}{folder_name}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {path}{folder_name} /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """Creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
