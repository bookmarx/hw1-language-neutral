#!/usr/bin/ruby
require 'cgi'

puts "Content-type: text/html\n\n"
puts "<!DOCTYPE html>
<html>
<head>
<meta charset='UTF-8'>
<title>Ruby CGI ENV Script</title>
<style>
    table, th, td {
            border: 1px solid black;
    }
</style>
</head>
<body>
  <h1>Environment Variables</h1><hr/>
  <h3>Browser Env Table:</h3>
  <table>
	  <tr>
	    <th>Variable Key:</th>
	    <th>Variable Value: </th>
	  </tr>
"
#puts ENV['REQUEST_URI']
#pattern = "(^HTTP)|(^REQUEST)|(^QUERY)"
pattern = Regexp.union(['HTTP', 'REQUEST', 'QUERY'])
keys = ENV.each_key.sort
for params in keys
  if pattern.match(params)
    puts "<tr><td><b>%20s</b></td><td>%s</td></tr>"  %[params, ENV[params]]
  end
end

puts "
	</table>
	<h3>Server Env Table:</h3>
	<table>
		<tr>
			<th>Variable Key:</th>
			<th>Variable Value: </th>
		</tr>
"
for params in keys
  if !pattern.match(params)
    puts "<tr><td><b>%20s</b></td><td>%s</td></tr>"  %[params, ENV[params]]
  end
end

puts "
  </table>

</body>
</html>
"
