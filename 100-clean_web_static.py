#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""

from fabric.api import env, cd, local, run
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
        return

    local_path = os.path.join(os.path.dirname(__file__), 'versions')
    if os.path.isdir(local_path):
        with cd(local_path):
            archives = sorted(local('ls -t').split())
            [local('rm -rf {}'.format(a)) for a in archives[number:]
             if a.startswith('web_static_')]

    with cd('/data/web_static/releases'):
        archives = sorted(run('ls -t').split())
        [run('rm -rf {}'.format(a)) for a in archives[number:]
         if a.startswith('web_static_')]

    print(len(archives[:number] if number > 0 else archives[:1]))
