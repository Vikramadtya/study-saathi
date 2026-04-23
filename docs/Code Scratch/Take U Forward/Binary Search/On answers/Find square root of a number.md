---
tags:
  - cc
  - binary-search
  - math
  - answer-space
---

# Floor Square Root

## Question

Given a positive integer $n$, find and return its square root. If $n$ is not a perfect square, return the floor value $\lfloor \sqrt{n} \rfloor$.

## Solution

### Pattern

**Binary Search on Answer Space**

### How to Identify

- The problem asks to find a value within a known range $[1, n]$.
- The search space is **monotonic**: if $x^2 > n$, then any $y > x$ will also have $y^2 > n$.
- You are looking for the "last" value that satisfies a condition ($x^2 \le n$).

### Description

We treat the integers from $1$ to $n$ as our "array." We check the middle value $mid$. If $mid^2 \le n$, then $mid$ is a candidate for the floor, and we search the right half for a potentially larger floor. If $mid^2 > n$, we search the left half.

### The Intuition

Think of it as a "Guess My Number" game. If I tell you my number squared is $20$, and you guess $5$ ($25$), you know $5$ is too high, and so is everything above it. If you guess $4$ ($16$), you know $4$ is a possible answer, but maybe $4.1, 4.2...$ or in this case, the next integer, could be better.

### Complexity

| Label            | Complexity  |
| :--------------- | :---------- |
| Time Complexity  | $O(\log n)$ |
| Space Complexity | $O(1)$      |

### Code (Streamlined L5 Version)

```java
class Solution {
    public int floorSqrt(int n) {
        // Base case for 0 and 1
        if (n < 2) return n;

        long left = 1, right = n;
        int ans = 0;

        while (left <= right) {
            long mid = left + (right - left) / 2;
            long square = mid * mid;

            if (square == n) return (int) mid;

            if (square < n) {
                // Potential floor found, look for a larger one
                ans = (int) mid;
                left = mid + 1;
            } else {
                // Too large, search lower
                right = mid - 1;
            }
        }
        return ans;
    }
}
```

## Concepts to Think About

- Monotonicity: This algorithm only works because $f(x)=x^2$ never decreases. If the function fluctuated, we couldn't discard half the range.
- Long vs Int: Always square the mid using long to prevent 32-bit overflow.
- Newton's Method: In a real-world Google system, we might use Newton-Raphson iteration for faster convergence on floating-point roots, but Binary Search is the preferred "interview" algorithm for integers.
- The "Search for Last True": This is a classic variation where we want the last index where a condition (square ≤n) is true.

## Logical Follow-up

**Question:** "How would you modify this to find the **Cube Root** ($\sqrt[3]{n}$) of an integer?"

**Solution:**
The logic is identical, only the "check" changes.

1.  Search range: $[1, n]$.
2.  Condition: `if (mid * mid * mid <= n)`.
3.  **L5 Caution:** $mid^3$ overflows even a `long` much faster than $mid^2$. For a cube root, you must be extremely careful or use `BigInteger` if $n$ is very large.

---

**Question (Precision Square Root):** "Now, find the square root of a **double** `n` with a precision of $10^{-7}$ (e.g., $sqrt(2) = 1.4142135$). How does the search range and termination condition change?"

**Analysis & Solution:**
Searching for a double is different because we no longer have discrete integer steps.

1.  **Range:** For $n \ge 1$, the range is $[1, n]$. However, for $0 < n < 1$, the square root is actually **larger** than $n$ (e.g., $\sqrt{0.25} = 0.5$). So the safe range is $[0, \max(1, n)]$.
2.  **Termination:** We don't use `left <= right`. Instead, we run the loop until the window is small enough: `while (right - left > 1e-9)`.
3.  **Iteration Limit:** Alternatively, running the loop exactly $100$ times will always provide enough precision for a `double` and avoids potential infinite loops due to floating-point precision errors.

```java
public double getPrecisionSqrt(double n) {
    double left = 0, right = Math.max(1, n);
    // 100 iterations is a common trick for guaranteed precision
    for (int i = 0; i < 100; i++) {
        double mid = left + (right - left) / 2;
        if (mid * mid <= n) {
            left = mid;
        } else {
            right = mid;
        }
    }
    return left;
}
```
