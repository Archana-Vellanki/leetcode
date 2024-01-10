// 3. Longest Substring Without Repeating Characters
// Medium
// 34.8K
// 1.6K
// Companies
// Given a string s, find the length of the longest
// substring
// without repeating characters.

// Example 1:

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
// Example 2:

// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
// Example 3:

// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not
// a substring.

// Constraints:

// 0 <= s.length <= 5 * 104
// s consists of English letters, digits, symbols and spaces.

// Approach 2:

// Time Complexity: O(n) just one iteration through the string
// Space Complexity: O(n) hashmap to store chars
// Approach: maintain a hashmap to store chars and their indices, along with
// two pointers(left and right) to indicate the sliding window(current
// substring)
// For every iteration,
// check if the char at the right index is present in the hashmap.
// If it is present, that means it is repeating. move the left pointer ahead
// of it (if it has not crossed it already)
// update the maximum length and the char index in the hashmap
// move the right pointer to the next character
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0, maxLength = 0;
        Map<Character, Integer> currString = new HashMap<>();
        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);
            if (currString.containsKey(ch)) {
                left = Math.max(left, currString.get(ch) + 1);
            }
            currString.put(ch, right);
            maxLength = Math.max(right - left + 1, maxLength);
        }
        return maxLength;
    }
}

// Approach 1:
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0, maxLength = 0;
        Set<Character> currString = new HashSet<>();
        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);
            while (currString.contains(ch)) {
                currString.remove(s.charAt(left));
                left++;
            }
            currString.add(ch);
            maxLength = Math.max(right - left + 1, maxLength);
        }
        return maxLength;
    }
}
