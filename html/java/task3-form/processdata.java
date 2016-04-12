import java.util.*;
import java.io.*;
import javax.servlet;

class JavaForm 
{
  public static void main( String args[] )
  {
    System.out.println("Content-type: text/html\r\n\r\n");

    System.out.println("<!DOCTYPE html>" +
      "<html lang='en'>" +
      "<head>" +
	    "<meta charset='UTF-8'>" +
	    "<title>Java CGI Form</title>" +
      "</head>" +
      "<body>" +
	    "<h1>Java Process Data</h1><hr />");

    String username;
    String password;
    int magicnum;


    System.out.println ("</body>" + "</html>");
  }
}


/*
// Create instance of FieldStorage 
form = cgi.FieldStorage() 

// Get data from fields
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
	<h1>Python Process Data</h1><hr />
"""
for i in range(0,int(magicnum)):
	print "<h1>Hello %s with a password of %s!</h1>" % (username, password)

print"""
</body>
</html>
"""
*/
