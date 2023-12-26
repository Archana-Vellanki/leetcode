// 347. Top K Frequent Elements
// Solved
// Medium
// Topics
// Companies
// Given an integer array nums and an integer k, return the k most frequent
// elements. You may return the answer in any order.

// Example 1:

// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]
// Example 2:

// Input: nums = [1], k = 1
// Output: [1]

// Constraints:

// 1 <= nums.length <= 105
// -104 <= nums[i] <= 104
// k is in the range [1, the number of unique elements in the array].
// It is guaranteed that the answer is unique.

// Follow up: Your algorithm's time complexity must be better than O(n log n),
// where n is the array's size.

// My solution
// Time complexity:O(nlogn)
// Space complexity:O()

// Approach: sort the array, calculate the frequencies of each integer in the
// array.
// create a treemap with frequency as the key and the list of integers which
// have the same frequency as the value.
// create an array of size k for result. pop the max entry from the treemap
// which gives the list of elements with maximum frequency. Check the size and
// add the elements to the result.

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        TreeMap<Integer, ArrayList<Integer>> treeMap = new TreeMap<>();
        int[] result = new int[k];
        int i = 0, counter = 0, len = nums.length;
        Arrays.sort(nums);
        while (i < len) {
            counter = 1;
            while (i < len - 1 && nums[i] == nums[i + 1]) {
                counter += 1;
                i += 1;
            }
            if (treeMap.containsKey(counter)) {
                ArrayList<Integer> value = treeMap.get(counter);
                value.add(nums[i]);
                treeMap.put(counter, value);

            } else {
                treeMap.put(counter, new ArrayList<>(Arrays.asList(nums[i])));
            }
            i += 1;
        }
        i = 0;
        int j;
        while (i < k) {
            ArrayList<Integer> list = treeMap.pollLastEntry().getValue();
            // System.out.println(list.toString());
            j = 0;
            while (j < list.size() && i < k) {
                result[i] = list.get(j);
                i++;
                j++;
            }
            // i++;
        }
        return (result);
    }
}

// Second approach: If sorting has to be skipped, the frequency counter
// (hashmap(element:frequency))can be calculated using a single loop.
// but keep track of the max frequency.
// for the result, start with max freuency, add the elements with that max
// frequency to the result,
// for the next iteration, decrease the max frequency by 1 and check if the
// hashmap contains elements with this frequency and add them to the result
// continue until the result size reaches k and return the result.

// Time complexity: O(n)
// Space complexity O(n)

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        TreeMap<Integer, LinkedList<Integer>> treeMap = new TreeMap<>();
        Map<Integer, Integer> freqMap = new HashMap<>();
        int maxFreq = 0;
        for (int j = 0; j < nums.length; j++) {
            int freq = freqMap.getOrDefault(nums[j], 0) + 1;
            freqMap.put(nums[j], freq);
            if (freq > maxFreq) {
                maxFreq = freq;
            }
        }

        for (Map.Entry<Integer, Integer> each : freqMap.entrySet()) {
            if (!treeMap.containsKey(each.getValue())) {
                treeMap.put(each.getValue(), new LinkedList<>());
            }
            treeMap.get(each.getValue()).add(each.getKey());
        }

        int[] result = new int[k];
        int i = 0;
        // int j;
        while (i < k) {
            ListIterator<Integer> list = treeMap.get(maxFreq).listIterator();
            // System.out.println(list.toString());

            while (list.hasNext() && i < k) {
                result[i] = list.next();
                i++;
            }
            while (--maxFreq > 0 && !treeMap.containsKey(maxFreq)) {
            }
        }
        return (result);
    }
}
