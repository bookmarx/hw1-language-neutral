//#!/usr/bin/java hello

import java.util.*; 
import java.io.*;

class javaenv
{
  public static void main( String args[] )
  {
    System.out.println("Content-type: text/html\r\n\r\n");
    System.out.println("<!DOCTYPE html>" +
      "<html>" +
      "<head><title>Python CGI ENV Script</title></head>" +
      "<body>" +
      "<h1 align="center">Environment Variables</h1><hr />" +
      "<h3>Browser Env Table:</h3>" +
      "<table border="1" style="width:100%">" +
  	  "<tr>" +
	    "<th>Variable Key:</th>" +
	    "<th>Variable Value: </th>" +		
	    "</tr>");
/*  From python-env.cgi */
/*
      "envVars = sorted(os.environ.keys())" +
      "for param in envVars:"
        "if "HTTP" in param:"
	   print "<tr><td><b>%20s</b></td><td>%s</td></tr>" % (param, os.environ[param])
           print """
	</table>
	<h3>Server Env Table:</h3>
	<table border="1" style="width:100%">
		<tr>
			<th>Variable Key:</th>
			<th>Variable Value: </th>		
		</tr>
"""		

for param in envVars:
	if "HTTP" not in param: 
		print "<tr><td><b>%20s</b></td><td>%s</td></tr>" % (param, os.environ[param])
*/
     System.out.println("</table>" +
       "</body>" +
       "</html>");
  }
}
