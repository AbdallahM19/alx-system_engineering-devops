# we are testing how well our web server setup featuring Nginx is doing

exec { 'fix_nginx':
  provider => shell,
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  before  => Exec['restart_nginx']
}

-> exec { 'restart_nginx':
  provider => shell,
  command => 'sudo service nginx restart'
}
