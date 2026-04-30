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

## Binary Search: When to use `left < right` (The Squeeze vs. Search)

- Use `while (left <= right)` when you have an **early return** (`if nums[mid] == target return mid`).
- Use `while (left < right)` when you are **narrowing down** to a specific index (like the minimum or a peak).

## The Search Pattern (`left <= right`)

- **Best for:** Finding an exact value.
- **Logic:** If `nums[mid]` isn't the target, discard it completely (`mid + 1`, `mid - 1`).
- **Exit:** You either find it and return, or you finish with $left > right$ (not found).

## The Squeeze Pattern (`left < right`)

- **Best for:** Finding a transition point, minimum, or single element.
- **Logic:** The `right = mid` update keeps `mid` in the search space because it _could_ be the answer.
- **Exit:** Terminate when only one element remains ($left == right$).

## Critical Rule for `left < right`

When using `right = mid`, you **must** ensure the loop terminates. If $left$ and $right$ are adjacent, $mid$ will always equal $left$.

- If your logic moves $left$ forward (`left = mid + 1`), you are safe.
- If your logic moves $right$ to $mid$, you are safe (because $right$ becomes $left$ and the loop ends).

### Concepts to Think About

- **Lower Bound:** Finding the first element $\ge$ target always uses `left < right`.
- **Search Space:** Does `left < right` work if the target might NOT be in the array? (Yes, but you need a final check: `if (nums[left] == target)` after the loop).

- **Search Space Size:** `left < right` ensures the search space is always $\ge 2$ elements.
- **Convergence:** The "squeeze" approach is more mathematically robust for finding transition points in functions or rotated arrays.

# Identifying Binary Search

1. **Search Space:** Can I define a `low` and `high` for the final answer?
2. **The Predicate:** Can I write a `boolean isPossible(x)` function that runs in $O(N)$?
3. **The Flip:** Does `isPossible(x)` go from `false, false, false...` to `true, true, true...`?
