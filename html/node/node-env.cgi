#!/usr/bin/node

var header ="Content-type: application/json\n\n";
var body = process.env; 
console.log(header + JSON.stringify(body))
