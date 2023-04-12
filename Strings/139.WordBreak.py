# 139. Word Break
# Medium

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.


# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false


# Constraints:

# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

# Time complexity: O(N^2)
# Space complexity: O(N)

# Iterate through all the indices of the string
# Check if the substring from 0 to the index is a valid word
# if it is a valid word, check the substring from the index to the end recursively
# Use memoization to store the result of substrings found to avoid re-computation.

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Memoization dictionary to store the results for substrings
        wordsFound = {}
        return self.helper(s, wordDict, wordsFound)

    def helper(self, s, wordDict, wordsFound):
        # if s is already explored return the result that is stored
        if s in wordsFound:
            return wordsFound[s]

        # if s is empty return True since it is the base case
        if not s:
            return True

        # check if the current prefix s[:right] is a valid word
        # recursively check if the remaining suffix can be segmented into words
        for right in range(1, len(s) + 1):
            if s[:right] in wordDict and self.helper(s[right:], wordDict, wordsFound):
                # store the result for this substring and return True
                wordsFound[s] = True
                return True
        # store the result for this substring and return False
        wordsFound[s] = False
        return False


# without memoization the time complexity would be exponential

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Time complexity: O(2^N)
        n = len(s)
        if n == 0:
            return True
        right = 0
        result = False
        while right <= n and not result:
            if s[:right] in wordDict:
                result = self.wordBreak(s[right: n], wordDict)
            right += 1
        return result
