---
tags:
  - cc
  - array
  - dynamic-programming
  - kadanes-algorithm
---

# Maximum Subarray (Kadane's Algorithm)

## Question
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

## Solution

### Pattern
**Dynamic Programming / Greedy (Kadane's)**

### How to Identify
* The problem asks for an "optimal" contiguous segment (subarray).
* The property (sum) can be built incrementally.
* A negative sum "resets" the potential of future subarrays.

### Description
We traverse the array while maintaining a `currSum`. For each element, we add it to `currSum`. If `currSum` ever becomes higher than our `maxSum`, we update `maxSum`. Crucially, if `currSum` drops below zero, we reset it to zero. Why? Because any subarray starting with a negative prefix would be improved by simply dropping that prefix and starting fresh.



### The Intuition: "The Fresh Start"
Imagine you are a gambler. You're tracking your net winnings/losses throughout the day. If at any point your total losses exceed your total gains (a negative `currSum`), you are better off "forgetting" everything that happened so far and starting your count from zero with the next bet. You keep track of the highest peak your wallet ever hit during the day—that's your `maxSum`.

### Complexity

| Label | Worst | Average |
| :--- | :--- | :--- |
| Time Complexity | $O(n)$ | $O(n)$ |
| Space Complexity | $O(1)$ | $O(1)$ |

### Code

```java
class Solution {
    public int maxSubArray(int[] nums) {
        // Defensive check for Google-level production code
        if (nums == null || nums.length == 0) return 0;

        int currSum = 0;
        int maxSum = Integer.MIN_VALUE;

        for (int num : nums) {
            currSum += num;
            
            // Update global maximum before potential reset
            if (currSum > maxSum) {
                maxSum = currSum;
            }
            
            // If the current path is a net loss, abandon it
            if (currSum < 0) {
                currSum = 0;
            }
        }

        return maxSum;
    }
}
```

## Concepts to Think About

- Return Indices: How would you modify this to return the start and end indices of the subarray? (Hint: Track tempStart whenever currSum resets).
- The All-Negative Case: Why does the order of maxSum update and currSum < 0 check matter?
- Divide and Conquer: Can this be solved in O(nlogn)? (Hint: This is a classic example of the "Maximum Crossing Subarray" problem).
- 2D Extension: How would you find the maximum sum rectangle in a 2D matrix? (Hint: It involves running Kadane's on columns).

---

### **Normal Logical Follow-up**

**Question:** "The current code only returns the sum. Can you modify it to return the actual subarray or at least the `[start, end]` indices of that subarray?"

**Solution Logic:** You need three extra variables: `start`, `end`, and `tempStart`. 
1.  Initialize all to `0`. 
2.  Whenever you reset `currSum = 0`, set `tempStart = i + 1`. 
3.  Whenever you update `maxSum`, update `start = tempStart` and `end = i`.

---