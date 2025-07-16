from typing import List

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings strs, group the anagrams together. You can return the answer in any order.

        Args:
        - strs: A list of strings to group anagrams from.

        Returns:
        A list of lists, where each inner list contains the anagrams grouped together.
        """
        anagrams = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
                
        return list(anagrams.values())