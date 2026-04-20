---
tags:
  - cc
  - array
  - rotation
---

# Rotate Array Left by One

## Question
Given an integer array `nums`, rotate the array to the left by one position. The modification should be done in-place.

## Solution

### Pattern
**In-place Displacement / Linear Shifting**

#### How to Identify
* The problem asks for a cyclic shift of elements.
* The rotation amount is small or fixed (e.g., exactly 1).
* You are required to modify the array without using extra space ($O(1)$).

### Description
To rotate an array to the left by one, we "save" the first element because it will be overwritten during the shift. We then move every other element one position to the left (index $i$ moves to $i-1$). Finally, we place the saved first element into the last position of the array.



### The Intuition
Imagine a conveyor belt of items. To move everything one step left, you pick up the very first item (the one at the front). You push every other item forward by one slot. Now that the very last slot is empty, you take the item you picked up from the front and place it at the back.

### Complexity

| Label            | Worst           | Average         |
| :--------------- | :-------------- | :-------------- |
| Time Complexity  | $O(n)$          | $O(n)$          |
| Space Complexity | $O(1)$          | $O(1)$          |

### Code

```java
class Solution {
    /**
     * Rotates the array to the left by one position in-place.
     */
    public void rotateArrayByOne(int[] nums) {
        // Guardrail: Nothing to do for null, empty, or single-element arrays
        if (nums == null || nums.length < 2) {
            return;
        }

        // 1. Store the element that will "fall off" the front
        int firstElement = nums[0];

        // 2. Shift all subsequent elements one position to the left
        for (int i = 1; i < nums.length; i++) {
            nums[i - 1] = nums[i];
        }

        // 3. Move the original first element to the last position
        nums[nums.length - 1] = firstElement;
    }
}
```

## Concepts to Think About

- Rotating by k positions: If you were asked to rotate by k instead of 1, would you run this function k times? That would be O(n×k). Is there a better way using the "Triple Reverse" trick to keep it O(n)?
- Right Rotation: How would the code change if you had to rotate to the right by one? (Hint: You would save the last element and shift from right to left).
- Large k values: If k is larger than the array length n, the effective rotation is actually k(modn). Why is this important for performance?
- Juggling Algorithm: For rotating by k, there is a "Juggling Algorithm" based on the Greatest Common Divisor (GCD). When might that be more or less efficient than the reversal method?
- Data Structures: If this were a Doubly Linked List instead of an array, could you perform a rotation in O(1) time? (Hint: Think about moving the head and tail pointers).
