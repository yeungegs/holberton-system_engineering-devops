# puppet script to debug web server failed requests
exec { 'increase limit on open files':
  command => '/bin/sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"- Hn\"/" /etc/default/nginx && /etc/init.d/nginx restart',
  }
