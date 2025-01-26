class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        """
        Given a string `s`, find the length of the **longest substring** without repeating characters.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.
        """
        char_set = set()
        max_length = 0
        start = 0

        for end in range(len(s)):
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            
            char_set.add(s[end])
            max_length = max(max_length, end - start + 1)
        
        return max_length
