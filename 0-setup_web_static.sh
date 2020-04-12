#!/usr/bin/env bash
#Install Nginx
sudo apt-get install nginx
#Create folder /data/web_static/releases
sudo mkdir -p /data/web_static/releases/test
#Create folder /data/web/shared
sudo mkdir -p /data/web_static/shared
#Create fake HTML file
fake_html="<html>
	<head>\n\t</head>
	<body>\n\t\tHolberton School\n\t</body>
</html>
"
echo "$fake_html" > /data/web_static/releases/test/index.html
# Create Symbolic link

sudo ln -sf /data/web_static/releases/test /data/web_static/current

#Give permissions to /data/folder
sudo chown -R ubuntu:ubuntu data/

#Update NGINX configuration to serve /data/web_static/current/ to hbnb_static
base_txt="server_name _;"
new_txt="server_name _;\n\tlocation \/hbnb_static {\n\talias  \/data\/web_static\/current;\n\t}"
sudo sed -i "s/$base_text/$new_txt/" /etc/nginx/sites-available/default
