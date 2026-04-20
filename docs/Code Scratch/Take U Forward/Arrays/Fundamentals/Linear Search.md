---
tags:
  - cc
  - searching
---

# Linear Search

## Question

Given an array of integers `nums` and an integer `target`, find the smallest index (0-based indexing) where the target appears in the array. If the target is not found in the array, return -1.

## Solution

### Pattern

**Sequential Scanning / Brute Force Search**

### How to Identify

- The data is **unsorted** (meaning Binary Search is not an option).
- You need to find the **first** occurrence of an element.
- The collection is small or doesn't support random access (like a basic Linked List).

### Description

Linear Search is the most basic searching algorithm. It starts at the beginning of a collection and checks every single element one by one until it finds a match or reaches the end of the data.



### The Intuition

Imagine you are looking for a specific key in a messy drawer. Since the drawer isn't organized, you have to pick up every single object one by one, look at it, and see if it's the key you want. You stop the moment you find the key.

### Complexity

| Label            | Worst  | Average |
| :--------------- | :----- | :------ |
| Time Complexity  | $O(n)$ | $O(n)$  |
| Space Complexity | $O(1)$ | $O(1)$  |

*Note: The Best Case is O(1) if the target is the very first element in the array.*

### Code

```java
class Solution {
    public int linearSearch(int nums[], int target) {
        // Defensive check for null or empty array
        if (nums == null || nums.length == 0) {
            return -1;
        }

        // Iterate through the array sequentially
        for (int i = 0; i < nums.length; ++i) {
            // Check if current element matches target
            if (nums[i] == target) {
                // Return index immediately for the 'smallest' index
                return i;
            }
        }

        // Target not found after scanning the whole array
        return -1;
    }
}
```

### Concepts to Think About

- **Sorted Data:** If the array were sorted, would you still use Linear Search? Think about why **Binary Search** ($O(\log n)$) would be vastly superior for sorted datasets.
- **Search for All:** How would the code change if the question asked for **all** indices where the target appears? (Hint: You would need a dynamic collection like a `List` to store results instead of returning immediately).
- **Sentinel Search:** There is a variation called "Sentinel Linear Search" where you place the target at the very end of the array manually. Why would this reduce the number of comparisons made inside the loop?
    - Sentinel Linear Search is an optimized version of the basic search. By placing the target at the end of the array (the "sentinel"), we guarantee the loop will always find the target. This allows us to remove the boundary check (`i < length`) from the loop header, saving one comparison per iteration.
    - Imagine walking through a long hallway of doors looking for a specific person. Usually, you have to check two things at every door: "Is this the person?" AND "Have I reached the end of the hallway?" To save time, you put a clone of the person you're looking for at the very end of the hallway. Now, you only have to ask one question: "Is this the person?" When you find them, you just check if you're at the very last door to see if it was a real find or just your clone.
        ```java
        class Solution {
            public int linearSearch(int[] nums, int target) {
                // Guardrail for empty arrays
                if (nums == null || nums.length == 0) return -1;

                int n = nums.length;
                int lastElement = nums[n - 1];

                // Place sentinel
                nums[n - 1] = target;
                int i = 0;

                // Optimized loop: No boundary check (i < n) required!
                while (nums[i] != target) {
                    i++;
                }

                // Restore the original last element
                nums[n - 1] = lastElement;

                // If we found the target before the last element, or if the 
                // original last element was actually the target, return the index.
                if (i < n - 1 || lastElement == target) {
                    return i;
                }

                return -1;
            }
        }
        ```

- **Order of Operations:** If you are going to search the same unsorted array 1,000 times, is it better to do 1,000 Linear Searches, or sort the array once and do 1,000 Binary Searches? (Think about the $O(n^2)$ total cost vs $O(n \log n + k \log n)$).
- **2D Linear Search:** If you were given a matrix instead of a flat array, what would the Time Complexity be? ($O(rows \times columns)$).