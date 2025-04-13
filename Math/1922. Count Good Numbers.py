# 1922. Count Good Numbers
# Solved
# Medium
# Topics
# Companies
# Hint
# A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

# For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
# Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

# A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

 

# Example 1:

# Input: n = 1
# Output: 5
# Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
# Example 2:

# Input: n = 4
# Output: 400
# Example 3:

# Input: n = 50
# Output: 564908303
 

# Constraints:

# 1 <= n <= 1015


'''
Digits at even indices can be any of the 5 even digits: 0, 2, 4, 6, 8
Digits at odd indices can be any of the 4 prime digits: 2, 3, 5, 7

The total count of such numbers is: count = 5^even_positions X 4^odd_positions % mod (10^9 + 7)

Key properties used: 
1. Fast exponentiation: 
Since `n` can be very large (up to 10^15), we use fast or modular exponentiation to efficiently compute large powers without overflow.
Ex: 
5^1024
= (5^2)^512        = 25^512
= (25^2)^256       = 625^256
= (625^2)^128      = 390625^128
= (390625^2)^64    = ...
...

2. Modulo multiplication property:  
(a%mod * b%mod * c%mod ...)%mod = (a*b*c)%mod

Time Complexity: O(logn) because of fast exponentiation
Space Complexity: O(1) 

'''

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        e = 5 # all even digits 0,2,4,6,8
        o = 4 # all prime digits: 2 3 5 7
        mod = 10**9 + 7

        def fast_pow(base, exp, mod):
            result = 1
            while exp > 0:
                if exp%2 == 1:
                    result = (result*base)%mod
                base = (base*base)%mod
                exp //= 2
            return result
        

        even_digits = (n+1)//2
        odd_digits = n//2

        return (fast_pow(o, odd_digits, mod) * fast_pow(e, even_digits, mod))%mod
        
