---
tags:
  - cc
  - array
  - binary-search
  - pivot
  - logic-nuance
---

# Search in Rotated Sorted Array

## Question
An integer array `nums` is sorted in ascending order with distinct values. It is then rotated at an unknown pivot. Given a target `k`, return its index. If not present, return -1.

## Solution

### Pattern
**One-Pass Binary Search (Conditional Monotonicity)**

#### How to Identify
* The array is "partially" sorted or rotated.
* The time complexity requirement is $O(\log n)$.
* The array structure has a "break" point but remains locally sorted.

### Description
In a rotated array, at least one half (either `[left, mid]` or `[mid, right]`) is **guaranteed** to be sorted. 

1. Find the `mid`.
2. Determine which half is sorted by comparing `nums[left]` and `nums[mid]`.
3. Check if the `target` falls within the range of the sorted half.
4. If yes, search that half; if no, search the other half.




#### Why `nums[left] <= nums[mid]`?

A common interview mistake is using `nums[left] < nums[mid]`. The equality check is the "glue" that prevents the algorithm from breaking during the final steps.

##### The 2-Element Base Case
Consider a range with only two elements: `[3, 1]` and `target = 1`.

* $left = 0, right = 1$
* $mid = 0 + (1 - 0) / 2 = \mathbf{0}$
* Here, **$left$ and $mid$ point to the same index.**

If we used `nums[left] < nums[mid]`:

* `nums[0] < nums[0]` is **False**.
* The algorithm would jump to the `else` block (assuming the right half is the sorted one).
* While the right half *is* technically sorted here, in more complex rotations, misidentifying which half is "broken" leads to skipping the target or index errors. 

**The Invariant:** A single element (where $left = mid$) is by definition **sorted**. The `<=` ensures the algorithm correctly identifies the left side as "sorted" in this base case.




### Complexity

| Label | Worst | Average |
| :--- | :--- | :--- |
| Time Complexity | $O(\log n)$ | $O(\log n)$ |
| Space Complexity | $O(1)$ | $O(1)$ |

### Code

```java
class Solution {
    public int search(int[] nums, int target) {
        if (nums == null || nums.length == 0) return -1;

        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;

            // Use <= to handle cases where left == mid (2-element windows)
            if (nums[left] <= nums[mid]) {
                // Left half is sorted
                if (target >= nums[left] && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                // Right half is sorted
                if (target > nums[mid] && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
}
```


## Concepts to Think About

- Strict Monotonicity: This logic relies on the values being distinct. If duplicates are introduced, the condition nums[left] == nums[mid] == nums[right] makes it impossible to know which side is sorted without a linear shrink (O(n)).
- Pivot vs. Target: Finding the smallest element (the pivot) is a different problem. There, the predicate is nums[mid] > nums[right].
- The "One-Pass" Advantage: While you could find the pivot first and then do a normal binary search, the one-pass approach is cleaner and more highly regarded in Google interviews.

### Follow-up

**Question:** "What if the array is rotated but looks exactly like the original sorted array (rotated by $n$ or $0$ positions)? Does your logic change?"

**Solution:** No. The `nums[left] <= nums[mid]` condition will simply be true for every iteration, and the algorithm will behave like a standard binary search. This proves the **robustness** of the approach—it handles the "zero-rotation" case without needing a special `if` statement.


