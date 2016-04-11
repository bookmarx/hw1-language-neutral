#!/usr/bin/ruby
require 'cgi'
cgi = CGI.new
h = cgi.params

username = h['username']
password = h['password']
magicnum = h['magicnum']
num = magicnum.pop.to_i

puts "Content-type:text/html\r\n\r\n"
puts "
<!DOCTYPE html>
<html lang='en'>
<head>
	<meta charset='UTF-8'>
	<title>Ruby CGI Form</title>
</head>
<body>
	<h1>Ruby Process Data</h1>
  "

for i in 1..num do
  puts "<h1>Hello %s with a password of %s!</h1>" %[username, password]
end

#puts "<h2> %s WHAT!!" %magicnum
puts "
</body>
</html>
"
