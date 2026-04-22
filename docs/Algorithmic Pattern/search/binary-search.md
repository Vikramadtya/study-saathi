# Binary Search

| Pattern                     | Purpose                            | Typical Use Cases                         |
| --------------------------- | ---------------------------------- | ----------------------------------------- |
| **Exact match**             | Find a specific target value       | Search in sorted array                    |
| **Lower bound**             | First value >= target              | Insertion point, minimum satisfying value |
| **Upper bound**             | First value > target               | Counting occurrences, range queries       |
| **Binary search on answer** | Find min/max satisfying a property | Parametric search, optimisation problems  |

## Standard Binary Search (Exact Match)

```java
public int search(int[] nums, int target) {
  int left = 0, right = nums.length-1;
  while(left <= right) {
       int mid = ( ( right -  left ) >> 1) + left;
       if(nums[mid] == target) return mid;
       if(nums[mid] < target) left = mid+1;
       else right = mid-1;
  }
  return -1;
}
```

## **Lower Bound** (First element > target)

The lower bound for a target value in a sorted array is the index of the first element that is greater than or equal to the target value. If the target value is present multiple times, the lower bound identifies the first occurrence. If the target value is not present, it indicates the position where the target value could be inserted while maintaining the sorted order.

```java
public int lowerBound(int[] nums, int target) {
    int left = 0, right = nums.length;
    while (left < right) {
        int mid = left + ((right - left) >> 1);
        if (nums[mid] < target) left = mid + 1;
        else right = mid;
    }
    return left; // Could be nums.length if all elements < target
}
```

## **Upper Bound** (First element ≥ target)

The upper bound for a target value in a sorted array is the index of the first element that is strictly greater than the target value. If the target value is present multiple times, the upper bound identifies the position after the last occurrence of the target value. If the target value is not present, it indicates the same insertion point as the lower bound.

```java
public int upperBound(int[] nums, int target) {
    int left = 0, right = nums.length;
    while (left < right) {
        int mid = left + ((right - left) >> 1);
        if (nums[mid] <= target) left = mid + 1;
        else right = mid;
    }
    return left; // Could be nums.length if all elements <= target
}

```

## **Binary Search on Answer** (Predicate-based)

Instead of searching an array, search the **answer space**

```java
public int binarySearchAnswer(int low, int high) {
    while (low < high) {
        int mid = low + ((high - low) >> 1);
        if (condition(mid)) {
            high = mid; // Look left
        } else {
            low = mid + 1; // Look right
        }
    }
    return low;
}
```

!!! note "Note"
    We can use _lower_ & _upper_ bound to find the occurrence count efficiently.

## Binary Search: When to use `left < right`

### The Rule of Thumb

- Use `while (left <= right)` when you have an **early return** (`if nums[mid] == target return mid`).
- Use `while (left < right)` when you are **narrowing down** to a specific index (like the minimum or a peak).

### The Invariant

For "Find Minimum," we maintain the invariant that **the minimum is always in the range $[left, right]$**.

1. **If `nums[mid] > nums[right]`:** The "cliff" is to the right. `mid` cannot be the minimum. 
   * New Range: $[mid + 1, right]$.
2. **If `nums[mid] <= nums[right]`:** `mid` could be the minimum, or the minimum is to its left. 
   * New Range: $[left, mid]$.



### Why `left < right` avoids Infinite Loops

If `left = 0` and `right = 1`:

- `mid = 0`.
- If the logic says `right = mid`, then `right` becomes `0`.
- Loop Condition `left < right` ($0 < 0$) is now **False**. The loop ends correctly.
- If you used `left <= right`, the loop would continue forever.

### Concepts to Think About

- **Search Space Size:** `left < right` ensures the search space is always $\ge 2$ elements.
- **Convergence:** The "squeeze" approach is more mathematically robust for finding transition points in functions or rotated arrays.
