---
tags:
  - cc
  - array
  - two-pointers
  - sorting
  - k-sum
---

# 4Sum: The k-Sum Reduction Pattern

## Question
Given an integer array `nums` and a `target`, return all unique quadruplets that sum to exactly `target`.

## Solution

### Pattern
**Recursive/Nested k-Sum Reduction**

#### How to Identify
* The problem asks for a combination of $k$ elements (where $k > 2$).
* The results must be unique.
* The time complexity is allowed to be $O(n^{k-1})$.

### Description
We first **sort** the array. We use two nested loops to fix the first two elements ($i$ and $j$). This reduces the problem to a **Two Sum** problem for the remaining target. We then use two pointers ($k$ and $l$) to find the remaining pair. Pruning logic is added to skip iterations that cannot mathematically reach the target.



### The Intuition
Think of this like a Russian Nesting Doll. To solve 4Sum, you open it up to find a 3Sum problem inside. Open that, and you find a 2Sum problem. By sorting the "dolls" by size first, you can immediately tell if a doll is too big or too small to fit your target without checking every single one inside.

### Complexity

| Label | Worst | Average |
| :--- | :--- | :--- |
| Time Complexity | $O(n^3)$ | $O(n^3)$ |
| Space Complexity (Aux) | $O(\log n)$ | $O(\log n)$ |

> **Note:** $O(n^3)$ results from two nested loops $O(n^2)$ and a two-pointer scan $O(n)$.

### Code (L5 Optimized with Pruning)

```java
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums == null || nums.length < 4) return res;
        
        Arrays.sort(nums);
        int n = nums.length;

        for (int i = 0; i < n - 3; i++) {
            // Duplicate skip
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            // L5 Pruning 1: Smallest sum is too big
            if ((long)nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target) break;
            // L5 Pruning 2: Largest sum is too small
            if ((long)nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target) continue;

            for (int j = i + 1; j < n - 2; j++) {
                // Duplicate skip
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                
                // L5 Pruning 3: Smallest sum in this loop is too big
                if ((long)nums[i] + nums[j] + nums[j+1] + nums[j+2] > target) break;
                // L5 Pruning 4: Largest sum in this loop is too small
                if ((long)nums[i] + nums[j] + nums[n-2] + nums[n-1] < target) continue;

                int left = j + 1, right = n - 1;
                while (left < right) {
                    long sum = (long)nums[i] + nums[j] + nums[left] + nums[right];
                    if (sum == target) {
                        res.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;
                        left++;
                        right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }
        return res;
    }
}
```

## Concepts to Think About

- Overflow: Always use long when summing multiple integers in a target problem.
- Generalization: Could you write a generic kSum function that uses recursion to handle any k?
- The Two-Pointer Direction: Why does left++ increase the sum and right-- decrease it? (Only because the array is sorted).
- Pruning Efficiency: How much does the O(n^3) runtime actually improve with the break and continue optimizations? (In practice, it can be 10x faster on skewed datasets).

---

### **Follow-up**

**Question:** "How would you implement a general `kSum(int[] nums, int target, int k)` function?"

**Solution:** Use recursion.
1. **Base Case:** If $k = 2$, use the Two-Pointer approach ($O(n)$).
2. **Recursive Step:** Iterate from `start` to `end`. For each element, call `kSum` for the sub-problem: `kSum(nums, target - nums[i], k - 1)`.
3. Remember to skip duplicates at every level of the recursion.