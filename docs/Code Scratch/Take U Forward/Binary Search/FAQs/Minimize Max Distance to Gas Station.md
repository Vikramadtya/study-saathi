---
tags:
  - cc
  - binary-search
  - greedy
  - precision-handling
---

# Minimise Max Distance to Gas Stations

## Question

Given a sorted array `arr` of $n$ gas station positions and an integer $k$, place $k$ new gas stations anywhere on the X-axis such that the maximum distance between any two adjacent stations is minimized. Return the minimized maximum distance.

## Solution

### Pattern

**Binary Search on Answer Space (Continuous)**
The problem asks to "Minimise the maximum," which is a classic indicator. Because stations can be placed at non-integer positions, we binary search over a continuous range of distances.

### How to Identify

- **Superlative Goal:** Minimize the maximum value (or vice versa).
- **Monotonicity:** If a maximum distance $d$ is possible with $k$ stations, then any distance $D > d$ is also possible.
- **Verification:** For a fixed distance $d$, we can greedily calculate the number of stations needed in $O(N)$.

### Description

Step-by-step explanation:

1.  **Search Space:** Set `low = 0` and `high = arr[n-1] - arr[0]`. The answer must lie between these two values.
2.  **Binary Search Loop:** Perform a fixed number of iterations (e.g., 100). This is more stable for floating-point calculations than checking the difference between `low` and `high`.
3.  **The Predicate (Check):** For a candidate distance `mid`:
    - Iterate through all adjacent gaps in the input array.
    - For each gap $G$, the number of new stations needed is $\lfloor (G / mid) \rfloor$. 
    - *Wait:* If $G = 10$ and $mid = 5$, $G/mid = 2$. We only need **1** station to split a 10m gap into two 5m gaps. Therefore, the formula is $\text{stations} = \lceil G / mid \rceil - 1$.
    - A numerically stable way to write this is `(int)(gap / mid)` but we must subtract a tiny epsilon if `gap % mid == 0`.
4.  **Narrowing:**
    - If `total_stations_needed > k`, our `mid` is too small. Move `low = mid`.
    - Otherwise, `mid` is feasible. Move `high = mid`.



### The Intuition

Think of each gap as a piece of string. You have $k$ cuts to make. To minimize the length of the longest piece, you want to "spend" your cuts on the longest strings first. 
Binary Search allows us to guess the maximum length $L$. If the number of cuts required to make all pieces $\le L$ is greater than $k$, then $L$ was an over-ambitious guess.



### Complexity

| Label            | Worst          | Average          |
| :--------------- | :------------- | :--------------- |
| Time Complexity  | $O(N \cdot \text{iters})$ | $O(N \cdot \text{iters})$ |
| Space Complexity | $O(1)$          | $O(1)$           |

#### Time Complexity

We iterate through the array of $N$ stations inside the check function. This check is performed for a fixed number of binary search iterations (usually 100). Total: $O(N \cdot 100)$.

#### Space Complexity

The algorithm only uses a few primitive variables to track bounds and counts. No extra data structures are required.

### Code

```java
class Solution {
    /**
     * Predicate: How many stations are needed to ensure no gap > maxDist
     */
    private int getRequiredStations(int[] arr, double maxDist) {
        int count = 0;
        for (int i = 1; i < arr.length; i++) {
            double gap = arr[i] - arr[i - 1];
            // Subtracting a tiny epsilon (1e-9) handles the case where gap is 
            // an exact multiple of maxDist to avoid overcounting.
            count += (int)((gap - 1e-9) / maxDist);
        }
        return count;
    }

    public double minimiseMaxDistance(int[] arr, int k) {
        int n = arr.length;
        double low = 0;
        double high = arr[n - 1] - arr[0];

        // 100 iterations provide precision up to ~10^-30
        for (int i = 0; i < 100; i++) {
            double mid = low + (high - low) / 2.0;
            
            if (getRequiredStations(arr, mid) <= k) {
                // Feasible: try smaller distance
                high = mid;
            } else {
                // Infeasible: need a larger distance
                low = mid;
            }
        }

        return high;
    }
}
```

## Caveats

- **Modulo Operator:** Never use `%` on `double` values to check divisibility; it is unreliable.
- **Precision:** `1e-6` is a standard requirement. Using 100 iterations is a "safety-first" approach for Google-level code.
- **Scale of K:** If $k$ is small, a Max-Heap approach $O(k \log N)$ is faster, but Binary Search is the general-purpose solution for large $k$.

## Concepts to Think About

- **Numerical Stability:** Dealing with floating-point underflow/overflow.
- **Fixed Iterations vs. Epsilon Loop:** Trade-offs in termination conditions.
- **Greedy vs. BS:** When to use a Priority Queue vs. Binary Search on Answer.
- **NP-Hardness:** How "contiguous" requirements (like in Book Allocation) simplify problems that would otherwise be NP-hard (like Partition).

## Logical Follow-up

Question: If you were given a very small $k$ (e.g., $k=10$) but $n=1,000,000$, would this approach still be the best?
Solution: No. In that case, an $O(k \log n)$ approach using a Max-Heap would be faster. You would store all current gaps in the heap and repeatedly split the largest one.

Question: Can we parallelize this?
Solution: Yes. The predicate function `getRequiredStations` is a simple summation over an array, which can be easily distributed across multiple cores or even using MapReduce for massive datasets.
