#!/usr/bin/env bash
#Install Nginx
apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
new_txt="server_name _;\n\tlocation \/hbnb_static\/ {\n\talias \/data\/web_static\/current\/;\n\tautoindex off;\n\t}\n"
sed -i "s/server_name _;/$new_txt/" /etc/nginx/sites-available/default
service nginx restart
