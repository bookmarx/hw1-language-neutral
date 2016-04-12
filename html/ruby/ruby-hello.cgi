#!/usr/bin/ruby

time = Time.new
colors = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"]
randColor = colors.sample

puts "Content-type: text/html\n\n"
puts "<!DOCTYPE html><html>\n<head>\n<meta charset='UTF-8'><title>Hello CGI World</title>\n</head>\n"
puts "<body style='background-color: %s'>\n" %randColor
puts "<h1>Hello World from CGI Ruby @ %s </h1>\n" %time.inspect
puts "</body>\n</html>"
