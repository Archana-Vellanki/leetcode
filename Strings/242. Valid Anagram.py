# 242. Valid Anagram
# Solved
# Easy
# Topics
# Companies
# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# Approach: use a hashmap to store the frequencies of each character in s. While iterating through t, reduce the count of each character 
# By the end of the iteration if the hashmap is empty that means it is a valid anagram of s, hence return true; return false otherwise

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_map = {}
        for each in s:
            if each in frequency_map:
                frequency_map[each] += 1
            else:
                frequency_map[each] = 1
        for each in t:
            if each in frequency_map:
                frequency_map[each] -= 1
                if frequency_map[each] == 0:
                    frequency_map.pop(each)
            else:
                return False
        return frequency_map == {}
        
