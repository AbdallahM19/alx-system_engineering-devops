# Nginx should be listening on port 80
# When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
# The redirection must be a “301 Moved Permanently”
# Your answer file should be a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements

exec {'install':
    command => 'sudo apt-get update',
}

package { 'nginx':
    ensure  => 'installed',
    require => Exec['install']
}

file { '/var/www/html/index.html':
    ensure  => file,
    content => "Hello World!\n",
}

exec {'redirection':
    command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
    provider => shell,
}

service { 'nginx':
    ensure => running,
    enable => package['nginx']
}
