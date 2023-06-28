# 424. Longest Repeating Character Replacement
# Medium
# 8.4K
# 362
# Companies
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.


# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achive this answer too.


# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

# Time complexity: O(26*n) == O(n)
# Space Complexity: O(26) == O(1)

# Approach: The problem requires us to return the length of the longest substring with repeating characters (all same characters) with at most k charcater conversions.
# i.e., we can convert at most k characters to any uppercase character to get the longest substring with repeating characters
# for a given substring, find the most frequent character.
# count the other characters(all characters other than most frequent character) in the substring.
# if the count is less than k, then the given substring is valid. (we can convert all the other characters to the most freq character)
# if it is not valid, reduce the length of the substring from the left and repeat
# As we come across each valid substring, ensure to update the maximum length if the substring exceeds the current maximum length.


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        hashmap = {}
        maxFreq = 0
        result = 0

        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            maxFreq = max(maxFreq, hashmap[s[right]])
            if right - left + 1 - maxFreq <= k:
                # valid window
                result = max(result, right - left + 1)
            else:
                hashmap[s[left]] = hashmap.get(s[left], 0) - 1
                maxFreq = max(hashmap.values())
                left += 1

        return result
