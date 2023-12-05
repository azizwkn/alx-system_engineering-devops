#!/usr/bin/env bash
# configures a brand new Ubuntu machine to the requirements:
# the name of the custom HTTP header must be X-Served-By
# the value of the HTTP header is the hostname of the running server.

# Update package list
exec { 'apt_update':
  command => 'apt-get update',
  path    => '/usr/bin',
}

# Install Nginx
package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt_update'],
}

# Configure Nginx with custom HTTP response header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location / {
        # Add custom HTTP response header
        add_header X-Served-By ${::hostname};
    }
}
",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Enable Nginx to start on boot
service { 'nginx':
  ensure => 'running',
  enable => true,
}
