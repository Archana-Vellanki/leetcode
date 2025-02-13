# 227. Basic Calculator II
# Solved
# Medium
# Topics
# Companies
# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "3+2*2"
# Output: 7
# Example 2:

# Input: s = " 3/2 "
# Output: 1
# Example 3:

# Input: s = " 3+5 / 2 "
# Output: 5
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0, 231 - 1].
# The answer is guaranteed to fit in a 32-bit integer.

# Multiplication and Division handling is different from Addition and Subtraction, think why?
# Because they have to be given highest priority and have to be applied only for the immediate operands.
# For example "4 + 6 * 3",here you cannot do 4+6 = 10 then 10/3, it should be 6*3 then add the result to 4
# same is the case for division
# but for addition and subtraction it doesnt require to consider immediate operands
# So process multiplication and division operands then and there and keep adding the operands to the stack for '+', '-' operators.
# For '-' operator just append -num to the stack
# use Math.trunc() to calculate the floor operation, because negative//num moves the result away from 0

# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def calculate(self, s: str) -> int:
        num, sym = 0, "+"
        plusStack = []
        length = len(s)
        for i in range(length):
            ch = s[i]
            if ch.isdigit():
                num = num*10+int(ch)
            if (not ch.isdigit() and not ch==" ") or i == length - 1:
                if sym == "+":
                    plusStack.append(num)
                elif sym == "-":
                    plusStack.append(-num)
                elif sym == "*":
                    plusStack.append(plusStack.pop()*num)
                else:
                    lastElement = plusStack.pop()
                    if lastElement > 0:
                        plusStack.append(lastElement//num)
                    else:
                        plusStack.append(-(-lastElement//num))
                sym = ch
                num = 0
                # print(plusStack)
        return sum(plusStack)
