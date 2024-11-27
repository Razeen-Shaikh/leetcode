class Solution:
    def first_uniq_char(self, s: str) -> int:
        """
        Find the first unique character in the given string.

        Args:
        s (str): The input string.

        Returns:
        int: The index of the first unique character, or -1 if no unique character is found.
        """
        t = s
        for i, c in enumerate(s):
            if i != s.index(c):
                t = t.replace(s[i], "")
        if len(t) > 0:
            return s.index(t[0])
        else:
            return -1
