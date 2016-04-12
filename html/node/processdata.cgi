#!/usr/bin/node
'use strict';
var querystring = require('querystring');

var header ='Content-type: text/html';
console.log(header);


if( process.env.REQUEST_METHOD==='GET' ) {
	var data = querystring.parse(process.env['QUERY_STRING']);
	printBody(data.username, data.password, data.magicnum);

} else if (process.env.REQUEST_METHOD==='POST') {
	var data = '';
	process.stdin.on('data', function(chunk) {
		data+=chunk;
	});

	process.stdin.on('end', function() {
		var d = querystring.parse(data)
		printBody(d.username, d.password, d.magicnum);
	});
}

function printBody(username, password, n){
	if(!username || !password || !n){
		return console.log('Status: 400 Bad Request', '\n\n 400 Bad Request: Username or Password was invalid.')
	}

	var helloString = echoHello(username, password, n);

	//Using ES6 Multiline string
	var body =`<!doctype html>
	<html lang="en">
	<head>
	<title>Node CGI Process Data</title>
	<style>
	</style>
	</head>
	<body>
		<h1>Node Process Data</h1>
		${helloString}
	</body>
	</html>`;

	console.log('\n\n',body);
}


function echoHello(username, password, n){
	var helloString = '';
	for(var i=0; i<n; i++) {
		helloString += `<h1>Hello ${username} with a password of ${password}!</h1>`;
	}
	return helloString;
}
