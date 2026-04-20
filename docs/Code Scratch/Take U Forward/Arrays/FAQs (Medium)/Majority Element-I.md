---
tags:
  - cc
  - array
  - math
---

# Majority Element (Boyer-Moore Voting)

## Question
Given an integer array `nums` of size $n$, return the majority element. The majority element is defined as the element that appears more than $\lfloor n/2 \rfloor$ times. You may assume that the majority element always exists in the array.

## Solution

### Pattern
**Boyer-Moore Voting Algorithm**

#### How to Identify
* The problem asks for an element that appears more than **half** the time ($> n/2$).
* Constraints demand $O(n)$ time and $O(1)$ space.
* You are looking for a "dominant" value that can survive a process of elimination.

### Description
The algorithm maintains a `candidate` and a `count`. We process the array in a single pass:
1. If `count` is $0$, we pick the current element as our new `candidate`.
2. If the current element matches the `candidate`, we increment `count` (it "gains power").
3. If it doesn't match, we decrement `count` (it "loses power").

Because the majority element appears more than $n/2$ times, it will mathematically outlast all other elements combined.



### The Intuition
Think of this as a **Battle Royale**. Every element belongs to a "tribe." When two people from different tribes meet, they fight and both are eliminated ($count--$). When two people from the same tribe meet, they join forces ($count++$). Since the majority tribe has more members than all other tribes combined, at least one member of the majority tribe is guaranteed to be the last one standing, even if every other tribe specifically targeted them.

### Complexity

| Label            | Worst           | Average         |
| :--------------- | :-------------- | :-------------- |
| Time Complexity  | $O(n)$          | $O(n)$          |
| Space Complexity | $O(1)$          | $O(1)$          |

### Code

```java
class Solution {
    public int majorityElement(int[] nums) {
        // Defensive Check
        if (nums == null || nums.length == 0) return -1;

        int candidate = 0;
        int count = 0;

        for (int num : nums) {
            // Step 1: If count is 0, we need a new candidate
            if (count == 0) {
                candidate = num;
            }

            // Step 2: Increment or Decrement based on the candidate
            if (num == candidate) {
                count++;
            } else {
                count--;
            }
        }

        return candidate;
    }
}
```

## Concepts to Think About

- Verification Pass: In real-world scenarios where a majority element isn't guaranteed, you must perform a second pass to count the occurrences of the candidate. If the count is ≤n/2, the candidate is "fake."
- Generalization (Boyer-Moore for n/3): If you need to find elements that appear more than n/3 times, you need two candidates and two counters. This is known as the Misra-Gries algorithm.
- Sorting Trick: If you sort the array, the majority element is always at index ⌊n/2⌋. Why? Because it spans more than half the array, it must cross the midpoint. This is O(nlogn) time but very simple to write.
- Bit Manipulation: You can determine each bit of the majority element by counting the frequency of 1s and 0s at each of the 32 bit positions. The majority bit at each position forms the majority element.
- Randomization: If you pick an element at random, there is a >50% chance it's the majority element. You can verify this in O(n). The expected number of attempts is constant, leading to an O(n) average-case algorithm.