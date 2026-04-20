---
tags:
  - cc
  - binary-search
  - array
  - modular-code
---

# Find First and Last Position of Element

## Question
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value. If the target is not found, return `[-1, -1]`.

## Solution

### Pattern
**Modular Binary Search (Boundary Finding)**

#### How to Identify
* The array is sorted.
* You need to find a **range** or **interval** of identical values.
* The problem requires $O(\log n)$ performance.

### Description
Instead of one search, we perform two. One search finds the **leftmost** index (the first element $\ge$ target), and the other finds the **rightmost** index (the first element $>$ target, then minus one). By using a helper function, we keep the code clean and reduce the surface area for bugs.



### The Intuition
Imagine a plateau in a landscape. You want to find where the plateau starts and where it ends. You use binary search to find the first step that reaches the plateau's height. Then you use it again to find the first step that goes *above* the plateau's height. The space between those two steps is your range.

### Complexity

| Label | Worst | Average |
| :--- | :--- | :--- |
| Time Complexity | $O(\log n)$ | $O(\log n)$ |
| Space Complexity | $O(1)$ | $O(1)$ |

### Code (L5 Refactored Version)

```java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int first = findBound(nums, target, true);
        if (first == -1) return new int[]{-1, -1};
        
        int last = findBound(nums, target, false);
        return new int[]{first, last};
    }

    private int findBound(int[] nums, int target, boolean isFirst) {
        int left = 0, right = nums.length - 1;
        int ans = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                ans = mid; // Record candidate
                if (isFirst) {
                    right = mid - 1; // Keep looking left
                } else {
                    left = mid + 1;  // Keep looking right
                }
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return ans;
    }
}
```


## Concepts to Think About

- The lowerBound Relation: The first occurrence is exactly lowerBound(target). The last occurrence is upperBound(target) - 1. Why? (Hint: Upper bound is the first element strictly greater than the target).
- Search Space Optimization: If you find the first occurrence at index k, your second search space only needs to be [k, nums.length - 1].
- DRY Principle: In an L5 interview, modularizing code into findBound or binarySearch helpers is often more important than the algorithm itself.
- Empty/Single Element Arrays: How does the logic change if the array has only one element? (The loop runs once, left and right both point to index 0, and ans is correctly recorded).


### Logical Follow-up

**Question:** "What if the array is sorted but **circularly shifted** (e.g., `[4, 5, 5, 5, 6, 1, 2]`)? Can you still find the range of `5` in $O(\log n)$?"

**Solution:**

1. Use Binary Search to find the **Pivot** (the minimum element) in $O(\log n)$.
2. The pivot divides the array into two sorted halves.
3. Identify which half (or both) could contain the target.
4. Run your `searchRange` logic on that specific segment.


**Question (Search in a Sorted Array with Duplicates and "Gaps"):**
"Imagine a sorted array where some elements are replaced with empty strings (e.g., `["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]`). Find the index of a target string. If the target appears multiple times, return the first and last index."

**Solution:**

This is called **Sparse Binary Search**.

1. **The Challenge:** If `nums[mid]` is an empty string `""`, you don't know whether to move left or right.
2. **L5 Solution:** When `nums[mid] == ""`, you must linearly move `mid` to the closest non-empty string (either left or right).
3. **Worst Case:** If the array is almost all empty strings, the complexity can degrade to $O(n)$.
4. **Range Search:** Once you've moved `mid` to a non-empty string, you proceed with the standard range-finding logic.