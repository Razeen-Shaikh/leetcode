class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        if len(word1) > len(word2):
            for i in range(len(word2)):
                result += word1[i] + word2[i]
            result += word1[len(word2):len(word1)]
        elif len(word2) > len(word1):
            for i in range(len(word1)):
                result += word1[i] + word2[i]
            result += word2[len(word1):len(word2)]
        else:
            for i in range(len(word1)):
                result += word1[i] + word2[i]
        
        return result