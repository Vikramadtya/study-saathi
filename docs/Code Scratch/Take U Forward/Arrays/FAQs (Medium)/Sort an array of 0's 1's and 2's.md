---
tags:
  - cc
  - sorting
  - two-pointers
  - dnf-partition
---

# Sort Colors (Dutch National Flag Problem)

## Question
Given an array `nums` with $n$ objects colored red (0), white (1), or blue (2), sort them **in-place** so that objects of the same color are adjacent, in the order red, white, and blue.

## Solution

### Pattern
**Three-Way Partitioning (Dutch National Flag)**

#### How to Identify
* The input contains a **fixed, small number of unique values** (e.g., 0, 1, 2).
* You are asked to sort in $O(n)$ time and $O(1)$ space.
* Relative order of same elements doesn't matter (though the standard version is unstable).

### Description
We maintain three pointers to divide the array into four sections. 
1. Elements before `low` are **0s**.
2. Elements between `low` and `mid-1` are **1s**.
3. Elements from `mid` to `high` are **unprocessed**.
4. Elements after `high` are **2s**.

As `mid` (the explorer) traverses the array, it "throws" 0s to the left and 2s to the right.



### The Intuition
Imagine you are sorting three types of balls rolling down a tube. You have a "0-zone" on the far left and a "2-zone" on the far right. Every time you see a 0, you kick it to the left zone. Every time you see a 2, you kick it to the right zone. If you see a 1, you just let it stay where it is. By the time you've looked at every ball, the 1s will naturally be squeezed into the middle.

### Complexity

| Label            | Worst | Average |
| :--------------- | :---- | :------ |
| Time Complexity  | $O(n)$ | $O(n)$  |
| Space Complexity | $O(1)$ | $O(1)$  |

### Code (Refined Implementation)

```java
class Solution {
    public void sortColors(int[] nums) {
        if (nums == null || nums.length < 2) return;

        int low = 0;          // Boundary for 0s
        int mid = 0;          // Explorer / Boundary for 1s
        int high = nums.length - 1; // Boundary for 2s

        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums, low, mid);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else { // nums[mid] == 2
                swap(nums, mid, high);
                high--;
                // Do NOT increment mid here; we must check the new value at mid
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```

## Concepts to Think About

- Stability: Is this algorithm stable? (Hint: No. Swapping mid and high can change the relative order of two 2s).
- Counting Sort Alternative: Why is DNF better than a two-pass counting sort? (Hint: DNF is a single pass, which matters for "One-Write" constraints or when the array is in a read-once stream).
- Multi-Value Partitioning: How would you adapt this for 4 or 5 colors? (Hint: You'd need k−1 pointers, but the logic becomes increasingly complex).
- Quicksort Connection: This three-way partition is exactly what makes QuickSort efficient when there are many duplicate keys.


---

### Logical Follow-up

**Question:** "What if the array only contained **0s and 1s**? How would you simplify your current logic?"

**Solution:** This becomes a standard **Two-Pointer** partition (like the first step of QuickSort). 
* You'd use a `left` and `right` pointer. 
* While `left < right`, if `nums[left] == 1` and `nums[right] == 0`, swap them. 
* Increment `left` if it's 0, and decrement `right` if it's 1.

