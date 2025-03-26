

## Flowchart for `kth-largest-element-in-an-array.py`
```
op34=>operation: from ast import List
op36=>operation: class Solution():

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[(len(nums) - k)]

op34->op36

```