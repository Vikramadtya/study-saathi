---
tags:
  - cc
  - array
  - two-pointers
---

# Rearrange Array Elements by Sign

## Question
Given an integer array `nums` of even length with an equal number of positive and negative integers, rearrange the array so that:
1. Every consecutive pair has opposite signs.
2. The relative order of same-signed integers is preserved.
3. The array begins with a positive integer.

## Solution

### Pattern
**Multi-Pointer Indexing (Fixed-Step Runners)**

#### How to Identify
* The problem requires placing elements into specific slots based on a property (like parity or sign).
* The output format is predictable (e.g., "Even indices must be X, Odd indices must be Y").
* You need to preserve the original relative order (Stability).

### Description
We initialize two pointers representing the next available indices for positive and negative numbers. Since the array must start with a positive number and alternate, positive numbers will always occupy **even indices** ($0, 2, 4, \dots$) and negative numbers will always occupy **odd indices** ($1, 3, 5, \dots$). We iterate through the input once and place each number into its designated index in a new result array.



### The Intuition
Think of two separate lines of people—one line of people wearing blue shirts (positive) and one line wearing red shirts (negative). You have a row of chairs. You want to seat them so they alternate colors, starting with blue. You walk down the hallway, see a blue shirt, and tell them to take the next available "even-numbered" chair. You see a red shirt and tell them to take the next available "odd-numbered" chair.



### Complexity

| Label | Worst | Average |
| :--- | :--- | :--- |
| Time Complexity | $O(n)$ | $O(n)$ |
| Space Complexity | $O(n)$ | $O(n)$ |

> **Note:** The space is $O(n)$ because we must allocate a new array to maintain the relative order while rearranging.

### Code

```java
class Solution {
    public int[] rearrangeArray(int[] nums) {
        // Perimeter Defense
        if (nums == null || nums.length < 2) return nums;

        int n = nums.length;
        int[] result = new int[n];
        
        // Pointers for the next available even (positive) and odd (negative) slots
        int posIdx = 0;
        int negIdx = 1;

        for (int num : nums) {
            if (num > 0) {
                result[posIdx] = num;
                posIdx += 2; // Move to next even slot
            } else {
                result[negIdx] = num;
                negIdx += 2; // Move to next odd slot
            }
        }

        return result;
    }
}
```

## Concepts to Think About

- Stability: This approach is "stable" because we process nums from left to right. Why is it impossible to do this in O(1) space and O(n) time while remaining stable? (Look up "Stable In-Place Partitioning").
- Unequal Counts: How would your logic change if the number of positive and negative integers were not equal? You would likely need to fill the remaining slots with whatever numbers are left over at the end of the array.
- Follow-up - In-place (Unstable): If the interviewer says "I don't care about the original order, just alternate the signs in O(1) space," how would you use a two-pointer approach to swap elements in-place?
- Data Streams: If nums was a stream of data (too large to fit in an array), could you still produce an alternating output? (Hint: You would need two Queues to buffer the "wrong-signed" numbers until their slot comes up).
