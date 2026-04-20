---
tags:
  - cc
  - binary-search
  - array
---

# Search Insert Position

## Question
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

## Solution

### Pattern
**Lower Bound (The "First Greater or Equal" Position)**

#### How to Identify
* The array is sorted.
* You are looking for a specific value **OR** the position it "belongs" in.
* The problem can be rephrased as: "Find the first index $i$ such that $nums[i] \ge target$."

### Description
This is a standard Binary Search for a transition point. We look for the first element that is not smaller than our target. By the time our `left` and `right` pointers meet, they will point to either the target itself or the first element larger than the target (which is where the target should be inserted).



### Complexity

| Label | Worst | Average |
| :--- | :--- | :--- |
| Time Complexity | $O(\log n)$ | $O(\log n)$ |
| Space Complexity | $O(1)$ | $O(1)$ |

### Code (Streamlined L5 Version)

```java
class Solution {
    public int searchInsert(int[] nums, int target) {
        // L5 Insight: No need for early exit if-statements; 
        // the loop handles nums.length, 0, and out-of-bounds naturally.
        int left = 0;
        int right = nums.length;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] >= target) {
                // This could be the insertion point, look left for a smaller one
                right = mid;
            } else {
                // Too small, must insert somewhere to the right
                left = mid + 1;
            }
        }

        return left;
    }
}
```

## Concepts to Think About

- Redundancy vs. Performance: While an early return mid saves a few iterations, the standard lowerBound is often preferred for its mathematical robustness and ability to handle duplicates.
- The `right = nums.length` Choice: This is vital. If the target is larger than everything in the array, the loop must be able to return `nums.length`.
- Distinct vs. Duplicates: If the array had duplicates and the question asked for the last possible insertion point, how would the logic change? (Hint: Use upperBound logic).
- Library Equivalents: In Java, `Arrays.binarySearch` returns `-(insertion point) - 1` if the element isn't found. Understanding how to convert between library outputs and manual implementations is a key L5 skill.


---

### **Logical Follow-up**

**Question:** "Given a 2D matrix where each row is sorted and the first integer of each row is greater than the last integer of the previous row, return true if a `target` exists."

**Solution:** Treat the $M \times N$ matrix as a single $1 \text{D}$ array of length $M \times N$. 
* Binary search from `0` to `(M * N) - 1`. 
* Map the `mid` index back to 2D coordinates using `row = mid / N` and `col = mid % N`.

---

### **Google L5 Role Follow-up**

**Question (Search in a Bitonic Array):** "A Bitonic array is an array that is first strictly increasing and then strictly decreasing. Given a Bitonic array `nums` and a `target`, find the index of the `target` in $O(\log n)$ time."



**L5 Analysis & Solution:**
You cannot use standard Binary Search because the array is not monotonic.

1. **Find the "Peak":** Use Binary Search to find the maximum element (the point where the trend flips). A point `i` is a peak if `nums[i] > nums[i-1]` and `nums[i] > nums[i+1]`.
2. **Split the Search:**
    * Binary search for the target in the increasing left half.
    * If not found, binary search for the target in the decreasing right half (remember to flip your `>` and `<` logic for the decreasing part!).
3. **Why this is L5:** It requires composing multiple binary searches and identifying that "trend change" is just another predicate you can search for.




##### Key Differences for Binary Search

| Feature             | Bitonic Array                                                                               | Rotated Sorted Array                                                                                                 |
| :------------------ | :------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------- |
| **Trend**           | Increasing $\to$ Decreasing                                                                 | Sorted $\to$ Break $\to$ Sorted                                                                                      |
| **Crucial Point**   | **Peak:** The largest value.                                                                | **Pivot:** The point of discontinuity.                                                                               |
| **Monotonicity**    | Two monotonic halves (Inc / Dec).                                                           | Two monotonic halves (Part 1 / Part 2).                                                                              |
| **Search Strategy** | 1. Find Peak ($O(\log n)$) <br> 2. Binary search left half <br> 3. Binary search right half | Check which half is sorted ($O(\log n)$) <br> If `nums[L] <= nums[mid]`, left is sorted. <br> Else, right is sorted. |
