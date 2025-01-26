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
    
    # Local cleanup
    local("ls -1t versions | tail -n +{} | xargs -I {{}} rm versions/{{}}".format(
        number + 1))
    
    # Remote cleanup
    path = "/data/web_static/releases"
    run("ls -1t {} | grep web_static | tail -n +{} | xargs -I {{}} rm -rf {}/{{}}".format(
        path, number + 1, path))
