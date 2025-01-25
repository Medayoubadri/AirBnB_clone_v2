# Puppet manifest to set up web servers for deployment of web_static

# Install Nginx
package { 'nginx':
  ensure   => 'present',
  provider => 'apt',
}

file { '/data':
  ensure  => 'directory'
}
file { '/data/web_static':
  require => File['/data'],
}
file { '/data/web_static/releases':
  require => File['/data/web_static'],
}
file { '/data/web_static/shared':
  require => File['/data/web_static/releases'],
}
file { '/data/web_static/releases/test':
  require => File['/data/web_static/shared'],
}
file { '/data/web_static/releases/test/index.html':
  require => File['/data/web_static/releases/test'],
}
file { '/data/web_static/releases/test':
}
file { '/data/web_static/current':
  require => File['/data/web_static/releases/test/index.html'],
}
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => "<html>\n  <head>\n  </head>\n  <body>\n    ALX\n  </body>\n</html>\n"
}
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force  => true
}

file_line { 'nginx_configuration':
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => "\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n",
  notify => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File_line['nginx_configuration'],
}
