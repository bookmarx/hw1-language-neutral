#!/usr/bin/ruby

puts "Content-type: text/html\n\n"
puts "<!DOCTYPE html>
<html>
<head><title>Python CGI ENV Script</title></head>
<body>
  <h1 align="center">Environment Variables</h1><hr />
  <h3>Browser Env Table:</h3>
  <table border="1" style="width:100%">
	  <tr>
	    <th>Variable Key:</th>
	    <th>Variable Value: </th>
	  </tr>
"
