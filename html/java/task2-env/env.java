//#!/usr/bin/java hello

import java.util.*;
import java.io.*;

class JavaEnv
{
  public static void main( String args[] )
  {
    System.out.println("Content-type: text/html\r\n\r\n");
  
    System.out.println("<!DOCTYPE html>" +
      "<html>" +
      "<head><title>Java CGI ENV Script</title></head>" +
      "<body>" +
      "<h1 align='center'>Environment Variables</h1><hr />" +
      "<h3>Browser Env Table:</h3>" +
      "<table border='1' style='width:100%'>" +
      "<tr>" +
      "<th>Variable Key:</th>" +
      "<th>Variable Value: </th>" +
      "</tr>");

    Map<String, String> env = System.getenv();
      for (String envName : env.keySet()) {
        if(envName.contains("HTTP")) {
          System.out.format("<tr><td><b>%s</b></td><td>%s</td></tr>", envName, env.get(envName));
        }
      }

    System.out.println("</table>" +
	                     "<h3>Server Env Table:</h3>" +
                       "<table border='1' style='width:100%'>" +
	                     "<tr>" +
			                 "<th>Variable Key:</th>" +
			                 "<th>Variable Value: </th>" +
	                     "</tr>");

    Map<String, String> env2 = System.getenv();
      for (String envName2 : env2.keySet()) {
        if(!envName2.contains("HTTP")) {
          System.out.format("<tr><td><b>%s</b></td><td>%s</td></tr>", envName2, env2.get(envName2));
        }
      }

    System.out.println("</table>" +
                       "</body>" +
                       "</html>");
    }
}
