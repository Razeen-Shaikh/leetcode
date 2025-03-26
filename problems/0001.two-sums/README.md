

## Flowchart for `two_sums.py`
```
op28=>operation: from ast import List
op30=>operation: class Solution():

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        '\n        Given an array of integers `nums` and an integer `target`, \n        return indices of the two numbers such that they add up to `target`.\n        You may assume that each input would have **_exactly one solution_**,\n        and you may not use the same element twice.\n        \n        Args:\n            nums: A list of integers.\n            target: The target sum.\n            \n        Returns:\n            A list of two integers,\n            representing the indices of the two numbers that add up to the target.\n        '
        num_indices = {}
        for (i, num) in enumerate(nums):
            complement = (target - num)
            if (complement in num_indices):
                return [num_indices[complement], i]
            num_indices[num] = i
        return []

op28->op30

```