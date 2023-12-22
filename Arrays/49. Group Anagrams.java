// 49. Group Anagrams
// Solved
// Medium
// Topics
// Companies
// Given an array of strings strs, group the anagrams together. You can return
// the answer in any order.

// An Anagram is a word or phrase formed by rearranging the letters of a
// different word or phrase, typically using all the original letters exactly
// once.

// Example 1:

// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
// Example 2:

// Input: strs = [""]
// Output: [[""]]
// Example 3:

// Input: strs = ["a"]
// Output: [["a"]]

// Constraints:

// 1 <= strs.length <= 104
// 0 <= strs[i].length <= 100
// strs[i] consists of lowercase English letters.

//My solution

// Time complexity: O(m*n)  where m = number of strings in the list, n is the average length of the string
// Space complexity: O(m*n)

// Approach: create a frequency counter for each string. Result is a hashmap with frequency counter as the key and list of strings with same frequency counter as the value.
// once a frequency counter is created, check if the result already contains the frequency counter, 
// if so add the current string to that list. Else create a new list and add the current string to it.
// by the end, you will have a hashmap with frequency counters as the keys and anagram groups as the values. Result the values after converting it to list.

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<HashMap<Character, Integer>, List<String>> result = new HashMap<>();

        List<String> stringList = new ArrayList<String>();

        for (String each : strs) {
            HashMap<Character, Integer> map = new HashMap<>();
            for (int i = 0; i < each.length(); i++) {
                map.put(each.charAt(i), map.getOrDefault(each.charAt(i), 0) + 1);
            }
            // System.out.println(each + "\n" + map.toString() + "\n" +
            // result.containsKey(map));
            if (result.containsKey(map)) {
                stringList = result.remove(map);
                // System.out.println(stringList.toString());
            } else {
                stringList = new ArrayList<String>();
            }
            // System.out.println(stringList.toString()+ "\n\n" );
            stringList.add(each);
            result.put(map, stringList);
            // System.out.println(map.toString() + "\n" + stringList.toString());
            // map.clear();
            // stringList.clear();
            // System.out.println(result.toString()+ "\n");
        }
        return (new ArrayList<>(result.values()));
    }
}

// Using SORTING

// Time complexity: O(m*n*logn) where m = number of strings in the list, n is
// the average length of the string
// Space complexity: O(m*n)

// Approach: for each string, sort it and check if the sorted version is present
// in the map already, is present, add the current string to the list.
// If not create a new key-value pair with sorted string as the key and current
// string as the value.
// Note: All the anagrams will result in the same sorted string. Ex: 'nat',
// 'tan' both result in 'ant' as the sorted string.

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for (String word : strs) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String sortedWord = new String(chars);

            if (!map.containsKey(sortedWord)) {
                map.put(sortedWord, new ArrayList<>());
            }

            map.get(sortedWord).add(word);
        }

        return new ArrayList<>(map.values());
    }
}
