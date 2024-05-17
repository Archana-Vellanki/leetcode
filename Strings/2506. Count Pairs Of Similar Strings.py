# 2506. Count Pairs Of Similar Strings
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given a 0-indexed string array words.

# Two strings are similar if they consist of the same characters.

# For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
# However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
# Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.


# Example 1:

# Input: words = ["aba","aabb","abcd","bac","aabc"]
# Output: 2
# Explanation: There are 2 pairs that satisfy the conditions:
# - i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'.
# - i = 3 and j = 4 : both words[3] and words[4] only consist of characters 'a', 'b', and 'c'.
# Example 2:

# Input: words = ["aabb","ab","ba"]
# Output: 3
# Explanation: There are 3 pairs that satisfy the conditions:
# - i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'.
# - i = 0 and j = 2 : both words[0] and words[2] only consist of characters 'a' and 'b'.
# - i = 1 and j = 2 : both words[1] and words[2] only consist of characters 'a' and 'b'.
# Example 3:

# Input: words = ["nba","cba","dba"]
# Output: 0
# Explanation: Since there does not exist any pair that satisfies the conditions, we return 0.


# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consist of only lowercase English letters.

# Time complexity: O(n)
# Space complexity: O(n)
# Approach: The `similarPairs` method counts pairs of words that contain the exact same set of characters in a given list.
# It does this by converting each word into a set of its unique characters and storing
# these sets as keys in a dictionary, with their frequencies as values.
# For each set that appears more than once, it calculates the number of ways two words can be chosen from
# those appearing with the same set of characters using the combination formula, efficiently implemented with bit shifting for division.
# The method then sums these values to determine the total number of similar word pairs.

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        result = {}
        for each in words:
            wordSet = frozenset(each)
            if wordSet in result:
                result[wordSet] += 1
            else:
                result[wordSet] = 1
        # print(result.items())
        answer = 0
        for each in result:
            if result[each] > 1:
                answer += (result[each] * (result[each] - 1)) >> 1
        return answer