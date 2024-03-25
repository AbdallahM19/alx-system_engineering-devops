# Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task
# we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.

$file_ssh = '/etc/ssh/ssh_config';

file_line { 'Turn off passwd auth':
    ensure => 'present',
    path   => $file_ssh,
    line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
    ensure => 'present',
    path   => $file_ssh,
    line   => 'IdentityFile ~/.ssh/school',
}
