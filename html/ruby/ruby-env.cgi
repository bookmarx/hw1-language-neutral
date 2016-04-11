#!/usr/bin/ruby
require 'cgi'

puts "Content-type: text/html\n\n"
puts "<!DOCTYPE html>
<html>
<head><title>Ruby CGI ENV Script</title></head>
<body>
  <h1 align='center'>Environment Variables</h1><hr/>
  <h3>Browser Env Table:</h3>
  <table border='1' style='width:100%'>
	  <tr>
	    <th>Variable Key:</th>
	    <th>Variable Value: </th>
	  </tr>
"
puts ENV['REQUEST_URI']

ENV.each do |key,value|
  if key.include? "HTTP"
    puts "<tr><td><b>%20s</b></td><td>%s</td></tr>"  %[key, value]
  end
end

puts "
	</table>
	<h3>Browser Env Table:</h3>
	<table border='1' style='width:100%'>
		<tr>
			<th>Variable Key:</th>
			<th>Variable Value: </th>
		</tr>
"
ENV.each do |key,value|
  if !key.include? "HTTP"
    puts "<tr><td><b>%20s</b></td><td>%s</td></tr>"  %[key, value]
  end
end

puts "
  </table>

</body>
</html>
"
