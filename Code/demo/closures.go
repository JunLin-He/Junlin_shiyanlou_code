package main

import "fmt"

func intSeq() func() int {
	i := 0
	return func() int {
		i += 1
		return i
	}
}

func main() {

	nextInt := intSeq() // i := 0

	fmt.Println(nextInt()) // i == 1
	fmt.Println(nextInt()) // i == 2
	fmt.Println(nextInt()) // i == 3

	newInts := intSeq()    // i := 0
	fmt.Println(newInts()) // i == 1
}
