---
tags:
  - cc
  - array
  - rotation
---

# Rotate Array Left by K

## Question
Given an integer array `nums` and a non-negative integer `k`, rotate the array to the **left** by `k` steps. The modification must be done in-place with $O(1)$ extra space.

## Solution

### Pattern
**Triple Reverse (Reversal Algorithm)**

#### How to Identify
* The problem requires rotating an array by a variable $k$.
* You are restricted to $O(1)$ extra space.
* You need to avoid the $O(n \cdot k)$ "shift-one-by-one" brute force.

### Description
The Triple Reverse algorithm relies on a mathematical property: if you reverse two distinct parts of an array and then reverse the entire array (or vice versa), the elements will have effectively "swapped" positions in a cyclic manner. For a **Left Rotation**, we divide the array into the first $k$ elements and the remaining $n-k$ elements.



### The Intuition
Think of the array as two blocks: $A$ (the first $k$ elements) and $B$ (the rest).
1. Initial: $AB$
2. Reverse $A$: $A^rB$
3. Reverse $B$: $A^rB^r$
4. Reverse All: $(A^rB^r)^r = BA$
By reversing the components and then the whole, you move the front block to the back.

### Complexity

| Label            | Worst           | Average         |
| :--------------- | :-------------- | :-------------- |
| Time Complexity  | $O(n)$          | $O(n)$          |
| Space Complexity | $O(1)$          | $O(1)$          |

### Code

```java
class Solution {
    public void rotateArray(int[] nums, int k) {
        if (nums == null || nums.length < 2) return;

        int n = nums.length;
        k %= n; // Handle cases where k >= n
        if (k == 0) return;

        // For Left Rotation:
        // 1. Reverse the first k elements: [0...k-1]
        reverse(nums, 0, k - 1);
        // 2. Reverse the rest: [k...n-1]
        reverse(nums, k, n - 1);
        // 3. Reverse the whole array: [0...n-1]
        reverse(nums, 0, n - 1);
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}
```

## Concepts to Think About

- Left vs. Right Rotation: To perform a Right Rotation by k, the logic is slightly different. You would reverse the last k elements, then the first n−k, then the whole. Can you see how the "split point" moves?
- The Juggling Algorithm: There is another O(1) space approach using the Greatest Common Divisor (GCD) of n and k. It moves elements in "cycles." While harder to code, it performs fewer total assignments than the Reversal method.
- Block Swap Algorithm: This is another O(n) time approach that is very efficient for large k. It works by swapping blocks of size k recursively.
- Why Modulo? If n=5 and k=7, rotating 7 times is the same as rotating 2 times (7(mod5)). Always include this to show you understand cyclic properties.
