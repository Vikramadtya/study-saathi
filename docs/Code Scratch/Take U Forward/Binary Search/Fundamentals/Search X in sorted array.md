---
tags:
  - cc
  - searching
  - binary-search
---

# Binary Search (The Gold Standard)

## Question
Given a sorted integer array `nums`, find the index of a specified `target`. Return the index if found, otherwise return -1.

## Solution

### Pattern
**Decrease and Conquer (Logarithmic Search)**

#### How to Identify
* The input is **sorted**.
* You need to find an element or a boundary.
* You are looking for a performance better than $\text{O}(n)$.

### Description
Binary Search works by repeatedly halving the search space. We compare the `target` to the middle element. If they match, we're done. If the target is smaller, we discard the right half; if larger, we discard the left.



[Image of binary search algorithm flow]


### The Intuition
Imagine looking for a name in a physical phone book. You don't start at page 1. You open the middle. If the name starts with 'M' and you're at 'S', you know the name is in the first half. You repeat this until you find the name or realize the person isn't in the book.

### Complexity

| Label | Worst | Average |
| :--- | :--- | :--- |
| Time Complexity | $\text{O}(\log n)$ | $\text{O}(\log n)$ |
| Space Complexity | $\text{O}(1)$ | $\text{O}(1)$ |

### Code

```java
class Solution {
    public int search(int[] nums, int target) {
        if (nums == null || nums.length == 0) return -1;

        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            // Prevent (left + right) / 2 overflow
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }
}
```

---

### Masterclass: Boundary Logic & Loop Conditions

One of the hardest things in Binary Search is knowing when to use `left < right` vs `left <= right`. Here is the L5 guide to never getting stuck:

| Scenario                | Loop Condition          | Search Space       | Update Logic                 | Exit State                       |
| :---------------------- | :---------------------- | :----------------- | :--------------------------- | :------------------------------- |
| **Finding Exact Value** | `while (left <= right)` | Inclusive $[L, R]$ | `L = mid + 1`, `R = mid - 1` | `L > R`, Target not found.       |
| **Finding Boundary**    | `while (left < right)`  | Half-Open $[L, R)$ | `L = mid + 1`, `R = mid`     | `L == R`, This is the candidate. |

#### 1. Inclusive Boundaries (`left <= right`)
Use this when you are looking for a **single specific value**.

- **Why:** If the search space is one element ($L=R$), you still want to check that element.
- **Movement:** Since you checked `mid` and it wasn't the target, you must exclude it: `mid + 1` and `mid - 1`.

#### 2. Exclusive Boundaries (`left < right`)
Use this when you are looking for a **transition point** or the "leftmost/rightmost" element that satisfies a condition.

- **Why:** The loop stops when $L=R$, which is usually the point where the condition flips.
- **Movement:** Often uses `right = mid` because `mid` might still be the answer you're looking for (the boundary).

### Follow-up

**Question:** "Given a sorted array that has been **rotated** at some pivot, find the index of a target. For example: `nums = [4,5,6,7,0,1,2], target = 0` should return `4`."

**Hint:** Even if rotated, at least one half (left or right) is always sorted. Use that sorted half to determine which direction to move.


**Question (Search in an Infinite Array):** "Imagine you are searching for a `target` in a sorted array, but you **don't know the size of the array**. There is no `.length` property. If you access an index out of bounds, it throws an exception or returns `Integer.MAX_VALUE`. How do you find the target in $\text{O}(\log \text{index})$ time?"

**Solution Logic:**

1.  **Exponential Backoff (Phase 1):** You need to find the "Right" boundary. Start with `right = 1`. If `nums[right] < target`, double it: `right = right * 2`.
2.  Once `nums[right] >= target`, you have found a range $[right/2, right]$ where the target must live.
3.  **Binary Search (Phase 2):** Perform standard Binary Search within that range.
* **Why this is L5:** It shows you can apply the "halving" logic in reverse to *expand* a search space before shrinking it. This is similar to how TCP congestion control works!
