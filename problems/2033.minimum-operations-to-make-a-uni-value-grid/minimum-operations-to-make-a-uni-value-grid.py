class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [num for row in grid for num in row]
        nums.sort()  # Sorting to find the median

        # Check if transformation is possible
        for num in nums:
            if (num - nums[0]) % x != 0:
                return -1  # Impossible case

        # Find the median
        median = nums[len(nums) // 2]

        # Calculate total operations
        operations = sum(abs(num - median) // x for num in nums)

        return operations