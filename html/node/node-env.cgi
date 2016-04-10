#!/usr/bin/node
'use strict';
var evComponent = createEnvironmentVariable();

var header ='Content-type: text/html\n\n';

//Using ES6 Multiline string
var body =`<!doctype html>
<html lang="en">
<head>
<title>Node CGI Env Vars</title>
<style>
    table, th, td {
            border: 1px solid black;
    }
</style>
</head>
<body>
    <h3>Browser Env Table:</h3> ${evComponent.createBrowserEnv()}
    <hr>
    <h3>Server Env Table:</h3> ${evComponent.createServerEnv()}
</body>
</html>`;

console.log(header + body); // Server Response





/**
* A component like function that creates browser and server tables
*/
function createEnvironmentVariable(){
    var reBrowserVar = new RegExp('(^HTTP)|(^REQUEST)|(^QUERY)','i');
    var browserVars = {};
    var serverVars = {};

    for( let e in process.env){
        if(reBrowserVar.test(e)){
            browserVars[e]=process.env;
        } else {
            serverVars[e]=process.env;
        }
    }

    /**
    * Table Factory Helper
    */
    function createTable(envData){
        let data = '';
        for( let e in envData){
            data += '<tr><td>'+e+'</td><td>'+process.env[e]+'</td></tr>';
        }
        return '<table>'+data+'</table>';
    }

    /**
    * Create the browser env vars table
    */
    function createBrowserEnv(){ return createTable(browserVars); }

    /**
    * Create the server env vars table
    */
    function createServerEnv(){ return createTable(serverVars); }

    // Revealing Module Pattern
    return {
        createBrowserEnv: createBrowserEnv,
        createServerEnv: createServerEnv
    }
}
