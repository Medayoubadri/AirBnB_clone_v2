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
    if number < 0:
        return False
    number = max(1, number) if number == 0 else number + 1

    local_archives = local('ls -1t versions', capture=True).split()
    for archive in local_archives[number:]:
        local(f'rm -rf versions/{archive}')

    releases_path = '/data/web_static/releases'
    remote_archives = run(f'ls -1t {releases_path}').split()
    web_static_dirs = [d for d in remote_archives
                       if d.startswith('web_static_')]
    for archive in web_static_dirs[number:]:
        run(f'rm -rf {releases_path}/{archive}')

    return True
