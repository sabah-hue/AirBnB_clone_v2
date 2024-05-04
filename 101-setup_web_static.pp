# Using Puppet, sets up web servers for the deployment of web_static
exec { 'install_nginx':
    command  => 'sudo apt-get -y update;
    sudo apt-get -y install nginx;
    sudo mkdir -p /data/web_static/releases/test/;
    sudo echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
    </html>" > /data/web_static/releases/test/index.html;
    sudo mkdir -p /data/web_static/shared/;
    sudo ln -sf /data/web_static/releases/test/ /data/web_static/current;
    sudo chown -R ubuntu:ubuntu /data/;
    sudo sed -i "50 i location /hbnb_static {\n\talias /data/web_static/current;\n}" /etc/nginx/sites-enabled/default;
    sudo service nginx restart',
    provider => shell,
}
