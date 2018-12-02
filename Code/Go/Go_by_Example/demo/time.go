package main

import (
	"fmt"
	"time"
)

func main() {
	p := fmt.Println

	// Get the current time
	now := time.Now()
	p(now)

	// Year, Month, Day, hour, min, sec, milsec, timezone
	then := time.Date(
		2009, 11, 17, 20, 34, 58, 651387237, time.UTC)

	p(then)

	// Catch every component of time
	p(then.Year())
	p(then.Month())
	p(then.Day())
	p(then.Hour())
	p(then.Minute())
	p(then.Second())
	p(then.Nanosecond())
	p(then.Location())

	p(then.Weekday())

	// Compare two time: Before, After, Same
	p(then.Before(now))
	p(then.After(now))
	p(then.Equal(now))

	// Return a `Duration`
	diff := now.Sub(then)
	p(diff)

	// Length of time in diffrent units
	p(diff.Hours())
	p(diff.Minutes())
	p(diff.Seconds())
	p(diff.Nanoseconds())

	// `Add`-> Forward a time interval; `-`-> Back shift a time interval
	p(then.Add(diff))
	p(then.Add(-diff))

}
