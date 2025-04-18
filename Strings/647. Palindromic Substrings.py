# 647. Palindromic Substrings
# Solved
# Medium
# Topics
# Companies
# Hint
# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of lowercase English letters.

# Most optimized solution:
# Approach:
# Start from the center and expand the string and check if its a palindrome.
# Two possibilities of palindromes at index i: 
#   Odd length:  i-1, i, i+1
#   Even length: i, i+1

# Time Complexity: O(n²) for n characters and expanding around each center.
# Space Complexity: O(1) — constant extra space.

class Solution:
    def countSubstrings(self, s: str) -> int:
        result = len(s)
        length = result
        # abcdchg

        def findPalindrome(left, right):
            nonlocal result
            nonlocal length
            while left >= 0 and right < length and s[left] ==  s[right]:
                result += 1
                left -= 1
                right += 1
        # Recursive Approach: 
        # def findPalindrome(left, right):
        #     nonlocal result
        #     if left >= 0 and right < len(s):
        #         if s[left] ==  s[right]:
        #             result += 1
        #             findPalindrome(left-1, right+1)


        for i in range(length):
            findPalindrome(i-1, i+1)
            findPalindrome(i, i+1)
        return result
