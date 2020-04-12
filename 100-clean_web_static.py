#!/usr/bin/python3
""" Create .tgz file based in content of web_static """
from fabric.api import *
from datetime import datetime
import os
from glob import glob

env.hosts = ['35.231.235.242', '35.175.190.73']


def do_pack():
    """ Pack file in servers with extension .tgz """
    try:
        local("mkdir -p versions/")
        date = datetime.now()
        actual_date = date.strftime("%Y%m%d%H%M%S")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(actual_date))
        return("versions/web_static_{}.tgz".format(actual_date))
    except:
        return (None)


def do_deploy(archive_path):
    """ Deploy package in servers """
    try:
        if not(os.path.exists(archive_path)):
            return False
        put(archive_path, "/tmp/")
        base_name = os.path.basename(archive_path)
        file_name = os.path.splitext(base_name)[0]
        run("mkdir -p /data/web_static/releases/{}".format(file_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".
            format(base_name, file_name))
        run("rm /tmp/{}".format(base_name))
        dir_rel = "/data/web_static/releases/"
        run("mv {}{}/web_static/* {}{}".
            format(dir_rel, file_name, dir_rel, file_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(file_name))
        print("New version deployed!")
        return(True)
    except:
        return(False)


def deploy():
    """ Pack and deploy package in servers """
    base_name = do_pack()
    if base_name is None:
        return (False)
    return (do_deploy(base_name))


def do_clean(number=0):
    number = int(number)
    if number == 0:
        number == 2
    else:
        number +=1
    local("cd versions ; ls -t | tail -n +{} | xargs rm ".format(number))
    location="/data/web_static/releases"
    run("cd {} ; ls -t | tail -n +{} | xargs rm ".format(location, number))
