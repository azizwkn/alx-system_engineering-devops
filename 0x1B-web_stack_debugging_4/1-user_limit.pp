# Enable the user holberton to login and open files without error.

# Increase hard file limit for Holberton user.
exec { 'increase_hard_file_limit_for_user_holberton':
  command => "sed -i '/^holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for Holberton user.
exec { 'increase_soft_file_limit_for_user_holberton':
  command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

