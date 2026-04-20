---
tags:
  - cc
  - array
  - hash-table
  - google-l5
---

# Two Sum: The Complement Pattern

## Question
Given an array `nums` and a `target`, return indices of two numbers that add up to `target`. Each input has exactly one solution; you cannot use the same element twice.

## Solution

### Pattern
**Hash Map: One-Pass Complement Search**

#### How to Identify
* You need to find a "pair" based on a relationship ($A + B = Target$).
* You need to find values or indices in $O(n)$ time.
* The "Complement" ($Target - Current$) is the key to avoiding nested loops.

### Description
We iterate through the array once. For each element $x$, we calculate its complement $y = Target - x$. We check if $y$ exists in our Hash Map. If it does, we've found our pair. If not, we store $x$ and its index in the map and continue.



### The Intuition
Imagine you are at a party looking for a dance partner. Instead of walking around asking everyone "Will you dance?", you go to the host (the Hash Map) and ask, "Is there someone here who specifically wants to dance with a person of my height?" If the host says yes, you're done. If not, you tell the host, "I'm this height; tell the next person who asks for me that I'm over by the snacks."

### Complexity

| Label            | Worst | Average |
| :--------------- | :---- | :------ |
| Time Complexity  | $O(n)$ | $O(n)$  |
| Space Complexity | $O(n)$ | $O(n)$  |

### Code (Optimized)

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        if (nums == null || nums.length < 2) return new int[0];

        // L5 Tip: Pre-size the map to avoid rehashing
        Map<Integer, Integer> map = new HashMap<>((int)(nums.length / 0.75) + 1);

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            // Single lookup optimization
            Integer complementIndex = map.get(complement);
            
            if (complementIndex != null) {
                return new int[]{complementIndex, i};
            }
            
            map.put(nums[i], i);
        }

        return new int[0];
    }
}
```

## Concepts to Think About

- Sorted vs. Unsorted: If the array were sorted, could we do better? (Hint: Two Pointers, O(1) space).
- Memory Constraints: What if the array has 10 billion numbers and won't fit in memory? (Hint: Sharding or External Merge Sort).
- Collision Handling: How does your language of choice handle Hash Map collisions? (Java uses Linked Lists, then converts to Red-Black Trees for O(logn) worst-case).
- Duplicate Values: Does the Hash Map approach handle duplicates like nums = [3, 3], target = 6? (Yes, because the first 3 is stored before the second 3 is checked).

