import java.util.*; 
import java.io.*;
import java.text.SimpleDateFormat;
import java.text.DateFormat;

class hello
{
  public static void main( String args[] ) {
	System.out.println("Content-Type: text/html\n\n");

  Random randomGenerator = new Random();

  int randInt = randomGenerator.nextInt(15);
  
  String[] colors = {"aqua", "black", "blue", "fuchsia",
                     "gray", "green", "lime", "maroon",
                     "navy", "olive", "purple", "red",
                     "silver", "teal", "white", "yellow"};

  


  System.out.println("<html>"+ 
  "<head><title>Java CGI Script</title></head>" +
  "<body bgcolor='"+colors[randInt]+"'>");



  Date d = new Date();
  SimpleDateFormat df = new SimpleDateFormat("EEE MMM d HH:mm:ss yyyy");
  String formattedDate = df.format(d);

  System.out.println("<h1> Hello World from CGI Java @ " +
                     formattedDate +
                     "</h1>");
  }
}
