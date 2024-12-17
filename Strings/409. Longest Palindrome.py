# 409. Longest Palindrome
# Solved
# Easy
# Topics
# Companies
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
# palindrome
#  that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.

# Even count characters can be added to the result with no modification. But odd count characters can be considered at most one for the center position.
# The rest of their occurrences will pair up to maintain symmetry. 
# Examples:
# aabb - abba or baab
# abbca - abcba 
# aabbcd - abcba or abdba so either c or d can be considered but not both
# aabbccc - abcccba; here even though c is odd count character, we need to consider the 3 c's to form the longest palindrome 
#     because 1 c can be used for center of the palindrome
# aabbcccddd - here we will consider 2a's, 2b's, 2c's, 2d's and 1c/d = making the length 9. 
# so all we need to do is to keep a flag to check if there are any odd count characters in the string. We can use count - 1 chacarerts of it to ensure symmetry.
# but finally add 1 to the result if there is atleast 1 odd count character in the string.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        result = 0 
        odd = 0
        for each in freq:
            if freq[each]%2 == 0:
                result += freq[each]
            else:
                result += freq[each] - 1
                if not odd:
                    odd = 1
                
        return result + odd
