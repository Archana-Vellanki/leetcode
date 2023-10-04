// 912. Sort an Array
// Medium
// 5.5K
// 720
// Companies
// Given an array of integers nums, sort the array in ascending order and return it.

// You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

// Example 1:

// Input: nums = [5,2,3,1]
// Output: [1,2,3,5]
// Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
// Example 2:

// Input: nums = [5,1,1,2,0,0]
// Output: [0,0,1,1,2,5]
// Explanation: Note that the values of nums are not necessairly unique.

// Constraints:

// 1 <= nums.length <= 5 * 104
// -5 * 104 <= nums[i] <= 5 * 104

/**
 * Divide and Conquer: Divide the array upto single elements and then merge them
 * according to the sorting order. Sorting happens only while merging.
 */

class Solution {
    public int[] sortArray(int[] nums) {
        if (nums.length <= 1) {
            return nums;
        }
        int[] firstHalf = sortArray(Arrays.copyOfRange(nums, 0, nums.length / 2));
        int[] secondHalf = sortArray(Arrays.copyOfRange(nums, nums.length / 2, nums.length));

        // merge two sorted arrays
        int[] result = new int[nums.length];
        int i = 0;
        int j = 0;
        int k = 0;
        while (i < firstHalf.length && j < secondHalf.length) {
            if (firstHalf[i] <= secondHalf[j]) {
                result[k] = firstHalf[i];
                i++;
            } else {
                result[k] = secondHalf[j];
                j++;
            }
            k++;
        }
        while (i < firstHalf.length) {
            result[k] = firstHalf[i];
            i++;
            k++;
        }
        while (j < secondHalf.length) {
            result[k] = secondHalf[j];
            j++;
            k++;
        }
        return result;
    }
}
