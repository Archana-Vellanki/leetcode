# 844. Backspace String Compare
# Solved
# Easy
# Topics
# Companies
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.


# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".


# Constraints:

# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.


# Follow up: Can you solve it in O(n) time and O(1) space?
# To-do


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for each in s:
            if each == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(each)
            # print(each, stack)
        stack2 = []
        for each in t:
            if each == '#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(each)
        print(stack, stack2)
        return stack == stack2


# yet to do O(n) time and O(1) space
