---
tags:
  - cc
  - bms
  - arrays
---

# Majority Element II ($> n/3$ elements)

## Question

Given an integer array $nums$ of size $n$, find all elements that appear more than $\lfloor n/3 \rfloor$ times. 
- **Constraints:** $O(n)$ time complexity and $O(1)$ space complexity.
- **Fact:** In any array, there can be at most **two** such elements.

## Solution

### Pattern

**Boyer-Moore Voting Algorithm (Extended)**
A generalization of the majority element algorithm. It uses "cancellation" logic where $k$ distinct elements are removed from the dataset simultaneously. For the $n/3$ case, we track two candidates.



### How to Identify

- The problem asks for elements appearing more than $n/k$ times.
- Requirements demand linear time and constant auxiliary space.
- The output size is strictly bounded (at most $k-1$ elements).

### Description

Step-by-step explanation:

- **Step 1: The Voting Phase.** Initialize two candidates and two counters to 0. 
- **Step 2: Process Elements.** Iterate through the array:
    1. If the element matches `candidate1`, increment `count1`.
    2. Else if it matches `candidate2`, increment `count2`.
    3. Else if `count1` is 0, assign the element to `candidate1` and set `count1` to 1.
    4. Else if `count2` is 0, assign the element to `candidate2` and set `count2` to 1.
    5. **The Cancellation:** If the element matches neither and both counters are $> 0$, decrement both `count1` and `count2`.
- **Step 3: The Verification Phase.** Boyer-Moore only guarantees that *if* majority elements exist, they will be among the candidates. We must loop through the array again to count the actual occurrences of our two candidates.
- **Step 4: Filter.** Add to the result list only those candidates whose actual count is $> n/3$.



### The Intuition

Think of this as **"The Triplet Elimination Game."** If we are looking for elements appearing $> n/3$ times, we can conceptually group three *distinct* elements together and discard them. Since we only discard triplets of different numbers, any number that appears more than $1/3$ of the time is mathematically guaranteed to remain after all possible triplets are removed. 

We use two counters to represent our "survivors." When we find a third distinct number, we effectively "cancel" one instance of each of our two survivors along with that third number.

### Complexity

| Label            | Worst          | Average          |
| :--------------- | :------------- | :--------------- |
| Time Complexity  | $O(n)$         | $O(n)$           |
| Space Complexity | $O(1)$         | $O(1)$           |

#### Time Complexity
We perform exactly two linear passes over the array. $O(2n) \approx O(n)$.

#### Space Complexity
The algorithm uses a fixed number of variables (`cand1`, `cand2`, `cnt1`, `cnt2`) regardless of input size. The output list does not count toward auxiliary space in standard interview contexts.

### Code

```java
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        if (nums == null || nums.length == 0) return new ArrayList<>();

        // Phase 1: Finding potential candidates
        int cand1 = 0, cand2 = 0, count1 = 0, count2 = 0;

        for (int num : nums) {
            if (num == cand1) {
                count1++;
            } else if (num == cand2) {
                count2++;
            } else if (count1 == 0) {
                cand1 = num;
                count1 = 1;
            } else if (count2 == 0) {
                cand2 = num;
                count2 = 1;
            } else {
                // Triplet cancellation
                count1--;
                count2--;
            }
        }

        // Phase 2: Verification
        count1 = 0;
        count2 = 0;
        for (int num : nums) {
            if (num == cand1) count1++;
            else if (num == cand2) count2++;
        }

        List<Integer> result = new ArrayList<>();
        int n = nums.length;
        if (count1 > n / 3) result.add(cand1);
        if (count2 > n / 3) result.add(cand2);

        return result;
    }
}
```

## Caveats

- **Order of Conditions:** You **must** check `num == cand` before `count == 0`. Otherwise, you might assign the same number to both `cand1` and `cand2`.
- **Verification is Mandatory:** Boyer-Moore is a heuristic for potential candidates. For $n/2$, it works without verification *if* a majority is guaranteed. For $n/3$, you must always verify.
- **Empty Arrays:** Always handle null/empty cases to prevent runtime exceptions.

## Concepts to Think About

- **Generalization:** This approach can be generalized to $n/k$ by using $k-1$ candidates and $k-1$ counters (using a Hash Map for the "voting" part to keep space $O(k)$).
- **Misunderstandings:** This is not a "frequency" problem (which would be $O(n)$ space). This is a "relative frequency" problem.
- **Stable vs Unstable:** This algorithm is stable in its candidate selection but order-dependent in how counters fluctuate.
- **Streaming Data:** This algorithm is perfect for streaming data where you cannot store the entire dataset.

## Logical Follow-up

Question: How would you find all elements appearing more than $n/k$ times?

Solution: Use a `HashMap<Integer, Integer>` to keep track of $k-1$ candidates. When you encounter a new element and the map size is $k-1$, decrement all counts in the map. If a count reaches zero, remove the key. Finally, verify the remaining keys in a second pass.