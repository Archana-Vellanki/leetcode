// 242. Valid Anagram
// Solved
// Easy
// Topics
// Companies
// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// Example 1:

// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:

// Input: s = "rat", t = "car"
// Output: false

// Constraints:

// 1 <= s.length, t.length <= 5 * 104
// s and t consist of lowercase English letters.

// Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

// My solution:
// Approach: create a frequency hashmap for s. then iterate over t and for each character, decrement the counter in the frequency hashmap. 
// Post decrement, if the counter has become 0, pop that character from the hashmap. 
// if a character is not found in the hashmap, it means t is not an anagram of s.
// Time complexity: O(n)
// Space complexity: O(n) max 26 because strings contain only lowercase english letters
class Solution {
    public boolean isAnagram(String s, String t) {
        int slen = s.length();
        if (slen != t.length()) {
            return false;
        }
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < slen; i++) {
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
        }
        int count = 0;
        for (int i = 0; i < slen; i++) {
            count = map.getOrDefault(t.charAt(i), -1);
            if (count - 1 > 0) {
                map.put(t.charAt(i), count - 1);
            } else if (count - 1 == 0) {
                map.remove(t.charAt(i));
            } else if (count == -1) {
                return false;
            }

        }
        return (map.isEmpty());
    }
}

// Ideal solution:
// Approach: create an integer array of size 26 each index indicating the
// letters from a - z.
// Time complexity: O(n)
// Space complexity: O(1) array is of constant size 26
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int map[] = new int[26];
        for (char x : s.toCharArray()) {
            map[x - 'a']++;
        }
        for (char x : t.toCharArray()) {
            map[x - 'a']--;
        }
        for (int i : map) {
            if (i != 0) {
                return false;
            }
        }
        return true;
    }
}