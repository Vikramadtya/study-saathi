---
tags:
  - cc
  - array
  - math
---

# Missing Number

## Question
Given an integer array `nums` of size $n$ containing distinct values in the range $[0, n]$, return the only number in the range that is missing from the array.

## Solution

### Pattern
**Mathematical Summation (Gauss) / Bitwise XOR**

#### How to Identify
* The values are in a strict range (e.g., $0$ to $n$ or $1$ to $n$).
* The array contains "distinct" values.
* Exactly one (or a fixed number) of elements are missing.

### Description
The most efficient way to find a single missing number in a continuous range is to calculate the **Expected Sum** of the range and subtract the **Actual Sum** of the elements present in the array. The difference is the missing value.



### The Intuition
Imagine you have a box meant to hold a set of numbered tiles from $0$ to $10$. If you know the total weight of all tiles should be $55$ grams, but when you weigh the tiles currently in the box, they only total $52$ grams, you immediately know the "3" tile is missing without even looking at the labels.

### Complexity

| Label            | Worst           | Average         |
| :--------------- | :-------------- | :-------------- |
| Time Complexity  | $O(n)$          | $O(n)$          |
| Space Complexity | $O(1)$          | $O(1)$          |

### Code

```java
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        
        // Using long to prevent overflow during calculation
        // Formula: n * (n + 1) / 2
        long expectedSum = (long) n * (n + 1) / 2;
        long actualSum = 0;
        
        for (int num : nums) {
            actualSum += num;
        }
        
        return (int) (expectedSum - actualSum);
    }
}
```

## Concepts to Think About

- The XOR Magic: You can solve this using the property that x⊕x=0 and x⊕0=x. If you XOR all numbers from 0 to n and then XOR that result with every number in the array, the duplicates cancel out, leaving only the missing number. Why is this safer than the Sum method?
- Overflow Handling: If you aren't allowed to use long, how could you modify the sum loop to prevent overflow? (Hint: subtract as you go: sum += (i - nums[i])).
- Cyclic Sort: This problem can also be solved using the Cyclic Sort pattern, where you try to place every number i at nums[i]. After sorting, the first index i where nums[i] != i is your missing number. When would you prefer this over the Math approach?
- Multiple Missing Numbers: If the array was missing two numbers, would the Sum method still work? (Hint: You would need a second equation, like the sum of squares, to solve for two variables).
- Binary Search: If the input array was sorted, could you find the missing number faster than O(n)? (Hint: Look for the first index i where `nums[i] != i$ using Binary Search).