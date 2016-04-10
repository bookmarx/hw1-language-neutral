//#!/usr/bin/java hello

import java.util.*;
import java.io.*;

class JavaEnv
{
    public static void main( String args[] )
    {
        System.out.println("Content-type: text/html\r\n\r\n");

        Map<String, String> env = System.getenv();
        for (String envName : env.keySet()) {
            System.out.format("%s=%s%n",
            envName,
            env.get(envName));
        }
    }


    // System.out.println("<!DOCTYPE html>" +
    //   "<html>" +
    //   "<head><title>Python CGI ENV Script</title></head>" +
    //   "<body>" +
    //   "<h1 align="center">Environment Variables</h1><hr />" +
    //   "<h3>Browser Env Table:</h3>" +
    //   "<table border="1" style="width:100%">" +
    //  	  "<tr>" +
    //     "<th>Variable Key:</th>" +
    //     "<th>Variable Value: </th>" +
    //     "</tr>");
    //
    //  System.out.println("</table>" +
    //    "</body>" +
    //    "</html>");

}
