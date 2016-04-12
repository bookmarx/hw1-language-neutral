package main

import "fmt"
// import "net/http/cgi"
import "os"
import "bytes"
import "regexp"
import  "sort"
import "strings"

func main() {
    var browserBuffer bytes.Buffer
    var serverBuffer bytes.Buffer

    fmt.Printf("Content-Type: text/html\n\n")
    // fmt.Printf("%s",os.Environ())
    var keys []string
    for _, value := range os.Environ() {
        pair := strings.Split(value, "=")
        keys = append(keys, pair[0])
    }
    sort.Strings(keys)

    for _, key := range keys {
        isMatch, _ := regexp.MatchString("(^HTTP)|(^REQUEST)|(^QUERY)", key)
        envVar := fmt.Sprintf(`<tr><td>%s</td><td>%s</td></tr>`,key, os.Getenv(key))
        if(isMatch) {
            browserBuffer.WriteString(envVar);
        } else {
            serverBuffer.WriteString(envVar);
        }
    }

    fmt.Printf(`<!doctype html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
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
                </html>`,
                browserBuffer.String(),
                serverBuffer.String())
}
