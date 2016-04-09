#!/usr/bin/ruby

time = Time.new
colors = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"]
randColor = colors.choice

puts "Content-type: text/html\n\n"
puts "<html>\n<head>\n<title>Hello CGI World</title>\n</head>\n"
puts "<body bgcolor= %s>\n" %randColor.inspect
puts "<h1>Hello World from CGI Ruby @ %s </h1>\n" %time.inspect
puts "</body>\n</html>"
