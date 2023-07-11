# 784. Letter Case Permutation
# Medium
# 4.4K
# 155
# Companies
# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

# Return a list of all possible strings we could create. Return the output in any order.


# Example 1:

# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# Example 2:

# Input: s = "3z4"
# Output: ["3z4","3Z4"]


# Constraints:

# 1 <= s.length <= 12
# s consists of lowercase English letters, uppercase English letters, and digits.

# Time complexity: O(n)
# Space complexity: O(1)
# Approach: backtracking


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def backtrack(sub="", i=0):
            if len(sub) == len(S):
                res.append(sub)
            else:
                if S[i].isalpha():
                    backtrack(sub + S[i].swapcase(), i + 1)
                backtrack(sub + S[i], i + 1)

        res = []
        backtrack()
        return res

# Time complexity: O(n)
# Space complexity: O(1)
# Approach: backtracking


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if s.isnumeric():
            return [s]
        res = set()

        for i in range(len(s)):
            if s[i].isalpha():
                temp = []
                length = len(res)
                if length == 0:
                    res.update([s, s[:i] + s[i].swapcase() + s[i + 1:]])
                else:
                    for each in res.copy():
                        res.add(each[:i] + each[i].swapcase() + each[i + 1:])
        return res
