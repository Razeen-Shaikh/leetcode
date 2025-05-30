# 557. Reverse Words in a String III

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

**Example 1:**

```
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
```

**Example 2:**

```
Input: s = "God Ding"
Output: "doG gniD"
```

**Constraints:**

-   <code>1 <= s.length <= 5 \* 10<sup>4</sup></code>
-   s contains printable ASCII characters.
-   s does not contain any leading or trailing spaces.
-   There is at least one word in s.
-   All the words in s are separated by a single space.

## Flowchart for `reverse-words-in-a-string-iii.py`
```
op18=>operation: class Solution():

    def reverseWords(self, s: str) -> str:
        reverse = []
        for word in s.split(' '):
            reverse.append(''.join(list(reversed(word))))
        return ' '.join(reverse)


```