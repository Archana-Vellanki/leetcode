# 28. Find the Index of the First Occurrence in a String
# Solved
# Easy
# Topics
# Companies
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

# Time complexity:O(m*n)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        result = -1
        hayLength = len(haystack)
        needleLength = len(needle)
        while i < hayLength and j < needleLength:
            if haystack[i] == needle[j]:
                if j == 0:
                    result = i
                j+= 1
                i+=1
            else:
                if result != -1:
                    j = 0
                    i = result + 1
                    result = -1
                else:
                    i += 1
        return result if j == needleLength else -1
