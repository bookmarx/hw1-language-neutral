package main

import "time"
import "fmt"
import "math/rand"

//import "net/http/cgi"

func main() {
    fmt.Printf("Content-Type: text/html\n\n")

	colors := []string{"aqua", "black", "blue", "fuchsia",
                     "gray", "green", "lime", "maroon",
                     "navy", "olive", "purple", "red",
                     "silver", "teal", "white", "yellow"}

	s1 := rand.NewSource(time.Now().UnixNano())
    r1 := (rand.New(s1).Intn(16))

	t0 := time.Now()

    fmt.Printf(`<!doctype html>
				<html lang="en">
				<head>
				    <title>Hello CGI World</title>
				</head>
				<body style="background-color: %s">
				    <h1>Hello World from Go @  %s </h1>
				</body>
				</html>`, colors[r1], t0.Format("2006-01-02 15:04:05"))
}
