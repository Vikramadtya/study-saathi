---
tags:
  - cc
  - binary-search
  - pivot-finding
  - rotated-array
---

# Find Minimum in Rotated Sorted Array

## Question
Given an integer array `nums` (distinct values) rotated between 1 and $N$ times, find the minimum element in $O(\log n)$ time.

## Solution

### Pattern
**Binary Search: Pivot Transition**

#### How to Identify
* The array is a "Mountain and Valley" or "Two-Slope" structure.
* You are looking for the **Global Minimum** (the start of the low slope).
* The target is a property (the drop-off) rather than a specific value.

### Description
We use the `left < right` template. We compare the middle element with the rightmost element. 
* If $nums[mid] > nums[right]$, we are on the "High Slope," and the minimum must be to the right of `mid`. 
* If $nums[mid] < nums[right]$, we are on the "Low Slope" (or the array is fully sorted), and the minimum is either `mid` itself or to its left.



### The Intuition: "The Cliff"
Imagine you are walking on a staircase that is mostly going up, but at one point there is a huge cliff that drops back to the ground. You want to find that drop. If your current step is higher than the very last step in the distance, you know the drop is still ahead of you. If your current step is lower than the last step, you've already passed the drop (or it never happened).

### Complexity

| Label | Worst | Average |
| :--- | :--- | :--- |
| Time Complexity | $O(\log n)$ | $O(\log n)$ |
| Space Complexity | $O(1)$ | $O(1)$ |

### Code (Refined L5 Version)

```java
class Solution {
    public int findMin(int[] nums) {
        if (nums == null || nums.length == 0) return -1;

        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            // L5 Logic: Compare mid with right to find the 'Cliff'
            if (nums[mid] > nums[right]) {
                // Minimum must be in the right half (excluding mid)
                left = mid + 1;
            } else {
                // Minimum could be mid or in the left half
                right = mid;
            }
        }

        // left == right, pointing at the minimum
        return nums[left];
    }
}
```

## Concepts to Think About

- Why compare to right and not left? If you compare mid to left, the "fully sorted" case (0 rotations) becomes an edge case you have to handle separately. Comparing to right handles both rotated and non-rotated arrays with the same logic.
- The `right = mid` vs `left = mid + 1` logic: When `nums[mid]<nums[right]`, `mid` could be the minimum itself, so we keep it. When `nums[mid]>nums[right]`, `mid` is definitely part of the "high" side, so we discard it.
- Duplicates: If the array had duplicates, would this remain O(logn)? (No, we'd need to handle nums[mid]==nums[right] linearly).


### **Logical Follow-up**

**Question:** "What happens if the array is rotated $N$ times (making it effectively sorted)? Does your binary search logic still work, or does it return an incorrect index?"

**Answer:** It still works! If the array is sorted, $nums[mid]$ will always be less than $nums[right]$, causing the `right` pointer to move left until it reaches `0`. The loop will terminate at `left = 0`, which is the correct minimum.

**Question (Find the K-th Smallest Element):** "You've successfully found the minimum element in $O(\log n)$. Now, can you find the **k-th smallest element** in the same rotated sorted array (distinct values) in $O(1)$ *additional* time after finding the minimum?"

**Answer:**

1.  **Find the Pivot:** First, use the $O(\log n)$ algorithm above to find the index of the minimum element, let's call it `pivot`.
2.  **Virtual Index Mapping:** A rotated sorted array is just a regular sorted array that has been **offset**.
3.  **The Formula:** The $k$-th smallest element ($0$-indexed) in a sorted array is at index $k$. In a rotated array, that element is at:
    $$\text{TargetIndex} = (\text{pivot} + k) \pmod N$$.
4.  **Result:** You return `nums[TargetIndex]`.

**Concepts to Think About:**

- **Rotated Binary Search on Values:** Can you use this same "Index Mapping" to search for a target value without the complex `if/else` logic we used before? (Yes! You map `mid` to `(mid + pivot) % N`).

- **Cache Locality:** Does accessing elements via modulo indexing affect performance on massive arrays? (Slightly, due to non-sequential memory access).
