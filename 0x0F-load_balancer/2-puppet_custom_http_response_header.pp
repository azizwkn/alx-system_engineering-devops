#!/usr/bin/env bash
# configures a brand new Ubuntu machine to the requirements:
# the name of the custom HTTP header must be X-Served-By
# the value of the HTTP header is the hostname of the running server.

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html':
  ensure => directory,
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => '
    server {
      listen 80 default_server;
      listen [::]:80 default_server;
      add_header X-Served-By $hostname;
      root /var/www/html;
      index index.html index.htm;

      location /redirect_me {
        return 301 https//youtube.com/;
      }

      error_page 404 /404.html;
      location /404 {
        root /var/www/html;
        internal;
      }
    }
  ',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
