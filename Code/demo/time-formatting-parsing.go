package main

import (
	"fmt"
	"time"
)

func main() {

	p := fmt.Println

	// A formatting demo according to RFC3339, use corrisponding model constance
	t := time.Now()
	p(t.Format(time.RFC3339))

	t1, e := time.Parse(
		time.RFC3339,
		"2012-11-01T22:08:41+00:00")
	p(t1)

	p(t.Format("3:04pm"))
	p(t.Format("Mon Jan _2 15:04:05 2006"))
	p(t.Format("2006-01-02T15:04:05.999999-07:00"))

	form := "3 04 PM"
	t2, e := time.Parse(form, "8 41 PM")
	p(t2)

	// For time which showed in pure number, it can be formated with standard formatting
	fmt.Printf("%d-%02d-%02dT%02d:%02d:%02d-00:00\n",
		t.Year(), t.Month(), t.Day(),
		t.Hour(), t.Minute(), t.Second())

	ansic := "Mon Jan _2 15:04:05 2006"
	_, e = time.Parse(ansic, "8:41PM")
	p(e)
}
