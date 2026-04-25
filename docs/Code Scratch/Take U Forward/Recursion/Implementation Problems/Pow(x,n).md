---
tags:
  - cc
  - binary-exponentiation
  - recursion
  - math
---

# Pow(x, n) - Binary Exponentiation

## Question

Implement `pow(x, n)`, which calculates $x^n$. Handle negative exponents and potential integer overflows.

## Solution

### Pattern

**Binary Exponentiation (Divide and Conquer)**

### How to Identify

- Calculating large powers in logarithmic time.
- The problem can be broken down: $x^n = (x^{n/2})^2$ for even $n$, and $x \cdot (x^{n/2})^2$ for odd $n$.

### Description

Instead of multiplying $x$, $n$ times, we square the base and halve the exponent at each step. This reduces the number of multiplications from $n$ to $\log n$.

### The Intuition

If you want to calculate $2^8$, you don't do $2 \times 2 \times 2...$. You realize $2^8 = (2^4)^2$. Then $2^4 = (2^2)^2$. You only need 3 multiplications instead of 7.

### Complexity

- **Time Complexity:** $O(\log n)$
- **Space Complexity:** $O(\log n)$ for recursive, $O(1)$ for iterative.

### Code (L5 Robust Version)

```java
class Solution {
    public double myPow(double x, int n) {
        // Use long to prevent Integer.MIN_VALUE overflow
        long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }
        return fastPow(x, N);
    }

    private double fastPow(double x, long n) {
        if (n == 0) return 1.0;

        double half = fastPow(x, n / 2);

        if (n % 2 == 0) {
            return half * half;
        } else {
            return half * half * x;
        }
    }
}
```

## Concepts to Think About

- Iterative vs Recursive: Iterative is preferred at Google to save stack memory.
- Precision: When x is very small and n is very large, the result might underflow to 0.
- Bit Manipulation: `n / 2` can be written as `n >> 1` and `n % 2 == 1` as `(n & 1) == 1` .

## Logical Follow-up

**Question:** "Can you rewrite this iteratively to achieve $O(1)$ space complexity?"

**Solution:**
In the iterative version, we keep a `result` variable. Every time the current exponent is odd, we multiply the `result` by the current `x`. We then square `x` and halve the exponent regardless.

```java
public double myPow(double x, int n) {
    long N = n;
    if (N < 0) {
        x = 1 / x;
        N = -N;
    }
    double ans = 1;
    while (N > 0) {
        if ((N & 1) == 1) ans *= x;
        x *= x;
        N >>= 1;
    }
    return ans;
}
```

**Question:** "In modern cryptography (like RSA), we calculate (x^n) % m where x, n, and m are 2048-bit integers. How would you modify your algorithm, and why is double no longer an option?"

**Solution:**

- **Absolute Precision:** Cryptography requires **integer precision**. A `double` has a limited number of significant bits (53 bits for a 64-bit double). Rounding even a single bit would destroy the entire encryption key.
- **BigInteger:** We would use `java.math.BigInteger` or a similar library to handle numbers far larger than 2^64.
- **Property of Modulo:** To keep the intermediate results from becoming millions of digits long, we apply the modulo at **every** multiplication step:
  `(a * b) % m = ((a % m) * (b % m)) % m`
- **Efficiency:** The O(log n) logic remains the same, which is why RSA encryption is fast enough for web traffic.
