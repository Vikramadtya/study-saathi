---
tags:
  - cc
  - array
  - two-pointers
  - sorting
---

# 3Sum: The Sorting + Two-Pointer Pattern

## Question
Given an integer array `nums`, return all unique triplets $[nums[i], nums[j], nums[k]]$ such that their sum is exactly zero.

## Solution

### Pattern
**Sorting + Two-Pointer (Outer Loop + Inner Scan)**

#### How to Identify
* You need to find a combination of **three** elements.
* The result set must not contain **duplicate triplets**.
* The input is unsorted, but the problem allows for $O(n^2)$ time.

### Description
First, we **sort** the array. We then iterate through the array with a pointer $i$. For each $i$, we treat it as a fixed value and solve the **Two Sum** problem for the remaining target ($-nums[i]$) using two pointers ($j$ at $i+1$ and $k$ at the end). To avoid duplicates, we skip any value for $i, j, \text{ or } k$ that is the same as its predecessor.



### The Intuition
Imagine you are trying to balance a scale with three weights to reach exactly zero. You pick the first weight (pointer $i$). Now you just need two other weights that perfectly counter-balance $i$. Because you lined up your weights by size (sorting), if your current sum is too heavy, you grab a smaller weight from the right; if it's too light, you grab a larger one from the left.

### Complexity

| Label | Worst | Average |
| :--- | :--- | :--- |
| Time Complexity | $O(n^2)$ | $O(n^2)$ |
| Space Complexity (Aux) | $O(\log n)$ | $O(\log n)$ |

> **Note:** Time is $O(n \log n)$ for sorting + $O(n^2)$ for the nested loops. Space is for the sorting stack.

### Code

```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums == null || nums.length < 3) return res;

        Arrays.sort(nums); // O(n log n)

        for (int i = 0; i < nums.length - 2; i++) {
            // Early Exit: If the smallest number is > 0, sum can never be 0
            if (nums[i] > 0) break;

            // Skip duplicate values for the first element
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int j = i + 1;
            int k = nums.length - 1;

            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];

                if (sum == 0) {
                    res.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    
                    // Skip duplicates for second and third elements
                    while (j < k && nums[j] == nums[j + 1]) j++;
                    while (j < k && nums[k] == nums[k - 1]) k--;
                    
                    j++;
                    k--;
                } else if (sum < 0) {
                    j++; // Need a larger value
                } else {
                    k--; // Need a smaller value
                }
            }
        }
        return res;
    }
}
```

## Concepts to Think About

- Why Sort? Sorting allows us to use the Two-Pointer technique. Without sorting, we would need a HashSet and would struggle significantly with duplicate triplet detection.
- The "Skip" Logic: Why do we check nums[i] == nums[i-1] but nums[j] == nums[j+1]? (It depends on the direction of pointer movement to ensure we don't skip the first instance of a valid number).
- 3Sum Closest: How would you modify this if you needed to find the triplet sum closest to a target? (Hint: Maintain a minDiff variable).
- Memory Management: In a very large array, List<List<Integer>> creates many small objects. If returning a 2D primitive array int[][] would be more memory-efficient.

