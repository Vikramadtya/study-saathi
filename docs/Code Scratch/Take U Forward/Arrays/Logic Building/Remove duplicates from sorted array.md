---
tags:
  - cc
  - array
  - two-pointers
---

# Remove Duplicates from Sorted Array

## Question
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place so that each unique element appears only once. Return the number of unique elements $k$.

Change the array such that the first $k$ elements contain the unique values in their original order. The remaining elements do not matter.

## Solution

### Pattern
**Two-Pointer: Slow and Fast Runner**

#### How to Identify
* The input array is **sorted**.
* You need to "filter" or "remove" elements in-place without extra space.
* The problem asks to maintain the relative order of the remaining elements.

### Description
Since the array is sorted, duplicates are always adjacent. We use a **slow pointer** $i$ to track the position of the last unique element found and a **fast pointer** $j$ to scan the array. Whenever $nums[j]$ is different from $nums[i]$, we have found a new unique element. We move it to $nums[i+1]$ and increment $i$.



### The Intuition
Imagine you are a quality control officer standing at a conveyor belt of items. You keep your left hand on the last "unique" item you've approved. Your right hand reaches out to check the next items coming down the belt. If the right hand finds an item identical to the one under your left hand, you discard it. If it finds a different item, you place it immediately next to your left hand and move your left hand to that new item.

### Complexity

| Label            | Worst           | Average         |
| :--------------- | :-------------- | :-------------- |
| Time Complexity  | $O(n)$          | $O(n)$          |
| Space Complexity | $O(1)$          | $O(1)$          |

### Code

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        // Perimeter Defense: Handle empty array
        if (nums == null || nums.length == 0) return 0;

        // i is the slow pointer (index of the last unique element)
        int i = 0;

        // j is the fast pointer (starts at the second element)
        for (int j = 1; j < nums.length; ++j) {
            // Compare the current element with the last known unique element
            if (nums[i] != nums[j]) {
                // Move to the next slot and update it
                i++;
                nums[i] = nums[j];
            }
        }

        // k unique elements found, where k is index + 1
        return i + 1;
    }
}
```

## Concepts to Think About

- The "At Most K" Variation: How would you modify this if the problem allowed each unique element to appear at most twice? (Hint: You would compare nums[j] with nums[i-1]).
- Stability: Why is this algorithm considered stable? Because it processes elements from left to right and maintains their original relative order in the "unique" section.
- Unsorted Arrays: If the array were not sorted, would this approach work? (No, you would need a HashSet or you'd have to sort it first).
- Branch Prediction: In an array with many duplicates, the nums[i] != nums[j] condition will often be false. How does the CPU's branch predictor handle this "mostly-false" condition compared to a random array?
- In-Place vs. New Array: What are the memory trade-offs of modifying the original array vs. returning a new one, especially when considering Garbage Collection (GC) in Java?
