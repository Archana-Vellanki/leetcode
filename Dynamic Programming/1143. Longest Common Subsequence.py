# 1143. Longest Common Subsequence
# Solved
# Medium
# Topics
# Companies
# Hint
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
 

# Constraints:

# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.

# Approach:
# Imagine comparing two strings, for example, "abc" and "ac". You look at the first characters of each—both are 'a', so you count that as part of a shared subsequence. 
# Next, you compare 'b' (from "abc") with 'c' (from "ac"), which don’t match, so you try skipping characters: 
# either skip 'b' and compare 'c' from "abc" with 'c' from "ac," 
# or skip 'c' in the second string and keep 'b'. 
# Whichever path yields the longer subsequence is the one you keep. By continuing this process, you build the longest sequence of characters that appear 
# in both strings in the same order (though not necessarily contiguously). In this example, that subsequence is "ac," which has length 2.

# Time complexity: O(m*n) where m in len1 and n is len2
# Space Complexity: O(m*n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        mx = [[0 for i in range(len2+1)] for _ in range(len1+1)]
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if text1[i-1] == text2[j-1]:
                    mx[i][j] = mx[i-1][j-1] + 1
                else:
                    mx[i][j] = max(mx[i-1][j], mx[i][j-1])
        return mx[len1][len2]

