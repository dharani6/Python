// Stack and queue reversal with slices in Go.
//
// This program shows how to reverse a sequence of values using a slice.
// In Go, slices are commonly used for both stack-like and queue-like behavior.
package main

import "fmt"

func reverseSeq(s []int) []int {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
	return s
}

func main() {
	inputSlice := []int{1, 2, 3, 4, 5}
	result := reverseSeq(inputSlice)

	fmt.Println("Input  :", inputSlice)
	fmt.Println("Output :", result)
	fmt.Printf("input %v output %v\n", inputSlice, result)

	// Complexity:
	// - Time complexity: O(n) because each element is swapped at most once.
	// - Space complexity: O(1) additional space because the reversal happens in place.
	//
	// Useful info:
	// - Slices are flexible, and reversing a slice modifies the underlying data.
	// - If you need to preserve the original slice, make a copy first:
	//   `copySlice := append([]int(nil), inputSlice...)`
	// - Use slices for both stack and queue patterns, but choose a clear API
	//   for your intended behavior.
}

// Input  : [1,2,3,4,5]
// Output : [5,4,3,2,1]
