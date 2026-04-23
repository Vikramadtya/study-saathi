---
tags:
  - binary-search
  - array
  - rotated-sorted-array
  - pivot
---

# Number of Rotations in Sorted Array

## Question

Given a sorted array of distinct integers that has been right-rotated $k$ times, find $k$.

## Solution

### Pattern: Finding the Discontinuity (The Pivot)

In a sorted array rotated $k$ times, the element at index $k$ is the **minimum element**. The array consists of two sorted "slopes." The point where the high slope drops to the low slope is our pivot.

### Description

We use binary search to "squeeze" the search space toward the minimum element:

1. Compare `nums[mid]` with `nums[right]`.
2. If $nums[mid] > nums[right]$, the "drop-off" (minimum) must be to the right of `mid`.
3. If $nums[mid] \le nums[right]$, `mid` could be the minimum, or the minimum is to its left.
4. When `left == right`, we have found the index of the minimum element, which equals the number of rotations.

### Complexity

| Label            | Complexity  |
| :--------------- | :---------- |
| Time Complexity  | $O(\log n)$ |
| Space Complexity | $O(1)$      |

### Code (Refined)

```java
class Solution {
    public int findKRotation(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        // Converge on the minimum element's index
        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] > nums[right]) {
                // The pivot is to the right
                left = mid + 1;
            } else {
                // mid could be the pivot or pivot is to the left
                right = mid;
            }
        }
        // At the end, left == right == index of minimum element
        return left;
    }
}
```

## Concepts to Think About

- The Index-Rotation Identity: Why does the index of the minimum element equal the number of rotations? Think about the "0 rotations" case (index 0) vs. "1 rotation" (index 1).
- The Right-Boundary Rule: Why is comparing to nums[right] safer than nums[left]? (Hint: In a non-rotated array, nums[left]<nums[mid] is true, but that doesn't tell you the pivot is on the right—there is no pivot!)
- Termination: Why does left < right prevent an infinite loop when only two elements are left?

## Logical Follow-up

**Question:** "Now that you have the rotation count ($k$), how would you search for a specific `target` value in this same array in $O(\log n)$ time?"

**Solution:** You have two choices:

1. **The Two-Search Method:** Use $k$ to split the array into two sorted halves (`[0...k-1]` and `[k...n-1]`). Perform a standard binary search on the appropriate half.

2. **The "Virtual" Index Method:** Perform one binary search on the whole array, but map the `mid` index to the "real" sorted index using:  
   $$\text{realMid} = (\text{mid} + k) \pmod n$$

**Question (The Duplicate Trap):** "Suppose the array **contains duplicates** (e.g., `[2, 2, 2, 0, 2, 2, 2]`). Does your $O(\log n)$ solution still work? If not, what is the new worst-case time complexity, and how do you handle it in a production environment at Google?"

**L5 Analysis & Solution:**

1. **The Problem:** If `nums[mid] == nums[right]`, you cannot tell if the pivot is to the left or right. The binary search "breaks."
2. **The Fix:** When $nums[mid] == nums[right]$, you must simply shrink the search space linearly by setting `right = right - 1`.
3. **Complexity:** The worst-case time complexity becomes $O(n)$ (e.g., an array of all $1$s with one $0$ hidden somewhere).
4. **Production Context:** In an L5 role, you should mention that while the _average_ case is still fast, we must be aware of $O(n)$ "Degenerate Cases" for our Service Level Objectives (SLOs). We might even add telemetry to track how often our binary search "downgrades" to linear search.

**Revised Loop Segment:**

```java
if (nums[mid] > nums[right]) {
    left = mid + 1;
} else if (nums[mid] < nums[right]) {
    right = mid;
} else {
    // Ambiguity! Shrink the boundary linearly.
    right--;
}
```
