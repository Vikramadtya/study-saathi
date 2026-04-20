---
tags:
  - cc
  - array
  - two-pointers
---

# Move Zeroes

## Question
Given an integer array `nums`, move all the $0$'s to the end of it while maintaining the relative order of the non-zero elements. This must be done **in-place**.

## Solution

### Pattern
**Two-Pointers: Read-Write Strategy**

#### How to Identify
* You need to reorder elements based on a specific property (e.g., "is zero").
* The relative order of the "other" elements must stay the same.
* In-place modification is required ($O(1)$ space).

### Description
We maintain two pointers:
1.  **Read Pointer (`j`)**: Iterates through every element in the array.
2.  **Write Pointer (`i`)**: Keeps track of the next position where a non-zero element should be placed.

Whenever the Read Pointer finds a non-zero element, it "sends" it to the Write Pointer's position. By swapping or overwriting, we ensure all non-zeros accumulate at the front.



### The Intuition
Imagine you are sorting a shelf of books where some are missing (empty gaps = zeros). Instead of picking up every book, you just walk from left to right. Every time you see a book, you slide it as far to the left as possible into the first available "gap." By the time you reach the end, all the books are bunched up on the left, and all the gaps have naturally moved to the right.

### Complexity

| Label            | Worst           | Average         |
| :--------------- | :-------------- | :-------------- |
| Time Complexity  | $\text{O}(n)$   | $\text{O}(n)$   |
| Space Complexity | $\text{O}(1)$   | $\text{O}(1)$   |

### Code

```java
class Solution {
    public void moveZeroes(int[] nums) {
        // Perimeter Defense
        if (nums == null || nums.length <= 1) return;

        // i is the 'Write' pointer (tracks where the next non-zero goes)
        int i = 0;

        // j is the 'Read' pointer (scouts the array)
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != 0) {
                // If we found a non-zero, swap it with the element at the Write pointer
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                
                // Move the Write pointer forward
                i++;
            }
        }
    }
}
```