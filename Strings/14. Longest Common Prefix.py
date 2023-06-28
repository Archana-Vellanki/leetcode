# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


# Time complexity: O(m*n)
# Space complexity: O(m)
# m is the shortest string
# n is the number of strings
# Approach: find the length of the shortest string so that we can iterate only until that index.
# Iterate from the beginning of each string, to see if the character (of all strings )at a given index  is the same.
# If it is same, then it is valid prefix character hence append to the result.
# If not, return the prefix found till now.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        prefix = []
        ch = ''
        minLength = min([len(each) for each in strs])

        while i < minLength:
            ch = strs[0][i]
            for each in strs:
                if each[i] != ch:
                    return ''.join(prefix)
            prefix.append(ch)
            i += 1
        return ''.join(prefix)
