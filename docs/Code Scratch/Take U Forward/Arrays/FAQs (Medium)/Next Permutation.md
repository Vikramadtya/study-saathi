---
tags:
  - cc
  - permutations
  - arrays
---

# Next Permutation (Lexicographical Order)

## Question

Given an array of integers $nums$, rearrange the numbers into the **lexicographically next greater permutation**. If such an arrangement is not possible (the array is sorted in descending order), rearrange it to the lowest possible order (ascending). The replacement must be **in-place** and use $O(1)$ extra memory.

## Solution

### Pattern

**Breakpoint & Suffix Manipulation**
The algorithm relies on identifying the "pivot" point where the lexicographical order breaks and then minimally increasing that pivot while resetting the suffix to its smallest possible state.

### How to Identify

- The problem asks for "lexicographically next."
- Constraints require $O(1)$ space (In-place).
- Input involves permutations or arrangements.

### Description

Step-by-step explanation:



- **Step 1: Locate the Breakpoint.** Scan from right to left to find the first index $i$ such that $nums[i] < nums[i+1]$. This $nums[i]$ is our **pivot**. Everything to the right of $i$ is currently in non-increasing order.
- **Step 2: Find the Next Largest.** If a pivot is found, scan from right to left again to find the first element $nums[j]$ that is strictly greater than $nums[i]$. 
- **Step 3: Swap.** Swap $nums[i]$ and $nums[j]$. This minimally increases the prefix ending at $i$.
- **Step 4: Reverse the Suffix.** The elements to the right of index $i$ are still in descending order. To make the permutation as small as possible, reverse this suffix to put it in ascending order.
- **Case: No Pivot.** If no $i$ is found (array is `[3, 2, 1]`), skip steps 2-3 and simply reverse the entire array.

### The Intuition

Think of the array as a **topographical map**. A suffix in descending order is like a "peak" where you cannot find a larger permutation by just moving elements within that peak. 



1. To find a larger number, we must find the first "valley" (the pivot $i$) where the value drops.
2. We replace this "valley" value with the next highest value available on the "peak" (the swap).
3. Once we've increased the value at the valley, we want the rest of the path to be as flat/low as possible, so we turn the "peak" into a "plain" (the reverse).

### Complexity

| Label            | Worst          | Average          |
| :--------------- | :------------- | :--------------- |
| Time Complexity  | $O(n)$         | $O(n)$           |
| Space Complexity | $O(1)$         | $O(1)$           |

#### Time Complexity
We perform at most two linear scans and one reverse (which is another partial scan). Total operations are $O(n)$.

#### Space Complexity
The algorithm is entirely in-place. No additional data structures or recursive calls are utilized.

### Code

```java
class Solution {
    public void nextPermutation(int[] nums) {
        if (nums == null || nums.length <= 1) return;

        // 1. Find the first decreasing element from the right
        int i = nums.length - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }

        // 2. If the array isn't entirely descending
        if (i >= 0) {
            int j = nums.length - 1;
            // Find the successor to the pivot
            while (nums[j] <= nums[i]) {
                j--;
            }
            swap(nums, i, j);
        }

        // 3. Reverse the suffix to get the smallest lexicographical increase
        reverse(nums, i + 1);
    }

    private void reverse(int[] nums, int start) {
        int i = start, j = nums.length - 1;
        while (i < j) {
            swap(nums, i, j);
            i++;
            j--;
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```

## Caveats

- **Duplicates:** The comparison must be `nums[i] >= nums[i+1]` to correctly skip equal values.
- **Descending Order:** If you forget to reverse the suffix when $i = -1$, you fail the "last permutation" edge case.
- **Index Bounds:** Always check `i >= 0` before attempting to find $j$.

## Concepts to Think About

- **Lexicographical Generation:** This algorithm is the basis for generating all permutations in order.
- **Dictionary Order:** The logic mimics how words are ordered in a dictionary (e.g., "ABZ" -> "AC B").
- **Partial Sorting:** Reversing a descending suffix is a shortcut for sorting it in ascending order.
- **Pivot Logic:** This "pivot and swap" pattern appears in other problems like "Previous Permutation with One Swap."

## Logical Follow-up

Question: How would you find the **Previous Permutation**?
Solution: Reverse the logic. Find the first increasing element from the right ($nums[i] > nums[i+1]$), find the largest element smaller than it in the suffix, swap, and then reverse the suffix (which will be in ascending order) to make it descending.

Question: How can you find the **k-th permutation** of $n$ numbers without generating all of them?
Solution: Use the **Factorial Number System**. Since there are $(n-1)!$ permutations starting with a specific digit, you can mathematically determine which digit belongs at each position by dividing $k$ by the current factorial.