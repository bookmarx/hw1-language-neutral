package main

import (
    "net/http/cgi"
    "net/http"
    "fmt"
    "strconv"
)

func main() {

    fmt.Printf("Content-Type: text/html\n\n")

    var req *http.Request
    req, _ = cgi.Request()

    if(req.Method == "GET"){
        var queryString = req.URL.Query();
        var magnum, _ = strconv.Atoi(queryString.Get("magicnum"))
        printBody(queryString.Get("username"), queryString.Get("password"), magnum)
    } else if (req.Method == "POST"){
        username := req.FormValue("username");
        password := req.FormValue("password");
        magnum := req.FormValue("magicnum");
        magnumint, _ :=strconv.Atoi(magnum)
        printBody(username, password, magnumint)
    }
}


func printBody(username string, password string, n int){
    var helloString = "";
    for i := 0; i < n; i++ {
		helloString += fmt.Sprintf(`<h1>Hello %s with a password of %s!</h1>`, username, password)
	}

	fmt.Printf(`<!doctype html>
	<html lang="en">
	<head>
	<title>Node CGI Process Data</title>
	<style>
	</style>
	</head>
	<body>
		<h1>Node Process Data</h1>
		%s
	</body>
	</html>`, helloString);
}
