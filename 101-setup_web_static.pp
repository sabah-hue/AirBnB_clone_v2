# Using Puppet, sets up web servers for the deployment of web_static
package { 'nginx':
    ensure   => 'present',
    provider => 'apt',
}

file { '/data':
    ensure  => 'directory'
}

file { '/data/web_static':
    ensure => 'directory'
}

file { '/data/web_static/releases':
    ensure => 'directory'
}

file { '/data/web_static/releases/test':
    ensure => 'directory'
}

file { '/data/web_static/shared':
    ensure => 'directory'
}

file { '/data/web_static/releases/test/index.html':
    ensure  => 'present',
    content => 'Holberton School'
}

file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test'
}

exec { 'install_nginx':
    command  => 'sudo chown -R ubuntu:ubuntu /data/;
    sed -i "50 i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}" /etc/nginx/sites-enabled/default;
    sudo service nginx restart',
    provider => shell,
}
