---
tags:
  - cc
  - binary-search
  - parity-check
  - array
---

# Single Element in a Sorted Array

## Question

Given a sorted array `nums` where every element appears twice except for one, find that single element in $O(\log n)$ time and $O(1)$ space.

## Solution

### Pattern: Index Parity

Before the single element, pairs are at indices $(even, odd)$. After the single element, the parity shifts, and pairs are at $(odd, even)$.

### Description

We binary search for the "transition point" where the $even \to odd$ pair property breaks.

1. Pick `mid`.
2. Find its "partner" index using `mid ^ 1`.
3. If `nums[mid] == nums[mid ^ 1]`, the single element hasn't appeared yet. Move `left = mid + 1`.
4. Otherwise, the single element is at `mid` or to its left. Move `right = mid`.

### Complexity

| Label            | Worst Case  | Average Case |
| :--------------- | :---------- | :----------- |
| Time Complexity  | $O(\log n)$ | $O(\log n)$  |
| Space Complexity | $O(1)$      | $O(1)$       |

### Code (Refined L5 Version)

```java
class Solution {
    public int singleNonDuplicate(int[] nums) {
        int left = 0, right = nums.length - 1;

        // Using left < right so we converge on the answer
        while (left < right) {
            int mid = left + (right - left) / 2;

            // The XOR trick:
            // If mid is even, mid^1 is mid+1
            // If mid is odd, mid^1 is mid-1
            if (nums[mid] == nums[mid ^ 1]) {
                // Property holds (pair is still even-odd)
                // Single element must be on the right
                left = mid + 1;
            } else {
                // Property broken, single element is here or to the left
                right = mid;
            }
        }
        return nums[left];
    }
}
```

## Concepts to Think About

- The XOR Invariant: i ^ 1 is a powerful way to toggle between adjacent indices in pairs. It’s cleaner than manual parity checks.
- Search Space: Why does this only work if the total length is odd? (Because pairs + one element always equals an odd number).
- Parity Shift: Visualizing the array as a sequence of pairs (a,a),(b,b),(c),(d,d) makes the "break" point obvious.

## Logical Follow-up

**Question:** "What if the array is **not sorted**, but you still have pairs and one single element? Can you do it in $O(\log n)$?"

**Solution:** **No.** If the array is not sorted, you lose the parity property. You would have to use a **Bitwise XOR** of all elements: $a \oplus a \oplus b \oplus b \oplus c = c$. This would take $O(n)$ time and $O(1)$ space.

**Question (The "Median of Two Sorted Arrays" Twist):**
"You are given two sorted arrays `nums1` and `nums2` of size $m$ and $n$ respectively. Find the **median** of the two sorted arrays. The overall run time complexity should be $O(\log(min(m, n)))$."

**L5 Analysis & Solution:**
This is the ultimate test of "Binary Search on Partitions."

1. **Goal:** We need to partition both arrays such that the left side has the same number of elements as the right side, and all elements on the left are $\le$ all elements on the right.
2. **Binary Search on Smallest Array:** We only binary search on the smaller array to find the partition point `i`. The partition point `j` for the second array is then calculated as `(m + n + 1) / 2 - i`.
3. **Check Boundaries:** \* Is $nums1[i-1] \le nums2[j]$?
   - Is $nums2[j-1] \le nums1[i]$?
4. **Edge Cases:** If the total length is odd, the median is `max(L1, L2)`. If even, it's `(max(L1, L2) + min(R1, R2)) / 2`.
