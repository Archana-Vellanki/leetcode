# 231. Power of Two
# Solved
# Easy
# Topics
# Companies
# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

 

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: n = 3
# Output: false
 

# Constraints:

# -231 <= n <= 231 - 1
 

# Follow up: Could you solve it without loops/recursion?

# Time complexity: O(logn)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count1 = 0
        while n > 0:
            count1 += n & 1
            n = n >>1
            if count1 > 1:
                return False
        return count1 == 1
    
# Approach: Example: 
# n=8
# Binary Representation of 8:
# 1000
# 7 in binary is 0111

# Bitwise AND of 8 and 7:

# 8:  1000
# 7:  0111
#     0000
# The result is 0000, which is 0 in decimal.


# Non-Example: 
# n=10
# Binary Representation of 10: 1010
# 9 in binary is 1001

# Bitwise AND of 10 and 9:


#     1010
# AND 1001
# ----1000
# The result is 1000 which is not 0
# Time complexity: O(1)

def is_power_of_two(n: int) -> bool:
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

        