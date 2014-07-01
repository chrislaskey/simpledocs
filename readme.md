Simple Docs
================================================================================

**Simple documentation for IT teams**

Version 1.2.0

Plain-text to HTML. Searchable. Responsive. Easy.

#### Plain-text Flat Files

Simple Docs is a thin web interface that mirrors flat files on a server.
Navigation mirrors file hierarchy. Markdown parser adds rich elements like
images, links, and code blocks.

#### Low Management

Uses existing system configuration, file permissions for write control, web
server for access control. No compilation jobs to run, no caches to clear, and
no database to configure.

#### Easy to Deploy

Powered by Python Flask. Deployable on any Linux server, whether its Debian
with Nginx, CentOS with Apache, or Arch with Gunicorn.


Deploy
================================================================================

Since Simple Docs is just a thin web interface built on top of Python Flask,
the only server requirements are a HTTP server with WSGI support.

A complete deployment example for CentOS with Apache and Mod_WSGI:

```sh
git clone https://github.com/chrislaskey/simpledocs /var/www/simpledocs
cd /var/www/simpledocs
vim app/config.py
./setup.sh
vim example-apache.conf
mv example-apache.conf /etc/httpd/conf.d/simpledocs.conf
service httpd restart
```


License
================================================================================

All code written by me is released under MIT license. See the attached
license.txt file for more information, including commentary on license choice.
