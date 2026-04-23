---
tags:
  - cc
  - binary-search
  - math
  - nth-root
---

# Nth Root of M

## Question

Given two numbers $N$ and $M$, find the integer $N^{th}$ root of $M$. If the root is not an integer, return $-1$.

## Solution

### Pattern

**Binary Search on Answer Space** (Monotonic Function Search).

### How to Identify

- You are looking for a value $X$ such that $X^N = M$.
- The function $f(x) = x^N$ is strictly increasing for $x \ge 1$, which satisfies the requirement for Binary Search.

### Description

We search through the range $[1, M]$. For each `mid`, we calculate $mid^N$.

- If $mid^N = M$, we found the root.
- If $mid^N < M$, we need a larger $X$, so we move `left`.
- If $mid^N > M$, we need a smaller $X$, so we move `right`.

### The Intuition

Think of it as finding a specific point on a steep hill. Since the hill only goes up, if your current position is too high ($X^N > M$), you must move backward. If it's too low, you must move forward.

### Complexity

- **Time Complexity:** $O(\log M \cdot \log N)$.
  - $\log M$ for the Binary Search range.
  - $\log N$ for the Binary Exponentiation (Power function).
- **Space Complexity:** $O(1)$.

### Code (L5 "Overflow-Safe" Version)

```java
class Solution {
    public int NthRoot(int n, int m) {
        int low = 1, high = m;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            int midState = check(mid, n, m);

            if (midState == 1) return mid;
            if (midState == 0) low = mid + 1;
            else high = mid - 1;
        }
        return -1;
    }

    // Helper to calculate mid^n and compare with m
    // Returns: 1 if == m, 0 if < m, 2 if > m
    private int check(int mid, int n, int m) {
        long ans = 1;
        for (int i = 1; i <= n; i++) {
            ans = ans * mid;
            if (ans > m) return 2; // Stop early to prevent overflow
        }
        if (ans == m) return 1;
        return 0;
    }
}
```

## Concepts to Think About

- Integer vs. Double: When the problem asks for an integer root, avoid double to prevent precision errors.
- Early Exit Pattern: In the `check` function, we don't need the full value of $X^N$ if it's already larger than M. This is an L5 optimization.
- Binary Exponentiation: Could you make the check function $O(logN)$ instead of $O(N)$?
- Overflow Limits: What is the maximum value mid can take before $mid^N$ overflows a long? (In Java, `Long.MAX_VALUE` is $≈9×10^18$).

### Logical Follow-up

**Question:** "What if the problem asked for the $N^{th}$ root of $M$ as a decimal with $10^{-6}$ precision?"

**Solution:**

1.  Change the search range to `double`.
2.  The `while` condition becomes `while (high - low > 1e-7)`.
3.  The result would be `low` (or `high`).
4.  Binary search works perfectly for continuous values as long as the function remains monotonic.

**Question (Koko Eating Bananas):**
"Koko loves to eat bananas. There are `n` piles of bananas, the $i^{th}$ pile has `piles[i]` bananas. The guards will be back in `h` hours. Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile and eats `k` bananas from it. If the pile has less than `k` bananas, she eats them all and does not eat any more bananas during that hour. Return the minimum integer `k` such that she can eat all the bananas within `h` hours."

**Analysis & Solution:**
This is an L5 application of **Binary Search on Answer Space**.

1.  **Search Range:** The minimum speed is $1$, the maximum speed is $max(piles)$.
2.  **Monotonicity:** If Koko can finish at speed $K$, she can definitely finish at speed $K+1$. If she _cannot_ finish at speed $K$, she definitely cannot finish at speed $K-1$.
3.  **Check Function:** For a given speed `mid`, calculate the total hours: $\sum \lceil piles[i] / mid \rceil$.
4.  **Optimization:** This is the same "Answer Space" pattern. You are searching for the "Lower Bound" of speed $K$ such that `totalHours <= h`.
