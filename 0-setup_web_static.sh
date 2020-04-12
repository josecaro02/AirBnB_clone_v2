#!/usr/bin/env bash
#Install Nginx
apt-get update
apt-get install -y nginx
#Create folder /data/web_static/releases
mkdir -p /data/web_static/releases/test
#Create folder /data/web/shared
mkdir -p /data/web_static/shared

#Give permissions to /data/folder
chown -R ubuntu:ubuntu /data/

#Create fake HTML file
fake_html="<html>
	<head>
        </head>
	<body>Holberton School
        </body>
</html>
"
echo "$fake_html" > /data/web_static/releases/test/index.html
# Create Symbolic link

ln -sf /data/web_static/releases/test/ /data/web_static/current

#Update NGINX configuration to serve /data/web_static/current/ to hbnb_static
new_txt="server_name _;\n\tlocation \/hbnb_static\/ {\n\talias \/data\/web_static\/current\/;\n\tautoindex off;\n\t}\n"
sed -i "s/server_name _;/$new_txt/" /etc/nginx/sites-available/default

#Restart nginx
service nginx restart
