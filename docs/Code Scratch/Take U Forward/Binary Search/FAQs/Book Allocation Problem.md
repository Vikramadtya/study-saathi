---
tags:
  - cc
  - binary-search
  - greedy
  - optimization
---

# Allocation of Books (Minimize Maximum Pages)

## Question
Given $n$ books with $nums[i]$ pages, allocate them to $m$ students such that:

1. Every student gets at least one book.
2. Every book is allocated to exactly one student.
3. The allocation is **contiguous**.
4. The **maximum number of pages** assigned to any student is **minimized**.

## Solution

### Pattern
**Binary Search on Answer Space** Instead of searching for a student or a book, we search for the **minimum possible "Maximum Capacity"** a student can have.

### How to Identify
- **Optimization Target:** "Minimize the maximum" or "Maximize the minimum."
- **Monotonicity:** If a student can finish their books within a capacity of $K$ pages, they can certainly do it with $K+1$.
- **Contiguity:** The requirement for contiguous allocation allows for a simple $O(n)$ greedy check.

### Description
Step-by-step explanation:

1. **Define the Range:**
    - **Lower Bound ($L$):** The maximum single book size (since someone *must* carry that book).
    - **Upper Bound ($R$):** The total sum of all pages (one student carries everything).
2. **Binary Search:**
     - Pick a "Guess" capacity `mid`.
     - Use a **Greedy** approach to see how many students are needed if no one can exceed `mid` pages.
3. **Greedy Check:**
     - Iterate through books, adding pages to a current student. If adding the next book exceeds `mid`, start a new student.
4. **Narrow the Search:**
     - If students needed $> m$, our `mid` is too small $\rightarrow L = mid + 1$.
     - If students needed $\le m$, our `mid` might be the answer, but try smaller $\rightarrow R = mid - 1$.



### The Intuition
Imagine a "Slider." On one end, every student carries exactly one book. On the other end, one student carries all books. We are moving a slider representing **"Maximum Load"** and checking: "Is this load feasible with only $m$ people?" As we slide the load down, eventually we reach a point where we need $m+1$ people. The point just before that is our optimal answer.



### Complexity

| Label            | Worst          | Average          |
| :--------------- | :------------- | :--------------- |
| Time Complexity  | $O(n \cdot \log(\sum - \max))$ | $O(n \cdot \log(\sum - \max))$ |
| Space Complexity | $O(1)$         | $O(1)$           |

#### Time Complexity
We perform a binary search over the range of total pages. Let $S = \sum nums$ and $M = \max(nums)$. The number of checks is $\log(S-M)$. Each check takes $O(n)$ time via a linear scan.

#### Space Complexity
No auxiliary space is used; only a few variables to track indices and sums.

### Code
```java
class Solution {
    private int getRequiredStudents(int[] nums, long maxCapacity) {
        int students = 1;
        long currentLoad = 0;
        
        for (int pages : nums) {
            if (currentLoad + pages > maxCapacity) {
                students++;
                currentLoad = pages;
            } else {
                currentLoad += pages;
            }
        }
        return students;
    }

    public int findPages(int[] nums, int m) {
        if (m > nums.length) return -1;

        long left = 0; // Minimum possible max pages
        long right = 0; // Maximum possible max pages
        
        for (int num : nums) {
            left = Math.max(left, num);
            right += num;
        }

        int result = (int) right;
        while (left <= right) {
            long mid = left + (right - left) / 2;
            
            // Greedy check: Can we do it with mid capacity?
            if (getRequiredStudents(nums, mid) <= m) {
                result = (int) mid;
                right = mid - 1; // Try smaller capacity
            } else {
                left = mid + 1; // Need more capacity
            }
        }
        return result;
    }
}
```

## Caveats
- **Non-Contiguous Allocation:** If books weren't contiguous, this would become the "Partition Problem" or "Multi-way Number Partitioning," which is NP-hard and requires Backtracking or DP.
- **Minimum Value:** The search must start at `max(nums)`, not `0`. If `mid` is less than the largest book, that book can never be assigned.

## Concepts to Think About
- **Aggressive Cows vs. Book Allocation:** One maximizes the minimum; the other minimizes the maximum. Both use BS on Answer Space.
- **Painters Partition Problem:** Identical logic.
- **Split Array Largest Sum:** Identical logic (LeetCode 410).
- **Precision:** If the inputs were floating point (e.g., allocating "time" or "gas"), we would use `while (right - left > 1e-7)` instead of `while (left <= right)`.

## Logical Follow-up

**Question:** How would you solve this if the array was too large to fit on a single machine?
**Solution:** (L5/L6 Response) Use a **MapReduce** style approach. The Binary Search logic remains on a coordinator node. The `getRequiredStudents` (Greedy check) is difficult to parallelize because it's contiguous. However, if we know the split points, we can distribute the array. Alternatively, we search for the answer on a coordinator and broadcast the `mid` to workers to validate their local chunks, but this requires careful coordination of "carry-over" pages between nodes.
