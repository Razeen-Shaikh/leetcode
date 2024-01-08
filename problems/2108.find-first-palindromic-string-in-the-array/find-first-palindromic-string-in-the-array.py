from ast import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            rev = list(word)[::-1]
            if(word == "".join(rev)):
                return word

        return ""
