package main

import "fmt"

func reverseNumber(n int) int {
	sign := 1
	if n < 0 {
		sign = -1
		n = -n
	}
	result := 0
	for n != 0 {
		result = result*10 + n%10
		n /= 10
	}
	return sign * result
}

func main() {
	result := reverseNumber(-1234)
	fmt.Println(result)
}

// Input: -1234   Output: -4321
