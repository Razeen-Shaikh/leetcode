# 1346. Check If N and Its Double Exist

Given an array `arr` of integers, check if there exist two indices `i` and `j` such that :

- `i != j`
- `0 <= i, j < arr.length`
- `arr[i] == 2 \* arr[j]`

**Example 1:**

```
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 _ 5 == 2 _ arr[j]
```

**Example 2:**

```
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
```

**Constraints:**

- `2 <= arr.length <= 500`
- <code>-10<sup>3</sup> <= arr[i] <= 10<sup>3</sup>

## Flowchart for `check-if-n-and-its-double-exist.py`
```
op8=>operation: from ast import List
op10=>operation: class Solution():

    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        count = 0
        for i in range(len(arr)):
            if (arr[i] == 0):
                count += 1
            elif ((2 * arr[i]) in arr):
                return True
        if (count > 1):
            return True
        return False

op8->op10

```