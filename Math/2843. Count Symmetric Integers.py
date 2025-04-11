# 2843. Count Symmetric Integers
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given two positive integers low and high.

# An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.

# Return the number of symmetric integers in the range [low, high].

 

# Example 1:

# Input: low = 1, high = 100
# Output: 9
# Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.
# Example 2:

# Input: low = 1200, high = 1230
# Output: 4
# Explanation: There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.
 

# Constraints:

# 1 <= low <= high <= 104

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        symm_count = 0
        for num in range(low, high + 1):
            n = str(num)
            
            if len(n) %2:
                continue
            # else:
            digits = len(n)//2
            if sum(int(d) for d in n[:digits]) == sum(int(d) for d in n[digits:]): 
                symm_count += 1
        return symm_count

  # diff = high - low
  # can we find the number of digits in constant time?
  # yes: math.floor(math.log10(abs(n))) + 1

  # Brute force: iterate from low to high + 1 and find if each is symmetric
  # Possible Optimizations: 2530 half_sum = 7,so we need not increase by +1 and check every possibility. we can skip some of them

  # can we use dp for this?? (sum,digits): possibilities 
  # ex: (1:1):[1], (1,2):[10,01], (1,3):[100,010,001], (1,4): [1]
