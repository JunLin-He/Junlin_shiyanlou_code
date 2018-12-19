package main

import (
	"fmt"
	"math/rand"
)

func main() {

	// `rand.Intn` return a random integer n, `0 <= n <= 100`
	fmt.Print(rand.Intn(100), ",")
	fmt.Print(rand.Intn(100))
	fmt.Println()

	// `rand.Float64` return a 64bit float number `f`, `0.0 <= f <= 1.0`
	fmt.Println(rand.Float64())

	// random float `f`, `5.0 <= f <= 10.0`
	fmt.Print((rand.Float64()*5)+5, ",")
	fmt.Print((rand.Float64() * 5) + 5)
	fmt.Println()

	// To make the pseudo-random number generator deterministic, you can give it a clear seed
	s1 := rand.NewSource(42)
	r1 := rand.New(s1)

	fmt.Print(r1.Intn(100), ",")
	fmt.Print(r1.Intn(100))
	fmt.Println()

	// If you use the same seed generated random number generator, the same random number sequence will be generated
	s2 := rand.NewSource(42)
	r2 := rand.New(s2)
	fmt.Print(r2.Intn(100), ",")
	fmt.Print(r2.Intn(100))
	fmt.Println()
}
