import java.util.*; 
import java.io.*;

class hello
{
  public static void main( String args[] ) {
	System.out.println("Content-Type: text/html\n\n");

  Random randomGenerator = new Random();

  int randInt = randomGenerator.nextInt(15);
  
  privat String[] colors = {"aqua", "black", "blue", "fuchsia",
                            "gray", "green", "lime", "maroon",
                            "navy", "olive", "purple", "red",
                            "silver", "teal", "white", "yellow"};

  System.out.println("<html> 
  <head><title>Java CGI Script</title></head>
  <body bgcolor=color[randInt]>");

  Date d = new Date();
  DateFormat df = DateFormat.getDateInstance();
  System.out.println(df.format(d));
  
  }
}
