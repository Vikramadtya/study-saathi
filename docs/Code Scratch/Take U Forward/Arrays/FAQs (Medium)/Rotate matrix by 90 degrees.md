---
tags:
  - cc
  - matrix
  - geometry
---

# Rotate Image (90° Clockwise)

## Question
Given an $N \times N$ 2D matrix representing an image, rotate the image by **90 degrees clockwise**. You must rotate the image **in-place**, which means you have to modify the input 2D matrix directly.

## Solution

### Pattern
**Matrix Symmetry & Reflection (Transpose + Reverse)**

#### How to Identify
* The problem involves a fixed-degree rotation (90°, 180°, 270°).
* The matrix is square ($N \times N$).
* The constraints require $O(1)$ auxiliary space.

### Description
A 90-degree clockwise rotation can be broken down into two simpler geometric transformations:
1.  **Transpose:** Swap elements across the **main diagonal** (top-left to bottom-right). $M[i][j]$ becomes $M[j][i]$.
2.  **Horizontal Reflection:** Reverse each row.



### The Intuition
Imagine the matrix is a physical grid. If you flip the grid over its diagonal, the columns become rows. However, the columns are now in the wrong order for a clockwise rotation. By reversing each row, you move the elements into their final 90-degree clockwise positions.

### Complexity

| Label | Worst | Average |
| :--- | :--- | :--- |
| Time Complexity | $O(N^2)$ | $O(N^2)$ |
| Space Complexity | $O(1)$ | $O(1)$ |

> **Note:** $N^2$ is the total number of elements. We must touch every element at least once.

### Code (The Standard Two-Step Approach)

```java
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;

        // Step 1: Transpose (Swap M[i][j] with M[j][i])
        for (int i = 0; i < n; i++) {
            // j starts at i to avoid swapping elements back to original
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // Step 2: Reverse each row
        for (int i = 0; i < n; i++) {
            int left = 0, right = n - 1;
            while (left < right) {
                int temp = matrix[i][left];
                matrix[i][left] = matrix[i][right];
                matrix[i][right] = temp;
                left++;
                right--;
            }
        }
    }
}
```

## Concepts to Think About

- One-Pass (4-Way Swap): You can rotate the matrix in a single pass by moving elements in "four-way cycles." An element at (i,j) moves to (j,n−1−i), which moves to (n−1−i,n−1−j), and so on. This is more efficient but much harder to code without bugs.
- Other Rotations: * 90° Counter-Clockwise: Transpose + Vertical Reflection (Reverse each column).
- 180° Rotation: Horizontal Reflection + Vertical Reflection (or just reverse the whole matrix as a flat 1D array).
- Non-Square Matrices: Why is an in-place rotation impossible for an M×N matrix where $M!=N$ ? (Hint: The memory layout/dimensions of the array itself would need to change).

- Cache Locality: When transposing, you are jumping between rows and columns. How does this affect the CPU Cache? (Hint: Accessing matrix[j][i] when the outer loop is i causes cache misses because 2D arrays are stored row-major in Java).

- Linear Algebra: In mathematical terms, a rotation is a linear transformation. A 90° clockwise rotation is equivalent to a transpose followed by a reflection across the y-axis.