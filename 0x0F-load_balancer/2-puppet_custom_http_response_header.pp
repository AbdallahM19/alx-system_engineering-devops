# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

exec { 'update_files_system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update_files_system']
}

file {'/var/www/html/index.html':
  content => 'Hello World!'
}

exec {'redirect':
  command  => 'sed -i "24i\trewrite ^/redirect https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

exec {'add_custom_header':
  command  => 'sed -i "25i\tadd_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

service {'nginx':
  ensure  => running,
  require => Package['nginx']
}
