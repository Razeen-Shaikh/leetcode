class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def count_vowels(s):
            vowels = set("aeiouAEIOU")
            return sum(1 for char in s if char in vowels)

        length = len(s)
        mid = length // 2

        first_half = s[:mid]
        second_half = s[mid:]

        return count_vowels(first_half) == count_vowels(second_half)