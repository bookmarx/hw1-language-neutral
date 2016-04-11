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

    fmt.Printf("<html>"+ 
			  "<head><title>GO CGI Script</title></head>" +
			  "<body bgcolor='"+colors[r1]+"'>")

	fmt.Println(t0.Format("2006-01-02 15:04:05"))
}