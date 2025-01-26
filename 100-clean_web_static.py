#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""

from fabric.api import env, lcd, cd, local, run
import os

env.hosts = ['34.224.63.237', '52.86.3.5']


def do_clean(number=0):
    """
    Deletes out-of-date archives
    Args:
        number (int): The number of archives to keep.
        If number is 0 or 1, keeps only the most recent archive.
        If number is 2, keeps the most and second most recent archives, etc.
    """
    number = int(number)
    if number < 1:
        number = 1

    with lcd("versions"):
        archives = local("ls -1t", capture=True).split()
        to_delete = archives[number:]
        for archive in to_delete:
            local(f"rm -f {archive}")

    with cd("/data/web_static/releases"):
        archives = run("ls -1t").split()
        web_static_archives = [a for a in archives if a.startswith("web_static_")]
        to_delete = web_static_archives[number:]
        for archive in to_delete:
            run(f"rm -rf {archive}")
