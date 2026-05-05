---
tags:
  - cc
  - dynamic-programming
  - greedy
---

# Maximum Product Subarray

## Question

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest product and return that product.

Example:
Input: `nums = [2, 3, -2, 4]`
Output: `6` (Subarray: `[2, 3]`)

## Solution

### Pattern

**Prefix and Suffix Scan (Observation-based Greedy)**
The maximum product subarray is either a prefix product or a suffix product of a segment not containing any zeros.

### How to Identify

- Problem involves **contiguous subarrays**.
- Optimization of a **Product** (unlike sum, products flip signs with negative numbers).
- Presence of **Zeros** acting as delimiters.

### Description

Step-by-step explanation:

- We traverse the array from left to right (Prefix Product).
- We traverse the array from right to left (Suffix Product).
- During each step, we update our `maxProduct` with the current running product.
- **Invariant:** If we encounter a `0`, the product becomes `0`. Since we want the maximum product and a subarray cannot "cross" a zero (as it would make the product 0), we reset the running product back to `1` and continue.
- This effectively treats the array as multiple sub-arrays separated by zeros.



### The Intuition

Deep reasoning:
1. **No Negative Numbers:** The max product is just the product of all elements.
2. **Even Negative Numbers:** The max product is still the product of all elements.
3. **Odd Negative Numbers:** If there are an odd number of negatives (say 3), the max product will either be everything *before* the last negative or everything *after* the first negative.
4. **Zeros:** Any subarray containing a zero has a product of 0. Thus, zeros act as walls.

By scanning from both directions, we are essentially testing the "everything before the last negative" (Prefix) and "everything after the first negative" (Suffix) scenarios for every zero-bounded segment.

### Complexity

| Label            | Worst          | Average          |
| :--------------- | :------------- | :--------------- |
| Time Complexity  | $O(n)$         | $O(n)$           |
| Space Complexity | $O(1)$         | $O(1)$           |

#### Time Complexity
We perform two linear passes (or one pass with two pointers), visiting each element exactly once. 

#### Space Complexity
Only a few variables (`prefix`, `suffix`, `max`) are used. No additional data structures are required.

### Code

```java
class Solution {
    public int maxProduct(int[] nums) {
        int n = nums.length;
        double prefix = 1;
        double suffix = 1;
        double maxProduct = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            // Reset product if previous element was 0
            if (prefix == 0) prefix = 1;
            if (suffix == 0) suffix = 1;

            prefix *= nums[i];
            suffix *= nums[n - 1 - i];

            maxProduct = Math.max(maxProduct, Math.max(prefix, suffix));
        }

        return (int) maxProduct;
    }
}
```

## Caveats

- **Overflow:** Subarray products grow much faster than sums. In Java, `long` or `double` might be needed for intermediate calculations, though the result usually fits in `int` based on standard competitive constraints.
- **Single Element 0:** If the array is `[-2, 0, -1]`, the answer is 0. The initialization to `MIN_VALUE` and the reset logic handle this.

## Concepts to Think About

- **Kadane’s Variation:** Can you solve this by tracking `minEndingHere` and `maxEndingHere`? (Crucial for a follow-up).
- **Logarithmic Transformation:** Could you turn this into a Max Subarray Sum problem using `log(abs(x))`? (Think about signs!).
- **Sign Tracking:** The parity of negative numbers determines if the whole segment is positive or negative.
- **Zero as a Reset:** Why does a zero break the "chain"?
- **Handling Large Numbers:** Does `double` provide enough precision for integer products? (In most interview cases, yes, but worth mentioning).

## Logical Follow-up

Question: What if the array contains fractional numbers between 0 and 1?
Solution: The product logic stays the same, but the "maximum" might not involve more elements; multiplying by a fraction makes the product smaller. Kadane's variation handles this more robustly than prefix/suffix.

Question: What if you need to return the actual subarray, not just the product?
Solution: Store the indices whenever `maxProduct` is updated during the prefix/suffix scan.
