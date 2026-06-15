package main

import "fmt"

/*
reverseString reverses the characters in a string.

This program is written for fresh learners.
The reverseString function converts the input string to a slice of runes
so it handles multi-byte characters correctly. It then swaps characters
from the outside in until the middle is reached.

Example:
- Input  : "upskill"
- Output : "llikspu"
*/
func reverseString(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}

func main() {
	result := reverseString("upskill")
	fmt.Println(result)

	// Complexity explanation:
	// Time complexity: O(n)
	//   We visit each character in the string once when swapping.
	// Space complexity: O(n)
	//   We create a new slice of runes and a new string of the same length.
}
