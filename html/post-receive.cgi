#!/bin/sh
git --git-dir=/root/hw1-language-neutral/.git fetch --all
git --git-dir=/root/hw1-language-neutral/.git reset --hard origin/master
git --work-tree=/var/www/ --git-dir=/root/hw1-language-neutral/.git checkout -f
chmod 775 /var/www/html/post-receive.cgi

echo "Content-type: text/html\n\n OK";
