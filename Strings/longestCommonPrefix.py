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


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        prefix = []
        nStrings = len(strs)
        ch = ''
        flag = True
        while flag:
            if i < len(strs[0]):
                ch = strs[0][i]
            else:
                break
            for each in strs:
                if i >= len(each) or each[i] != ch:
                    flag = False
                    break
            if flag:
                prefix.append(ch)
            i += 1
        # print(prefix)
        return ''.join(prefix)
