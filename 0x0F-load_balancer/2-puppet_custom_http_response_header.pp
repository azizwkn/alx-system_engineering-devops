#!/usr/bin/env bash
# automate the task of creating a custom HTTP header response
# configures a brand new Ubuntu machine to the requirements:
# the name of the custom HTTP header must be X-Served-By
# the value of the HTTP header is the hostname of the running server

exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package {'nginx':
  ensure => 'present',
}
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}
-> exec {'run':
  command => '/usr/sbin/service nginx restart',
}
