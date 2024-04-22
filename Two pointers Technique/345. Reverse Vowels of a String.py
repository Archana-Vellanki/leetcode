# 345. Reverse Vowels of a String
# Solved
# Easy
# Topics
# Companies
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"


# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s) - 1
        result = list(s)
        while i < j:

            while i < len(s) and result[i] not in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                i += 1
            while j >= 0 and result[j] not in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                j -= 1
            # print(i, j)
            # result = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
            if i < j:
                result[i], result[j] = result[j], result[i]
            i += 1
            j -= 1

        return "".join(result)
