# Using Puppet, create a file in /tmp.
package { 'Flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}
