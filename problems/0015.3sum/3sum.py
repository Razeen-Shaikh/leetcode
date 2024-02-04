from ast import List


class Solution:
    """
    Missing class docstring
    """
    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        """
        Describe the purpose, inputs, and outputs of the threeSum method here.
        """
        result = []
        numbers.sort()

        for i in range(len(numbers)-2):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue

            left, right = i+1, len(numbers)-1

            while left < right:
                curr_sum = numbers[i] + numbers[left] + numbers[right]

                if curr_sum == 0:
                    result.append([numbers[i], numbers[left], numbers[right]])

                    while left < right and numbers[left] == numbers[left+1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result
