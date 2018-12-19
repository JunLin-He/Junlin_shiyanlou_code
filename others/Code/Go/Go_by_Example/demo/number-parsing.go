package main

// Built-in `strconv` package include the digital-analysis function
import (
	"fmt"
	"strconv"
)

func main() {

	// `64` indicated the number of digits of the resolved number
	f, _ := strconv.ParseFloat("1.234", 64)
	fmt.Println(f)

	// `0` indicate that automatically infer the hexadecimal number of the number represented by the string
	i, _ := strconv.ParseInt("123", 0, 64)
	fmt.Println(i)

	// Automatic recognitio of hexadecimal numbers
	d, _ := strconv.ParseInt("0x1c8", 0, 64) // 1 * 16^2 + 12 * 16^1 + 8 * 16^0 == 456
	fmt.Println(d)

	u, _ := strconv.ParseUint("789", 0, 64)
	fmt.Println(u)

	k, _ := strconv.Atoi("135")
	fmt.Println(k)

	_, e := strconv.Atoi("wat")
	fmt.Println(e)
}
