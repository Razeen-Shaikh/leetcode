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

        # Iterate through each word in the input array
        for word in strs:
            # Sort the characters of the word
            sorted_word = ''.join(sorted(word))
            
            # Check if the sorted word exists in the dictionary
            if sorted_word in anagrams:
                # If it exists, append the original word to the list of anagrams
                anagrams[sorted_word].append(word)
            else:
                # If it doesn't exist, create a new list with the original word
                anagrams[sorted_word] = [word]
        
        # Convert the values of the dictionary to a list of lists
        grouped_anagrams = list(anagrams.values())
        
        return grouped_anagrams