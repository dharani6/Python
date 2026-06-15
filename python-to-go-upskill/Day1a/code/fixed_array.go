package main

import "fmt"

/*
reverseArray demonstrates reversing a fixed-size array in Go.

This example is written for fresh learners. It shows how to reverse the
elements of a fixed-length array (here `[4]int`) by swapping elements
from the ends moving toward the center.

Key points for beginners:
- Arrays in Go have fixed size and their type includes the length, e.g. `[4]int`.
- The function modifies and returns a copy of the array because arrays are
  value types; modifying the parameter does not change the caller's array
  unless you assign the returned value.

Example:
- Input  : [4]int{1, 2, 3, 4}
- Output : [4]int{4, 3, 2, 1}
*/
func reverseArray(a [4]int) [4]int {
	for i, j := 0, len(a)-1; i < j; i, j = i+1, j-1 {
		a[i], a[j] = a[j], a[i]
	}
	return a
}

func main() {
	inputArray := [4]int{1, 2, 3, 4}

	result := reverseArray(inputArray)
	fmt.Println(result)

	// Complexity:
	// - Time complexity: O(n)
	//   The function visits each element at most once (half the array is swapped).
	// - Space complexity: O(1) for auxiliary space
	//   The reversal is done in-place on the function's local copy of the array.
	//   Note: because arrays are value types in Go, the caller receives the
	//   modified copy returned by the function.
	//
	// Useful info:
	// - To avoid copying for large data, use a slice instead of an array: `[]int`.
	// - For slices, reversing in place will modify the original slice seen by the caller.
	// - If you want to keep the original array unchanged, make a copy explicitly
	//   before reversing: `b := a; reverseArray(b)`.
}

// Input  : [4]int{1, 2, 3, 4}
// Output : [4]int{4, 3, 2, 1}
