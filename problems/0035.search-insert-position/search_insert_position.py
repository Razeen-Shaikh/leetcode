from ast import List


class Solution:
    """
    This class provides a solution to the search_insert problem.
    """
    def search_insert(self, nums: List[int], target: int) -> int:
        """
        Search for the target in the list nums and return its index if found. If not found, insert the target into the list and return its index.
        
        Args:
        - nums: List of integers to search within.
        - target: Integer value to search for or insert into the list.
        
        Returns:
        - Integer representing the index of the target in the list nums.
        """
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
