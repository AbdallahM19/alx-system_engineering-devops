# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

exec { 'update_system':
    command => '/usr/bin/apt-get update',
}

package { 'nginx':
    ensure  => 'present',
    require => Exec['update_system']
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

file_line { 'add_custom_header':
    path     => '/etc/nginx/nginx.conf',
    ensure   => 'present',
    command  => 'sudo sed -i '26i\tadd_header X-Served-By "$hostname";' /etc/nginx/sites-available/default'
    notify   => Service['nginx'],
    require  => Package['nginx']
}

service { 'nginx':
    ensure  => running,
    require => Package['nginx']
}
