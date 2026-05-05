
---
tags:
  - cc
  - divide-and-conquer
  - merge-sort
---

# Count Inversions in an Array

## Question

Given an integer array $nums$, return the total number of inversions. An inversion is defined as a pair of indices $(i, j)$ such that $i < j$ and $nums[i] > nums[j]$. The count represents how far an array is from being sorted.

## Solution

### Pattern

**Divide and Conquer (Merge Sort Variation)**
The problem is solved by augmenting the Merge Sort algorithm. During the merge step, when an element from the right half is smaller than an element from the left half, we can count multiple inversions simultaneously.

### How to Identify

- Questions involving counting pairs $(i, j)$ with specific order constraints and value comparisons.
- Problems asking how "unsorted" an array is.
- Situations where a brute-force $O(n^2)$ approach is obvious, but $O(n \log n)$ is required.

### Description

Step-by-step explanation:

1.  **Divide:** Split the array into two halves recursively until base cases (single elements) are reached.
2.  **Conquer:** Count inversions in the left half and right half independently.
3.  **Combine (Merge):** Maintain two pointers, one for each sorted half. 
    - If $nums[leftPointer] \leq nums[rightPointer]$, no inversion is found for that left element; move to the next.
    - If $nums[leftPointer] > nums[rightPointer]$, then because the left half is sorted, every element from $leftPointer$ to $mid$ is also greater than $nums[rightPointer]$.
4.  **Count:** Add $(mid - leftPointer + 1)$ to the total inversion count.
5.  **Merge:** Complete the standard sorting process to ensure subsequent parent calls receive sorted subarrays.



### The Intuition

Deep reasoning:
In a sorted array, the inversion count is 0. In Merge Sort, we are constantly "fixing" the order of elements. The number of inversions is exactly the number of "jumps" elements take to reach their sorted positions. By counting how many elements a smaller value from the right "passes" in the left half, we capture all inversions involving that element.

### Complexity

| Label            | Worst          | Average          |
| :--------------- | :------------- | :--------------- |
| Time Complexity  | $O(n \log n)$ | $O(n \log n)$ |
| Space Complexity | $O(n)$         | $O(n)$         |

#### Time Complexity
The algorithm follows the recurrence $T(n) = 2T(n/2) + O(n)$. Regardless of the input distribution, it consistently performs $O(n \log n)$ operations.

#### Space Complexity
$O(n)$ for the auxiliary array used during the merge process, plus $O(\log n)$ for the recursion stack depth.

### Code

```java
class Solution {
    public long numberOfInversions(int[] nums) {
        if (nums == null || nums.length < 2) return 0;
        
        // Pre-allocate temp array once to reduce memory allocation churn
        int[] temp = new int[nums.length];
        return mergeSort(nums, temp, 0, nums.length - 1);
    }

    private long mergeSort(int[] nums, int[] temp, int left, int right) {
        if (left >= right) return 0;

        // Overflow-safe midpoint calculation
        int mid = left + (right - left) / 2;

        long count = 0;
        count += mergeSort(nums, temp, left, mid);
        count += mergeSort(nums, temp, mid + 1, right);
        count += merge(nums, temp, left, mid, right);

        return count;
    }

    private long merge(int[] nums, int[] temp, int left, int mid, int right) {
        int i = left;      // Pointer for left half
        int j = mid + 1;   // Pointer for right half
        int k = left;      // Pointer for temp array
        long inversions = 0;

        while (i <= mid && j <= right) {
            if (nums[i] <= nums[j]) {
                temp[k++] = nums[i++];
            } else {
                // Since left half is sorted, all elements from i to mid 
                // are greater than nums[j].
                inversions += (mid - i + 1);
                temp[k++] = nums[j++];
            }
        }

        // Copy remaining elements
        while (i <= mid) temp[k++] = nums[i++];
        while (j <= right) temp[k++] = nums[j++];

        // Move sorted elements back to original array
        for (i = left; i <= right; i++) {
            nums[i] = temp[i];
        }

        return inversions;
    }
}
```

## Caveats

- **Stability:** The comparison `nums[i] <= nums[j]` is vital. Using `<` would incorrectly count identical elements as inversions.
- **Large Inputs:** Always use `long` for the count; `int` will overflow for $n > 65,536$ in a worst-case scenario (descending order).
- **Data Modification:** This algorithm sorts the input array in-place. If the original order must be preserved, a copy must be made first.

## Concepts to Think About

- **Binary Indexed Tree (Fenwick Tree):** Can also solve this in $O(n \log n)$ by processing elements as a frequency array.
- **Sorted List / AVL Trees:** Inserting into a balanced BST and counting elements to the right can also count inversions.
- **Relationship to Bubble Sort:** The inversion count is equal to the number of adjacent swaps Bubble Sort would perform.
- **Standardized Space:** Why is $O(n)$ space necessary for merging? (Hint: In-place merging exists but is $O(n^2)$ or extremely complex).

## Logical Follow-up

Question: What if we need to count **"Significant Inversions"** where $nums[i] > 2 \cdot nums[j]$?

Solution: This is **Reverse Pairs** (LeetCode 493). You can still use the Merge Sort pattern, but you must perform the counting in a separate pass before the merge step because the $2 \cdot nums[j]$ condition breaks the standard merge logic.

Question: Can we solve this in $O(n \log n)$ time with $O(1)$ auxiliary space?

Solution: Only if we use an in-place merge sort (like the "Gap Method" or Block Merge Sort), which are significantly more complex and often have higher constant factors. In a standard interview, $O(n)$ is the expected space complexity.