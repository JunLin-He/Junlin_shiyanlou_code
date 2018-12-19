package main

import "time"
import "fmt"

func main() {
	timer1 := time.NewTimer(time.Second * 2)
	fmt.Println("1")

	<-timer1.C
	fmt.Println("2")
	fmt.Println("Timer 1 expired")

	timer2 := time.NewTimer(time.Second)
	fmt.Println("3")
	go func() {
		<-timer2.C
		fmt.Println("4")
		fmt.Println("Timer 2 expired")
	}()
	stop2 := timer2.Stop()
	fmt.Println("5")
	if stop2 {
		fmt.Println("Timer 2 stopped")
		fmt.Println("6")
	}
	fmt.Println("7")
}
