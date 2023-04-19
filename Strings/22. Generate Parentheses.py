# 22. Generate Parentheses
# Medium
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


# Constraints:

# 1 <= n <= 8


# Backtracking approach - to find all the possibilities
# https://redquark.org/leetcode/0022-generate-parentheses/
# https://medium.com/javarevisited/solve-leetcode-problems-and-get-offers-from-your-dream-companies-232cf97cc9dd

# when n = 2
# 			   	(0, 0, '')
# 			 	    |
# 				(1, 0, '(')
# 			   /           \
# 		(2, 0, '((')      (1, 1, '()')
# 		   /                 \
# 	(2, 1, '(()')           (2, 1, '()(')
# 	   /                       \
# (2, 2, '(())')                (2, 2, '()()')
# 	      |	                             |
# res.append('(())')             res.append('()()')

# when n = 3
# generate called for :           left : 0    right : 0
# generate called for : (         left : 1    right : 0
# generate called for : ((        left : 2    right : 0
# generate called for : (((       left : 3    right : 0
# generate called for : ((()      left : 3    right : 1
# generate called for : ((())     left : 3    right : 2
# generate called for : ((()))    left : 3    right : 3

# generate called for : (()       left : 2    right : 1
# generate called for : (()(      left : 3    right : 1
# generate called for : (()()     left : 3    right : 2
# generate called for : (()())    left : 3    right : 3

# generate called for : (())      left : 2    right : 2
# generate called for : (())(     left : 3    right : 2
# generate called for : (())()    left : 3    right : 3

# generate called for : ()        left : 1    right : 1
# generate called for : ()(       left : 2    right : 1
# generate called for : ()((      left : 3    right : 1
# generate called for : ()(()     left : 3    right : 2
# generate called for : ()(())    left : 3    right : 3

# generate called for : ()()      left : 2    right : 2
# generate called for : ()()(     left : 3    right : 2
# generate called for : ()()()    left : 3    right : 3

# answer -> ((())) (()()) (())() ()(()) ()()()

# Time complexity: O(2^N)
# each string length= 2*N
# each position in the output string, two choices - either to add '(' or ')'.
# For N pairs of parentheses, there are a total of 2N positions to be filled in the output string.
# Hence, there are 2^(2N) possible combinations of parentheses that can be generated.

# Space complexity: O(2^N)
# To store all the possibilities

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ["()"]
        result = []
        self.generate(result, 0, 0, n, "")
        return result

    def generate(self, result, left, right, n, string):
        if left == n and right == left:
            result.append(string)

        if left < n:
            self.generate(result, left+1, right, n, string + "(")

        if right < left:
            self.generate(result, left, right+1, n, string + ")")
