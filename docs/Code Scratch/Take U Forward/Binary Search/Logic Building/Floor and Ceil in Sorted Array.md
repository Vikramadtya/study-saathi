---
tags:
  - cc
  - binary-search
  - array
---

# Floor and Ceil in a Sorted Array

## Question
Given a sorted array `nums` and a target `x`:
* **Floor:** The largest element $\le x$.
* **Ceil:** The smallest element $\ge x$.
Return -1 if either does not exist.

## Solution

### Pattern
**Binary Search: Lower Bound Derivative**

#### How to Identify
* The array is sorted.
* You need to find the "closest" elements based on a boundary ($x$).
* The problem asks for values on both sides of a transition point.

### Description
The "Ceiling" of $x$ is exactly the **Lower Bound** of $x$ (the first element $\ge x$). Once the Ceiling's index is found:
1. If $nums[idx] == x$, the Floor is also $x$.
2. If $nums[idx] > x$, the Floor is the element at $idx - 1$ (if it exists).
3. If $x$ is greater than all elements, the Ceiling is -1 and the Floor is the last element.



### Complexity

| Label            | Worst       | Average     |
| :--------------- | :---------- | :---------- |
| Time Complexity  | $O(\log n)$ | $O(\log n)$ |
| Space Complexity | $O(1)$      | $O(1)$      |

### Code (Single Pass)

```java
class Solution {
    public int[] getFloorAndCeil(int[] nums, int x) {
        if (nums == null || nums.length == 0) return new int[]{-1, -1};

        int n = nums.length;
        int left = 0, right = n;

        // Standard Lower Bound search (First element >= x)
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] >= x) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        int ceil = (left < n) ? nums[left] : -1;
        int floor;

        // If left is within bounds and we found exactly x
        if (left < n && nums[left] == x) {
            floor = nums[left];
        } else {
            // Otherwise, floor is the element to the left of the ceiling
            floor = (left > 0) ? nums[left - 1] : -1;
        }

        return new int[]{floor, ceil};
    }
}
```

## Concepts to Think About

- The Neighborhood Rule: In sorted arrays, the elements satisfying `nums[i]<x` and `nums[i]≥x` are always adjacent. Finding one usually gives you the other for free.
- Lower Bound as Ceil: Why is lowerBound the same as Ceil? Because both look for the first element that hasn't "failed" the ≥x condition.
- Edge Cases: What happens when x is smaller than nums[0]? (Ceil is nums[0], Floor is -1). What if x is larger than nums[n-1]? (Ceil is -1, Floor is nums[n-1]).

### **Logical Follow-up**

**Question:** "Given a sorted array, find the **Closest Element** to a target $x$. If two numbers are equally close, return the smaller one."

**Solution:** 

1. Use the **Lower Bound** logic to find the ceiling. 
2. Compare the absolute difference between $x$ and the Ceiling (`nums[idx]`) and $x$ and the Floor (`nums[idx-1]`). 
3. Return the one with the smaller difference.

**Question (Find K Closest Elements):** "Given a sorted integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted. If there is a tie, the smaller strategy is preferred."

**L5 Analysis & Solution:**
A naive L4 solution would be to find the closest element and then expand outwards using two pointers for $O(\log n + k)$. However, an **L5 candidate** might suggest a more elegant **Binary Search on the Window**.

1. **Intuition:** We are looking for the **starting index** `left` of a window of size `k`. 
2. **Search Space:** The possible starting index `left` ranges from `0` to `n - k`.
3. **Binary Search Criteria:** We compare the distance of the elements at the edges of the window. For a `mid` index:
   * Is $x$ closer to `nums[mid]` or `nums[mid + k]`?
   * If `x - nums[mid] > nums[mid + k] - x`, then `mid` is too far to the left, so `left = mid + 1`.
   * Else, `right = mid`.
4. **Result:** After $O(\log(n-k))$ time, we have the start of the perfect window.