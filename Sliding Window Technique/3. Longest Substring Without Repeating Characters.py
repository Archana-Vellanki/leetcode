# 3. Longest Substring Without Repeating Characters
# Medium
# 34.8K
# 1.6K
# Companies
# Given a string s, find the length of the longest
# substring
#  without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# Time Complexity: O(n) just one iteration through the string
# Space Complexity: O(n) hashmap to store chars
# Approach: maintain a hashmap to store chars and their indices, along with two pointers(left and right) to indicate the sliding window(current substring)
# For every iteration,
#   check if the char at the right index is present in the hashmap.
#       If it is present, that means it is repeating. move the left pointer ahead of it (if it has not crossed it already)
#   update the maximum length and the char index in the hashmap
#   move the right pointer to the next character

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        l, r = 0, 0
        length = len(s)
        maxLength = 0

        while r < length:
            if s[r] in chars:
                l = max(chars[s[r]] + 1, l)
            chars[s[r]] = r
            maxLength = max(maxLength, r-l+1)
            r += 1
        return maxLength
