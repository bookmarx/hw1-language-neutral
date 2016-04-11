package main

import "fmt"
// import "net/http/cgi"
import "os"
import "strings"
import "bytes"
import "regexp"

func main() {
    var browserBuffer bytes.Buffer
    var serverBuffer bytes.Buffer

    fmt.Printf("Content-Type: text/html\n\n")
    // fmt.Printf("%s",os.Environ())
    for _, value := range os.Environ() {
        pair := strings.Split(value, "=")
        isMatch, _ := regexp.MatchString("(^HTTP)|(^REQUEST)|(^QUERY)", pair[0])
        envVar := fmt.Sprintf(`<tr><td>%s</td><td>%s</td></tr>`,pair[0], pair[1])
        if(isMatch) {
            browserBuffer.WriteString(envVar);
        } else {
            serverBuffer.WriteString(envVar);
        }
    }

    fmt.Printf(`<!doctype html>
                <html lang="en">
                <head>
                <title>Node CGI Env Vars</title>
                <style>
                    table {
                        width: 100%%;
                    }
                    table, th, td {
                        border: 1px solid black;
                    }
                </style>
                </head>
                <body>
                    <h3>Browser Env Table:</h3>
                    <table>%s</table>
                    <hr>
                    <h3>Server Env Table:</h3>
                    <table>%s</table>
                </body>
                </html>`, browserBuffer.String(), serverBuffer.String())
}
