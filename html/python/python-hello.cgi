import cgi
import cgitb; cgitb.enable()  
import time
import random
print "Content-type: text/html"
print

timeStr = time.strftime("%c") # obtains current time

colors = ['aqua', 'black', 'blue', 'fuchsia', 'gray', 'green', 'lime', 'maroon', 'navy', 'olive', 'purple', 'red', 'silver', 'teal', 'white', 'yellow']
randColor = random.choice(colors)

print """
<html>

<head><title>Python CGI Script</title></head>

<body bgcolor='{randColor}'>

  <h1> Hello World from CGI Python @ {timeStr} </h1>
</body>

</html>  
"""
