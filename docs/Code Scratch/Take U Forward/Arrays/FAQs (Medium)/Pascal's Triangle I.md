---
tags:
  - cc
  - math
  - dynamic-programming
---

# Pascal's Triangle: Find a Specific Element

## Question
Given two integers $r$ (row) and $c$ (column), return the value at that position in Pascal's Triangle using 1-based indexing.



## Solution

### Pattern
**Combinatorial Optimization ($\binom{n}{k}$)**

### How to Identify
* The problem asks for a **single** element in Pascal's Triangle.
* You need a solution better than $O(r \times c)$ time or space.
* The structure follows the additive property: $P(r, c) = P(r-1, c-1) + P(r-1, c)$.

### Description
While you can build the triangle using DP, the value at Row $r$ and Column $c$ is mathematically equivalent to the "nCr" formula (combinations). Specifically:
$$\text{Value} = \binom{r-1}{c-1} = \frac{(r-1)!}{(c-1)! \times ((r-1)-(c-1))!}$$

To calculate this in $O(c)$ time and $O(1)$ space without calculating massive factorials, we use the multiplicative formula:
$$\binom{n}{k} = \frac{n}{1} \times \frac{n-1}{2} \times \frac{n-2}{3} \dots \text{for } k \text{ terms}$$

### The Intuition
Think of Pascal's Triangle as a map of "paths." To get to Row $r$, Column $c$, you must make a series of "down-left" or "down-right" choices. The number of ways to reach a specific spot is exactly the number of ways to choose $c-1$ "right turns" out of $r-1$ total steps.



### Complexity

| Label | Worst | Average |
| :--- | :--- | :--- |
| Time Complexity | $O(c)$ | $O(c)$ |
| Space Complexity | $O(1)$ | $O(1)$ |

> **Note:** The time complexity is proportional to the column index $c$ because we only need to perform $c$ multiplications to find the combination value.

### Code (The "Google" Optimized Way)

```java
class Solution {
    public int pascalTriangleI(int r, int c) {
        // Row r, Column c (1-indexed) maps to nCr where n = r-1, r = c-1
        return (int) nCr(r - 1, c - 1);
    }

    private long nCr(int n, int r) {
        // Optimization: nCr is symmetric, pick the smaller r for fewer iterations
        if (r > n / 2) r = n - r;
        
        long res = 1;
        for (int i = 0; i < r; i++) {
            // Multiplicative formula: (n * n-1 * n-2...) / (1 * 2 * 3...)
            res = res * (n - i);
            res = res / (i + 1);
        }
        return res;
    }
}
```

### Concepts to Think About

* **Integer Overflow:** Even for relatively small rows (e.g., Row 40), the values in Pascal's Triangle exceed the range of a 32-bit `int`. Always use `long` for intermediate calculations and clarify with your interviewer if you should return a `long` or if $r$ is guaranteed to be small.
* **Symmetry Property:** Pascal's Triangle is a mirror image of itself. Mathematically: 
    $$\binom{n}{k} = \binom{n}{n-k}$$ 
    In your code, checking `if (k > n / 2) k = n - k;` can cut your loop iterations in half and significantly reduce the risk of intermediate overflow.
* **DP vs. Math Trade-offs:** * **Use DP** ($\text{O}(r^2)$) if you need to return the **entire triangle**, as you have to touch every element anyway.
    * **Use Math** ($\text{O}(c)$) if you only need **one element** or a **single row**, as it is significantly more space and time-efficient.
* **The Row Generation "Trick":** There is a linear relationship between adjacent elements in a row. If you have the value of $\binom{n}{k}$, you can calculate $\binom{n}{k+1}$ in $\text{O}(1)$ time using the formula:
    $$\binom{n}{k+1} = \binom{n}{k} \times \frac{n-k}{k+1}$$
    This allows you to generate an entire row in $\text{O}(n)$ time and $\text{O}(n)$ space.
* **Recursion Stack Depth:** Even with a memoization table, the **recursion stack** depth in your initial solution is $\text{O}(r)$. In Google interviews, always include the stack depth in your space complexity analysis, as it distinguishes a junior candidate from a senior one.
