package main

import (
	"fmt"
)

/*
reverseSlice demonstrates how to reverse a slice in Go.

This example is written for fresh learners.
A slice is like a dynamic array, and reversing it means swapping
items from the beginning and end until the middle.

Example:
- Input  : [10, 20, 30, 40, 50]
- Output : [50, 40, 30, 20, 10]
*/
func reverseSlice(s []int) []int {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
	return s
}

func main() {
	inputSlice := []int{10, 20, 30, 40, 50}

	result := reverseSlice(inputSlice)
	fmt.Println(result)

	// Complexity:
	// - Time complexity: O(n)
	//   The function swaps each pair of elements once, so it processes
	//   the slice in a single pass.
	// - Space complexity: O(1)
	//   The reversal happens in place without creating a second slice.
	//
	// Useful info:
	// - Go slices are built on top of arrays and can change size.
	// - `reverseSlice` modifies the original slice values.
	// - If you want to keep the original slice unchanged, copy it first.
}
