#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""

from fabric.api import env, cd, lcd, local, run
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

    local_path = "versions"
    if os.path.isdir(local_path):
        with lcd(local_path):
            archives = sorted(local("ls -1t", capture=True).split())
            [local(f"rm -f {archive}") for archive in archives[number:]]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if a.startswith("web_static_")]
        if number <= 0 or number >= len(archives):
            pass
        else:
            archives_to_delete = archives[:-number]
            for archive in archives_to_delete:
                run(f"rm -rf {archive}")
