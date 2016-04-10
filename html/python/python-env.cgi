#!/usr/bin/python

import os
import re
print "Content-type: text/html\r\n\r\n";
print """
<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset="UTF-8">
<title>Python CGI ENV Script</title>
<style>
    table, th, td {
            border: 1px solid black;
    }
</style>
</head>
<body>
  <h1>Environment Variables</h1><hr />
  <h3>Browser Env Table:</h3>
  <table>
	  <tr>
	    <th>Variable Key:</th>
	    <th>Variable Value: </th>		
	  </tr>
"""
pattern = re.compile("(^HTTP)|(^REQUEST)|(^QUERY)", re.IGNORECASE)
envVars = sorted(os.environ.keys())
for param in envVars:
	if pattern.match(param): 
		print "<tr><td><b>%20s</b></td><td>%s</td></tr>" % (param, os.environ[param])

print """
	</table>
	<h3>Server Env Table:</h3>
	<table>
		<tr>
			<th>Variable Key:</th>
			<th>Variable Value: </th>		
		</tr>
"""		

for param in envVars:
	if pattern.match(param): 
		pass
	else:	
		print "<tr><td><b>%20s</b></td><td>%s</td></tr>" % (param, os.environ[param])

print """
	</table>

</body>
</html> 
"""





 