#!/usr/bin/python2.7

import cgi 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
username = form.getvalue('username')
password  = form.getvalue('password')
magicnum = form.getvalue('magicnum')


print "Content-type:text/html\r\n\r\n"
print """
<!DOCTYPE html>
<html lang='en'>
<head>
	<meta charset="UTF-8">
	<title>Python CGI Form</title>
</head>
<body>
	<h1 align="center">Python Process Data</h1><hr />
"""
for i in range(0,int(magicnum)):
	print "<h1>Hello %s with a password of %s!</h1>" % (username, password)

print"""
</body>
</html>
"""