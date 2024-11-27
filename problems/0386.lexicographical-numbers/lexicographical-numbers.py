# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
# You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

from typing import List


class Solution:
  def lexicalOrder(self, n: int) -> List[int]:
    """
    Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
    
    Args:
    n (int): The input integer.

    Returns:
    list: All the numbers in the range [1, n] sorted in lexicographical order.
    """
    def dfs(current):
      if current > n:
        return
      result.append(current)
      for i in range(10):
        next_number = current * 10 + i
        if next_number > n:
          break
        dfs(next_number)

    result = []
    for i in range(1, 10):
      dfs(i)
    return result