---
tags:
  - cc
  - binary-search
  - array
---

# Peak Element Discovery

## Question
Given an array `arr`, find a peak element (an element strictly greater than its neighbors). Neighbors outside the array bounds are considered $-\infty$. Return the index of **any** peak.

## Solution

### Pattern
**Binary Search on Unsorted Data**
Typically, Binary Search requires a sorted array. However, it can be applied to unsorted data if we can determine a **directional property** (like a slope) that guarantees the existence of the answer in one half.

### How to Identify
- **Local Property:** The condition depends only on immediate neighbors ($arr[i-1] < arr[i] > arr[i+1]$).
- **Multiple Answers:** The problem asks for "any" valid solution rather than "all."
- **Efficiency Constraint:** $O(\log n)$ is required on an unsorted input.

### Description
Step-by-step explanation:

1.  Initialize `left = 0` and `right = n - 1`.

2.  Calculate `mid`.

3.  **Compare `mid` with the next element (`mid + 1`):**
    - If `arr[mid] < arr[mid + 1]`: You are currently on an **upward slope**. Because the array ends at $-\infty$, there must eventually be a peak to the right. Set `left = mid + 1`.
    - If `arr[mid] > arr[mid + 1]`: You are on a **downward slope** or at a **peak**. There must be a peak to the left (potentially `mid` itself). Set `right = mid`.

4.  When `left == right`, the search space has converged to a peak.



### The Intuition
**Hill Climbing in the Dark:** Imagine you are on a mountain at night. You want to find *any* peak. You feel the ground at your current spot (`mid`) and one step to the right (`mid + 1`). 
- If the ground to the right is higher, keep going right.
- If the ground to the right is lower, you are either at a peak or the peak was behind you.
Since the edges of the world are infinitely deep pits ($-\infty$), as long as you keep moving "up," you are guaranteed to find a summit.

### Complexity

| Label            | Worst          | Average          |
| :--------------- | :------------- | :--------------- |
| Time Complexity  | $O(\log n)$    | $O(\log n)$      |
| Space Complexity | $O(1)$         | $O(1)$           |

#### Time Complexity
The search space is divided by 2 in every iteration. For $n$ elements, we perform at most $\lceil \log_2 n \rceil$ comparisons.

#### Space Complexity
The algorithm uses iterative pointers, requiring no extra memory or recursion stack.

### Code

```java
class Solution {
    public int findPeakElement(int[] arr) {
        int left = 0;
        int right = arr.length - 1;

        // Use left < right to ensure mid + 1 is always valid
        while (left < right) {
            int mid = left + (right - left) / 2;

            // If mid is less than the next element, we are on an upward slope.
            // The peak must be to the right (excluding mid).
            if (arr[mid] < arr[mid + 1]) {
                left = mid + 1;
            } 
            // If mid is greater than the next element, we are on a downward slope.
            // The peak could be mid or to the left of mid.
            else {
                right = mid;
            }
        }

        // When left == right, we have converged to a peak index.
        return left;
    }
}
```

## Caveats
- **Adjacent Duplicates:** This specific $O(\log n)$ logic assumes $arr[i] \neq arr[i+1]$. If duplicates are allowed and a peak is defined as $arr[i-1] \le arr[i] \ge arr[i+1]$, the problem may require $O(n)$ in the worst case.
- **Strict Peak:** The definition $arr[i-1] < arr[i] > arr[i+1]$ means a plateau (e.g., `[1, 2, 2, 2, 1]`) technically has no peak under strict rules.

## Concepts to Think About
- **Why it works on unsorted data:** We don't need the whole array to be sorted; we only need a "gradient" to guide the binary search.
- **Binary Search on Answer:** This is a subset of a broader pattern where we search for a value/index that satisfies a specific condition in a search space.
- **Local vs. Global Optima:** This algorithm finds a local maximum, not necessarily the global maximum.

## Logical Follow-up

Question: How would you find a peak in a **2D Matrix** where a peak is greater than its top, bottom, left, and right neighbors?

Solution: Use a modified Binary Search. Find the maximum element in the middle column ($O(M)$). Compare it to its left and right neighbors. If it's smaller than the right neighbor, search the right half of the matrix. This yields $O(M \log N)$ complexity.



Question: What if there are **multiple peaks** and you need to find the **highest** one?

Solution: Binary Search will no longer work. You must perform a linear scan $O(n)$ because a local peak found by binary search could be much lower than the global maximum.
