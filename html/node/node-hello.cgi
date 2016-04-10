#!/usr/bin/node

var header ='Content-type: text/html\n\n';

//Using ES6 Multiline string
var body =`<!doctype html>
<html lang="en">
<head>
    <title>Hello CGI World</title>
</head>
<body style="background-color: ${getRandomColor()}">
    <h1>Hello World from NodeJS @  ${new Date()} </h1>
</body>
</html>`;

console.log(header + body);

/**
 * Gets a random color
 */
function getRandomColor(){
    var colors = ['aqua', 'black', 'blue', 'fuchsia', 'gray', 'green', 'lime', 'maroon', 'navy', 'olive', 'purple', 'red', 'silver', 'teal', 'white', 'yellow'];
    var colorNum = Math.floor(Math.random()*colors.length);
    return colors[colorNum];
}
