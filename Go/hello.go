// First test in Go
package main

// Import OS and fmt packages
import(
	"fmt"
	"os"
)

func main(){
	fmt.Println("Hello, World")
	fmt.Println(os.Getenv("USER"),",Let's be friends!")
}