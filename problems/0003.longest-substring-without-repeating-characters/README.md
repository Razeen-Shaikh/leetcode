# 3. Longest Substring Without Repeating Characters

Given a string `s`, find the length of the **longest substring** without repeating characters.

**Example 1:**

```text
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**

```text
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```text
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Constraints:**

* <code>0 <= s.length <= 5 * 10<sup>4</sup></code>
* `s` consists of English letters, digits, symbols and spaces.

## Flowchart for `longest_substring_without_repeating_characters.py`
```
op40=>operation: class Solution():

    def length_of_longest_substring(self, s: str) -> int:
        '\n        Given a string `s`, find the length of the **longest substring** without repeating characters.\n\n        Args:\n            s (str): The input string.\n\n        Returns:\n            int: The length of the longest substring without repeating characters.\n        '
        char_set = set()
        max_length = 0
        start = 0
        for end in range(len(s)):
            while (s[end] in char_set):
                char_set.remove(s[start])
                start += 1
            char_set.add(s[end])
            max_length = max(max_length, ((end - start) + 1))
        return max_length


```