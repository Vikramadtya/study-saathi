---
tags:
  - cc
  - array
  - suffix-properties
---

# Leaders in an Array

## Question
Given an integer array `nums`, return a list of all the **leaders** in the array. A leader is an element that is strictly greater than all elements to its right. The rightmost element is always a leader. The result must be in the original order of appearance.

## Solution

### Pattern
**Suffix Maximum / Right-to-Left Scan**

#### How to Identify
* The problem involves comparing an element with everything to its **right**.
* The condition depends on the "Suffix" of the array.
* A brute force would involve nested loops ($O(n^2)$), but a reverse scan can reduce it to linear time.

### Description
Instead of looking right for every element, we look from the right and maintain a "Running Maximum." As we move left, any element larger than our current maximum is a leader. Once a leader is found, we update the running maximum to this new value.



### The Intuition
Imagine you are standing at the end of a line of people of different heights, looking toward the beginning. You can only see people who are taller than everyone you've already seen. The first person (rightmost) is always visible. If the next person is shorter, they are hidden. If they are taller, they become a new "leader" and hide everyone shorter behind them.

### Complexity

| Label | Worst | Average |
| :--- | :--- | :--- |
| Time Complexity | $O(n)$ | $O(n)$ |
| Space Complexity (Auxiliary) | $O(1)$ | $O(1)$ |
| Space Complexity (Total) | $O(n)$ | $O(n)$ |

> **Note:** We traverse the array once ($O(n)$) and reverse the result list ($O(n)$), resulting in a linear time complexity.

### Code

```java
class Solution {
    public List<Integer> leaders(int[] nums) {
        // Perimeter Defense
        if (nums == null || nums.length == 0) return new ArrayList<>();

        List<Integer> result = new ArrayList<>();
        int n = nums.length;
        
        // The rightmost element is always a leader
        int currentMax = nums[n - 1];
        result.add(currentMax);

        // Scan from right-to-left starting from the second-to-last element
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] > currentMax) {
                result.add(nums[i]);
                currentMax = nums[i];
            }
        }

        // The leaders were found in reverse order; restore original order
        Collections.reverse(result);

        return result;
    }
}
```

## Concepts to Think About

- Strictly Greater vs. Greater or Equal: If the problem allowed equal values, how would the > sign change? Would the rightmost still be a leader?
- Monotonic Stack: This problem is a precursor to the "Next Greater Element" problem. Could you solve this using a Stack? (Hint: A monotonic decreasing stack can keep track of leaders).
- Stream Processing: If you were receiving these numbers one by one from a live stream, could you still identify leaders in O(1) auxiliary space? (Hint: No, because you wouldn't know what's coming to the right yet).
- Suffix Max Array: You could pre-calculate a suffixMax array where suffixMax[i] stores the maximum value from i to n-1. How does this change the space complexity?
- Space Trade-offs: If the interviewer forbids Collections.reverse(), how could you use a Deque or an array with two pointers to build the result in the correct order from the start?
