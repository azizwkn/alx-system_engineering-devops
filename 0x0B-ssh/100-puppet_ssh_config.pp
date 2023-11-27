# Sets up client SSH configuration file using Puppet

file {'/etc/ssh/ssh_config':
  ensure  => file,
  content => "IdentityFile ~/.ssh/school\nPasswordAuthentication no\n",
}
