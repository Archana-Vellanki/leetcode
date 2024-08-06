# 567. Permutation in String
# Solved
# Medium
# Topics
# Companies
# Hint
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        string1 = {chr(i):0 for i in range(97,123)}
        string2 = {chr(i):0 for i in range(97,123)}
        for each in s1:
            string1[each] = string1.get(each, 0) + 1
        len1 = len(s1)
        len2 = len(s2)

        for each in s2[:len1]:
            string2[each] = string2.get(each, 0) + 1
        
        matches = 0

        for i in range(97,123):
            if string1[chr(i)] == string2[chr(i)]:
                matches += 1
        if matches == 26:
            return True
        # print(matches)
        for i in range(len1, len2):
            # prev1 is true if they match before updating
            prev = string2[s2[i]] == string1[s2[i]]
            # print(s2[i], " previously matching: ", prev)
            # updated
            string2[s2[i]] += 1
            # if it matches after updating, increment the matches by 1
            if string2[s2[i]] == string1[s2[i]]:
                matches += 1
            else:
                if prev:
                    matches -= 1
            prev = string2[s2[i-len1]] == string1[s2[i-len1]]
            # print(s2[i-len1], " previously matching: ", prev)
            string2[s2[i-len1]] -= 1
            if string2[s2[i-len1]] == string1[s2[i-len1]]:
                matches += 1
            else:
                if prev:
                    matches -=1
            # print(matches)
            if matches == 26:
                return True
        return matches == 26
