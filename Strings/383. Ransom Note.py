# 383. Ransom Note
# Solved
# Easy
# Topics
# Companies
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.


# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true


# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.


# Approach: One dictionary to store the letters of the magazine and their counts. 
# As we iterate through the ransom note, decrement the counter and if the counter becomes less than or equal to zero, pop it.
# If at any point the letter in the ransom note is not found in the dictionary, return False. 
# If we complete the iteration without any such case. That means we found all the letters and hence return True

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = Counter(magazine)
        for each in ransomNote:
            if each in hashmap and hashmap[each] > 0:
                hashmap[each] -= 1
            else:
                return False
        return True
