#!/usr/bin/python3
""" Create .tgz file based in content of web_static """
from fabric.api import local
from datetime import datetime


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
