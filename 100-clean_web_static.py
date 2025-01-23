#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""

from fabric.api import env, cd, local, run

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
        return

    with cd('/data/web_static/releases'):
        archives = sorted(run('ls -tr').split())
        archives = [a for a in archives if a.startswith('web_static_')]
        for archive in archives[:-number or -1]:
            run(f'rm -rf {archive}')

    with cd('versions'):
        archives = sorted(local('ls -tr', capture=True).split())
        archives = [a for a in archives if a.startswith('web_static_')]
        for archive in archives[:-number or -1]:
            local(f'rm -rf {archive}')
