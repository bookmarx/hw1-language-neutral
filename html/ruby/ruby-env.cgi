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
	<h3>Browser Env Table:</h3>
	<table border='1' style='width:100%'>
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
