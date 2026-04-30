---
tags:
  - cc
  - binary-search
  - greedy
---

# Aggressive Cows (Maximize Minimum Distance)

## Question
Given an array $nums$ representing stall positions and an integer $k$ (number of cows), assign cows to stalls such that the **minimum distance** between any two cows is as **large** as possible. Return this maximum possible minimum distance.

## Solution

### Pattern
**Binary Search on Answer Space**
When the problem asks to "maximize the minimum" or "minimize the maximum" of a value that has a monotonic relationship with a condition, we binary search the result directly.

### How to Identify
- **Keywords:** "Maximize the minimum" or "Minimize the maximum."
- **Monotonicity:** If it's possible to place cows with a minimum distance $D$, it is also possible for any distance $d < D$.
- **Greedy Validation:** Checking if a specific distance is "valid" can be done easily in $O(N)$ time.

### Description
Step-by-step explanation:

1.  **Sort the Input:** Stall positions must be ordered to allow a greedy, one-pass placement.

2.  **Define the Search Space:** - The smallest possible distance $L = 1$ (or the minimum gap between any two stalls).
    - The largest possible distance $R = \text{stalls}[n-1] - \text{stalls}[0]$.

3.  **Binary Search:** - Pick a middle distance $M = L + (R - L) / 2$.
    - Check if we can place $k$ cows such that every pair is at least $M$ apart.

4.  **Greedy Check (Predicate):** - Place the first cow in the first stall.
    - Iterate through stalls; place the next cow only if the distance from the last placed cow $\ge M$.
    - If cows placed $\ge k$, return `true`.

5.  **Adjust Bounds:**
    - If `true`, $M$ is a candidate answer. Try for a larger distance ($L = M + 1$).
    - If `false`, $M$ is too large. Try a smaller distance ($R = M - 1$).



### The Intuition
The problem is essentially asking us to find a "threshold" distance. Imagine a "Possibility Function" $P(d)$. For very small distances, $P(d)$ is always true. For very large distances, it's false. There is a single point where it flips from `True` to `False`. Binary search finds that boundary.



### Complexity

| Label            | Worst          | Average          |
| :--------------- | :------------- | :--------------- |
| Time Complexity  | $O(N \log N + N \log D)$ | $O(N \log N + N \log D)$ |
| Space Complexity | $O(1)$ | $O(1)$ |

#### Time Complexity
$O(N \log N)$ for sorting the stalls. The binary search takes $\log D$ steps (where $D$ is the max distance), and each step performs an $O(N)$ greedy check. Total: $O(N \log N + N \log D)$.

#### Space Complexity
$O(1)$ auxiliary space. The space used by the sorting algorithm ($O(\log N)$) is usually ignored in interview discussions unless specified.

### Code

```java
import java.util.Arrays;

class Solution {
    public int aggressiveCows(int[] stalls, int k) {
        if (stalls == null || stalls.length < k) return -1;
        
        Arrays.sort(stalls);
        
        int n = stalls.length;
        int low = 1; // Minimum possible distance
        int high = stalls[n - 1] - stalls[0]; // Maximum possible distance
        int ans = 0;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (canPlace(stalls, k, mid)) {
                ans = mid; // Mid is possible, try to find a larger minimum
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
    
    /**
     * Predicate function: Checks if we can place k cows with at least minDist
     */
    private boolean canPlace(int[] stalls, int k, int minDist) {
        int count = 1; // Place the first cow
        int lastPos = stalls[0];
        
        for (int i = 1; i < stalls.length; i++) {
            if (stalls[i] - lastPos >= minDist) {
                count++;
                lastPos = stalls[i];
            }
            if (count >= k) return true;
        }
        return false;
    }
}
```

## Caveats
- **Sorting Requirement:** Many candidates forget that the greedy placement only works if the stalls are sorted. Without sorting, the check becomes a variation of the NP-Hard Clique problem.
- **Search Space Range:** If coordinates are very large (e.g., $10^9$), the $\log D$ factor remains small ($\approx 30$), making this highly efficient.

## Concepts to Think About
- **Maximize Minimum vs Minimize Maximum:** Both are solved via Binary Search on Answer Space. For "Minimize Maximum," the greedy check logic and bound updates are simply mirrored.
- **Floating Point:** If stall positions were doubles, the binary search would use a fixed number of iterations (e.g., 100) or a `while (right - left > precision)`.
- **Integer Overflow:** `(right + left) / 2` can overflow if `right` and `left` are large; always use `left + (right - left) / 2`.

## Logical Follow-up

Question: What if the stalls are arranged in a **Circle**?
Solution: This is significantly harder. If circular, the distance between the last cow and the first cow also counts. You would need to run the greedy check fixing the first cow at different positions or use a "broken circle" approach where you duplicate the array and use a sliding window logic within the binary search check.

Question: What if each cow has a different "Aggression Level" (needs a different minimum distance from others)?
Solution: Binary search on answer space no longer works directly because there isn't a single "min distance" to optimize. This would likely require a Dynamic Programming approach or a more complex Greedy strategy if the aggression levels are sorted.
