# Boyer Moore majority vote algorithm

An optimum algorithm for determining the majority element among elements with more than $$\frac{N}{2}$$ occurrences

## Algorithm

> A majority element is one that appears more than half of the time in the input elements.

The algorithm seeks out a majority element if one exists. However, if there is no majority, the algorithm will not recognise this and will continue to output one of the items.

So to fix the issue algorithm is divided into two parts.

* A first pass identifies an element as a majority
* A second pass confirms that the element identified in the first pass is indeed a majority.

The method will not identify the majority element if it does not exist, and will thus return an arbitrary element.

### Steps

1. Begin by initializing two variables, num and a counter count, both of which are set to 0.
2. Now we’ll begin iterating over the number and for each element x.
3. We first check to see if the count is 0, and then we assign num to x.
4. Then we check to see if the current num is equal to x, if not, we decrease the count by one, else we increment it by one.
5. Reset the counter to zero.
6. Find the frequency of the num variable by looping through the nums array.
7. Now, if the count is larger than N/2, we return num; otherwise we return -1.

## Code&#x20;



### Complexity

**Time complexity:** O(n), we make only two iterations through the array.\
**Space complexity:** O(1), only two variables.

## Preactice Problems

|                     |   |   |
| ------------------- | - | - |
| Majority Element    |   |   |
| Majority Element II |   |   |



## Extension

#### Find all elements that appear more than a certain fraction of the time, such as `n/3`.

In the algorithm, two candidates and their counters are used to handle the case where there might be more than one element that appears more than `n/3` times in the array. \


**Two Candidates**

* **Candidate 1**: Represents one potential majority element.
* **Candidate 2**: Represents another potential majority element.

> This is necessary because in an array, there can be at most two elements that appear more than `n/3` times. If there were three such elements, their combined count would exceed `n`, which is impossible.

**Counters**

* **Count 1**: Tracks the count of occurrences for Candidate 1.
* **Count 2**: Tracks the count of occurrences for Candidate 2.

These counters help in determining whether the current candidate should be replaced or if its count should be incremented.

**First Pass**

* Iterate through the array to find the two most frequent candidates.
* Adjust the candidates and their counts based on the current element.
* If the current element matches one of the candidates, increment the corresponding count.
* If the current element does not match either candidate and one of the counts is zero, replace that candidate with the current element and reset the count.
* If the current element does not match either candidate and both counts are non-zero, decrement both counts.

**Second Pass**

* Verify the counts of the two candidates by iterating through the array again.
* Only include candidates that appear more than `n/3` times in the final result.

## Reference&#x20;

* [Boyer moore majority vote algorithm](https://www.topcoder.com/thrive/articles/boyer-moore-majority-vote-algorithm)
* [Boyer-Moore Majority Voting Algorithm](https://utkarsh1504.github.io/DSA-Java/bmmv-algorithm)



