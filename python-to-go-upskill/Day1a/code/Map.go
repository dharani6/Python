package main

import "fmt"

/*
Reverse a slice of keys in Go and explain the approach for new learners.

This example treats `keys` as a slice of strings and reverses its order
by swapping elements from the two ends moving toward the center.

Why this matters:
- Slices are the idiomatic variable-length sequence type in Go (like lists in Python).
- Reversing a slice is a common operation useful for algorithms and data processing.

How it works:
- We use two indices, `i` starting at 0 and `j` starting at `len(keys)-1`.
- While `i < j`, swap `keys[i]` and `keys[j]`, then move `i` forward and `j` backward.

Example:
- Input  : keys = ["a", "b", "c"]
- Output : keys = ["c", "b", "a"]

Complexity:
- Time complexity: O(n) — each element is touched at most once.
- Space complexity: O(1) additional space — the reversal is done in place.

Useful tips:
- This modifies the original slice; if you need to keep the original, copy it first:
  `copyKeys := append([]string(nil), keys...)` then reverse `copyKeys`.
- For slices of large objects, swapping moves only slice elements (headers),
  but the underlying values are referenced — copying may be cheaper depending on use.
*/
func main() {
	keys := []string{"a", "b", "c"}
	for i, j := 0, len(keys)-1; i < j; i, j = i+1, j-1 {
		keys[i], keys[j] = keys[j], keys[i]
	}
	fmt.Println(keys)
}

// Input  : keys = ["a","b","c"]
// Output : keys = ["c","b","a"]
