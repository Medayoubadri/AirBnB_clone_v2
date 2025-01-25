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


def deploy():
    """Creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
