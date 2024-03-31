# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

exec { 'update_system':
    command => '/usr/bin/apt-get update',
}

-> package { 'nginx':
    ensure  => 'present',
    require => Exec['update_system']
}

file {'/var/www/html/index.html':
    content => 'Hello World!'
}

-> header_line { 'add_custom_header':
    path  => '/etc/nginx/nginx.conf',
    match => 'http {',
    line  => "http {\n\tadd_header X-Served-By \${hostname};",
}

-> exec {'nginx_run':
    command => '/usr/sbin/service nginx restart',
}
