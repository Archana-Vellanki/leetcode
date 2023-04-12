# 5. Longest Palindromic Substring
# Medium
# 24.6K
# 1.5K
# Companies
# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"


# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

# Time complexity:O(N^2)
# Space Complexity: O(1)

# there is a better approach called Manacher's algorithm with a time complexity and space complexity of O(N)
# https://www.scaler.com/topics/data-structures/manachers-algorithm/


class Solution(object):
    def palCheck(self, left, right, i, s, length):
        temp = s[i]

        # iteratively check if left and right indices are within bounds and the chars at left and right indices are same
        # break the loop when the conditions are not met because we cannot find a palindrome by proceeding further
        # the palindrome that was found

        while left >= 0 and right < length and s[left] == s[right]:
            temp = s[left:right+1]
            left -= 1
            right += 1
        return temp

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        # if the string is empty or of single character, the longest palindrome is the string itself
        if length == 0 or length == 1:
            return s

        res = ""
        resLen = 0

        for i in range(length):
            print(i)
            # check for even length palindrome centered at i
            temp = self.palCheck(i, i+1, i, s, length)
            tempLen = len(temp)
            if tempLen > resLen:
                res = temp
                resLen = tempLen
            # check for odd length palindrome centered at i
            temp = self.palCheck(i-1, i+1, i, s, length)
            tempLen = len(temp)
            if tempLen > resLen:
                res = temp
                resLen = tempLen
        return res
