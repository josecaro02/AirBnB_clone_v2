#!/usr/bin/python3
""" Create .tgz file based in content of web_static """
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['35.231.235.242', '35.175.190.73']


def do_pack():
    try:
        local("mkdir -p versions/")
        date = datetime.now()
        actual_date = date.strftime("%Y%m%d%H%M%S")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(actual_date))
        return("web_static_{}".format(actual_date))
    except:
        return (None)


def do_deploy(archive_path):
    try:
        put(archive_path, "/tmp/")
        base_name = os.path.basename(archive_path)
        file_name = os.path.splitext(base_name)[0]
        run("mkdir -p /data/web_static/releases/{}".format(file_name))
        run("tar -zxf /tmp/{} -C /data/web_static/releases/{}".
            format(base_name, file_name))
        run("rm /tmp/{}".format(base_name))
        dir_rel = "/data/web_static/releases/"
        run("mv {}{}/web_static/* {}{}".
            format(dir_rel, file_name, dir_rel, file_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file_name))
        run("rm /data/web_static/current")
        run("ln -sf /data/web_static/releases/{} /data/web_static/current"
            .format(file_name))
        return(True)
    except Exception as e:
        print(e)
        return(False)
