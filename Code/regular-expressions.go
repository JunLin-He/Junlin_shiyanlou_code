package main

import (
	"bytes"
	"fmt"
	"regexp"
)

var p = fmt.Println

func main() {

	match, _ := regexp.MatchString("p([a-z]+)ch", "peach")
	p(match) // true

	r, _ := regexp.Compile("p([a-z]+)ch")
	p(r.MatchString("peach"))      // true
	p(r.FindString("peach punch")) // peach

	p(r.FindStringIndex("peach punch"))         // [0 5]
	p(r.FindStringSubmatch("peach punch"))      // [peach ea]
	p(r.FindStringSubmatchIndex("peach punch")) // [0 5 1 3]

	p(r.FindAllString("peach punch pinch", -1))              //[peach punch pinch]
	p(r.FindAllStringSubmatchIndex("peach punch pinch", -1)) // [[0 5 1 3] [6 11 7 9] [12 17 13 15]]
	p(r.FindAllString("peach punch pinch", 2))               // [peach punch]

	p(r.Match([]byte("peach"))) // true
	r = regexp.MustCompile("p([a-z]+)ch")
	p(r) // p([a-z]+)ch

	p(r.ReplaceAllString("a peach", "<fruit>")) // a <fruit>

	in := []byte("a peach")
	out := r.ReplaceAllFunc(in, bytes.ToUpper)
	p(string(out)) // a PEACH

}
