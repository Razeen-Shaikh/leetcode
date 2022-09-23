class Solution:
    def reverseWords(self, s: str) -> str:
        reverse = []
        for word in s.split(" "):
            reverse.append("".join(list(reversed(word))))
                
        return " ".join(reverse)