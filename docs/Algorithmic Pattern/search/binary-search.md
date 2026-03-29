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



{% hint style="info" %}
We can use _lower_ & _upper_ bound to find the occurrence count efficiently.
{% endhint %}

