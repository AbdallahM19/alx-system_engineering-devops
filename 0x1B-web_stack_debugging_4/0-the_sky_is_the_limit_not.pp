#!/usr/bin/env bash
# we are testing how well our web server setup featuring Nginx is doing

{ 'fix_nginx':
  provider => shell,
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  before  => Exec['restart_nginx']
}

{ 'restart_nginx':
  provider => shell,
  command => 'sudo service nginx restart'
}
