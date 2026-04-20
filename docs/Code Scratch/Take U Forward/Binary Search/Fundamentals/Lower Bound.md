---
tags:
  - cc
  - binary-search
  - array
---

# Lower Bound (The Transition Point Pattern)

## Question
Given a sorted array and a value $x$, find the **Lower Bound**: the first/smallest index $i$ such that $nums[i] \ge x$. If no such index exists, return the length of the array.

## Solution

### Pattern
**Binary Search: Predicate Transition**

### How to Identify
* The search space is **monotonic** (sorted).
* You are looking for a **threshold** or **boundary** (the first element that meets a criteria).
* The criteria can be expressed as a boolean function $f(i)$ that is `false` for a range and then becomes `true`.

### Description
We treat the array as a sequence of boolean values where the condition is $nums[i] \ge x$. We want to find the first index where this becomes `true`. By using `left < right` and `right = mid`, we continuously shrink the search space while keeping the first potential "true" value within our bounds.



### The Intuition
Imagine a long line of people sorted by height. You want to find the first person who is at least 6 feet tall. You check the middle person. If they are 6'2", you know the "first" person is either them or someone to their left—so you keep them in your search space. If they are 5'11", you know everyone to their left is too short, so you discard them and look to the right.

### Complexity

| Label | Worst | Average |
| :--- | :--- | :--- |
| Time Complexity | $O(\log n)$ | $O(\log n)$ |
| Space Complexity | $O(1)$ | $O(1)$ |

### Code

```java
class Solution {
    public int lowerBound(int[] nums, int x) {
        if (nums == null || nums.length == 0) return 0;

        int left = 0;
        int right = nums.length; // Range: [0, n] inclusive of the "not found" index

        while (left < right) {
            int mid = left + (right - left) / 2;

            // Predicate: Is this element >= x?
            if (nums[mid] >= x) {
                // This could be the answer, or the answer is to the left.
                // We keep mid in the search space.
                right = mid;
            } else {
                // This element is too small. Discard it and everything to the left.
                left = mid + 1;
            }
        }

        // When left == right, we've found the transition point.
        return left;
    }
}
```

---

### Logical Follow-up
**Question:** "Given a sorted array that contains duplicates, find the **range** (start and end index) of a given target $x$. For example, if `nums = [5, 7, 7, 8, 8, 10]` and `x = 8`, return `[3, 4]`."

**Hint:** Use `lowerBound(x)` to find the start, and `lowerBound(x + 1) - 1` (or a dedicated `upperBound`) to find the end.


**Question (Capacity to Ship Packages):** "A conveyor belt has packages that must be shipped within $D$ days. The weights of the packages are given in an array `weights`. You must load the packages in the order given. Every day, we load as many packages as possible without exceeding the ship's weight capacity. Find the **minimum** weight capacity of the ship that will result in all packages being shipped within $D$ days."

**Analysis & Solution:**
This is a classic "Binary Search on Answers" problem.
1. **Search Space:** The minimum possible capacity is $\max(\text{weights})$ (to carry the heaviest package). The maximum possible capacity is $\sum \text{weights}$ (shipping all in 1 day).
2.  **Monotonicity:** If a capacity $C$ works, any capacity $> C$ also works. If it doesn't work, any capacity $< C$ won't work either. This is our "Sorted" property.
3.  **The Predicate:** Write a helper function `canShip(capacity, D)` that simulates the process.
4.  **Binary Search:** Apply your `lowerBound` logic on the range $[\max(\text{weights}), \sum \text{weights}]$ to find the smallest capacity that satisfies `canShip == true`.

