# Create a server and configure it

exec { 'Update_system':
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'sudo apt-get update -y',
  provider => 'shell',
  returns  => [0,1],
}

exec { 'Install_nginx':
  require  => Exec['Update_system'],
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'sudo apt-get install nginx -y',
  provider => 'shell',
  returns  => [0,1],
}

exec { 'new_dir_1':
  require  => Exec['Install_nginx'],
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'mkdir -p /data/web_static/releases/test/',
  provider => 'shell',
  returns  => [0,1],
}

exec { 'new_dir_2':
  require  => Exec['new_dir_1'],
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'mkdir -p /data/web_static/shared/',
  provider => 'shell',
  returns  => [0,1],
}


exec { 'new_html':
  require  => Exec['new_dir_2'],
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'echo "Holberton School" > /data/web_static/releases/test/index.html',
  provider => 'shell',
  returns  => [0,1],
}

exec { 'create_ln':
  require  => Exec['new_html'],
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => 'shell',
  returns  => [0,1],
}


exec { 'chown_data':
  require  => Exec['create_ln'],
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'chown -R ubuntu:ubuntu /data/',
  provider => 'shell',
  returns  => [0,1],
}

exec { 'add_default':
  require  => Exec['chown_data'],
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'sed -i "s/server_name _;/server_name _;\n\tlocation \/hbnb_static\/ {\n\talias \/data\/web_static\/current\/;\n\tautoindex off;\n\t}\n/" /etc/nginx/sites-available/default',
  provider => 'shell',
  returns  => [0,1],
}

exec { 'Restart_web_server':
  require  => Exec['add_default'],
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'sudo service nginx restart',
  provider => 'shell',
  returns  => [0,1],
}
