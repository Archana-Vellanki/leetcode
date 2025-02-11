# 1249. Minimum Remove to Make Valid Parentheses
# Solved
# Medium
# Topics
# Companies
# Hint
# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either '(' , ')', or lowercase English letter.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = set()
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    remove.add(i)
        result = []
        for each in stack:
            remove.add(each)
        for i in range(len(s)):
            if i not in remove:
                result.append(s[i])
        return "".join(result)

  # Optimizations: 
  # 1. no need of stack - we can just use a counter to find the number of open brackets and reduce it when we find the balancing closing bracket 
  # 2. We can skip "remove" set, we can have a result array and skip adding the invalid closed brackets to it.
  # 3. In order to handle the invalid open brackets, we can count the total number of open brackets that we encountered and subtract the invalid brackets count from it. This will give the valid open brackets to be added to the result. Thes rest of the open brackets need not be added to the reuslt.
