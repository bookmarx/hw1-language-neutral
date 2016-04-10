#!/usr/bin/python2.7

import cgi
import time
import random
print "Content-type: text/html\n\n"


timeStr = time.strftime("%c") # obtains current time

colors = ['aqua', 'black', 'blue', 'fuchsia', 'gray', 'green', 'lime', 'maroon', 'navy', 'olive', 'purple', 'red', 'silver', 'teal', 'white', 'yellow']
randColor = random.choice(colors)

print """
<!DOCTYPE html>
<html lang='en'>

<head>
<meta charset="UTF-8">
<title>Python CGI Script</title>
</head>

<body style="background-color:%s">""" % randColor

print """

  <h1> Hello World from CGI Python @ %s </h1>""" % timeStr
print """
</body>

</html>
"""
