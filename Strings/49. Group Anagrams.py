# 49. Group Anagrams
# Solved
# Medium
# Topics
# Companies
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Using SORTING

# Time complexity: O(m*n*logn) where m = number of strings in the list, n is
# the average length of the string
# Space complexity: O(m*n)

# Approach: for each string, sort it and check if the sorted version is present
# in the map already, is present, add the current string to the list.
# If not create a new key-value pair with sorted string as the key and current
# string as the value.
# Note: All the anagrams will result in the same sorted string. Ex: 'nat',
# 'tan' both result in 'ant' as the sorted string.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for each in strs:
            sorted_str = str(sorted(each))
            if sorted_str in hashmap:
                hashmap[sorted_str].append(each)
            else:
                hashmap[sorted_str] = [each]
        return list(hashmap.values())


# Time complexity: O(m*n*logn)  where m = number of strings in the list, n is the average length of the string
# Space complexity: O(m*n)

# Approach: create a frequency counter for each string. Result is a hashmap with frequency counter as the key and list of strings with same frequency counter as the value.
# once a frequency counter is created, check if the result already contains the frequency counter,
# if so add the current string to that list. Else create a new list and add the current string to it.
# by the end, you will have a hashmap with frequency counters as the keys and anagram groups as the values. Result the values after converting it to list.
# from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for each in strs:
            # since counter is not hashable, we have to use a sorted tuple as a key
            counter = tuple(sorted(Counter(each).items()))
            print(counter)
            if counter in hashmap:
                hashmap[counter].append(each)
            else:
                hashmap[counter] = [each]
        return list(hashmap.values())
