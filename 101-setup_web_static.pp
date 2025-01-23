# Puppet manifest to set up web servers for deployment of web_static

# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Create necessary directories
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => "<html>\n  <head>\n  </head>\n  <body>\n    ALX\n  </body>\n</html>\n",
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Create or recreate symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force  => true,
}

# Update Nginx configuration
file_line { 'nginx_configuration':
  path  => '/etc/nginx/sites-available/default',
  after => 'server_name _;',
  line  => "\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n",
}

# Restart Nginx
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File_line['nginx_configuration'],
}
