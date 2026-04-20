---
tags:
  - cc
  - binary-search
  - array
---

# Upper Bound (The "First Greater" Pattern)

## Question
Given a sorted array `nums` and a value $x$, find the **Upper Bound**: the smallest index $i$ such that $nums[i] > x$. If no such index exists, return the length of the array.

## Solution

### Pattern
**Binary Search: Predicate Transition (Strict Inequality)**

### How to Identify
* You are looking for the "end" of a range of identical values.
* You need the first element that is **strictly greater** than a target.
* The search space is monotonic.

### Description
We use the `left < right` template. The core predicate is `nums[mid] > x`. 
* If `true`: The current element *could* be the upper bound, so we move `right` to `mid` to check for smaller indices that also satisfy the condition.
* If `false`: The current element is $\le x$, so the upper bound must be to its right. We move `left` to `mid + 1`.



### The Intuition
Think of a line of people sorted by age. You want to find the first person who is **strictly older** than 25. You find someone who is 25; you keep looking to the right. You find someone who is 26; they might be the first one, or there might be another 26-year-old to their left. You narrow the search until you find the exact spot where the age flips from 25 to 26.

### Complexity

| Label            | Worst          | Average        |
| :--------------- | :------------- | :------------- |
| Time Complexity  | $O(\log n)$    | $O(\log n)$    |
| Space Complexity | $O(1)$         | $O(1)$         |

### Code

```java
class Solution {
    /**
     * Finds the first index i such that nums[i] > x.
     * Time: O(log n), Space: O(1)
     */
    public int upperBound(int[] nums, int x) {
        if (nums == null || nums.length == 0) return 0;

        int left = 0;
        int right = nums.length;

        while (left < right) {
            int mid = left + (right - left) / 2;

            // Predicate: Is the current element strictly greater than x?
            if (nums[mid] > x) {
                // Potential candidate found, look left for a smaller index
                right = mid;
            } else {
                // Element is <= x, answer must be further right
                left = mid + 1;
            }
        }

        return left; // left == right at termination
    }
}
```

### Logical Follow-up

**Question:** "Given a sorted array `nums`, return the **count** of a specific number $x$. For example, if `nums = [1, 2, 2, 2, 3]` and $x = 2$, the output should be $3$."

**Solution:** The count of $x$ is simply $\text{upperBound}(x) - \text{lowerBound}(x)$.
1.  Run `lowerBound` to find the first index of $x$.
2.  Run `upperBound` to find the first index *after* the last $x$.
3.  The difference is the total frequency. This is $O(\log n)$.


**Question (Koko Eating Bananas):** "There are $n$ piles of bananas, where the $i^{th}$ pile has $piles[i]$ bananas. Guards will be gone for $H$ hours. Koko can decide her bananas-per-hour eating speed $k$. Each hour, she chooses a pile and eats $k$ bananas from it. If the pile has less than $k$, she eats them all and doesn't eat any more during that hour. Koko wants to finish all bananas within $H$ hours. Return the **minimum** integer $k$ such that she can eat all the bananas within $H$ hours."

**L5 Analysis & Solution:**
This is a "Binary Search on Answer" problem, where the search space is the **possible speed $k$**.

1. **Search Space:** The minimum speed is $1$ (she must eat something). The maximum speed is $\max(piles)$ (at this speed, she finishes any pile in 1 hour).
2.  **Monotonicity:** If Koko can finish at speed $k$, she can definitely finish at speed $k+1$. If she can't finish at speed $k$, she definitely can't finish at any speed slower than $k$. This is a sorted predicate `[false, false, true, true]`.
3.  **Predicate Function:** Write a `canFinish(speed, H)` helper:
    - Iterate through piles: `hoursUsed += Math.ceil(piles[i] / speed)`.
    - Return `hoursUsed <= H`.
4. **Binary Search:** Use your **Lower Bound** template on the range $[1, \max(piles)]$ to find the smallest speed that returns `true`.

