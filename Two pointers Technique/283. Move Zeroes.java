// 283. Move Zeroes
// Solved
// Easy
// Topics
// Companies
// Hint
// Given an integer array nums, move all 0's to the end of it while maintaining
// the relative order of the non-zero elements.

// Note that you must do this in-place without making a copy of the array.

// Example 1:

// Input: nums = [0,1,0,3,12]
// Output: [1,3,12,0,0]
// Example 2:

// Input: nums = [0]
// Output: [0]

// Constraints:

// 1 <= nums.length <= 104
// -231 <= nums[i] <= 231 - 1

// Follow up: Could you minimize the total number of operations done?

// Approach: 2 pointers left starting at 0 and right starting at 1. 
// 1: if left is 0 and right is not, swap and increase both pointers by 1
// 2. if left is 0 and right is zero, increment right by 1
// 3. If left is not 0, increment left by 1
// Time Complexity: O(n)
// Space complexity: O(1)

class Solution {
    public void moveZeroes(int[] nums) {
        if (nums.length == 1) {
            return;
        }
        int left = 0, right = 1, len = nums.length;
        while (right < len) {
            if (nums[left] == 0) {
                if (nums[right] == 0) {
                    right += 1;
                } else {
                    nums[left] = nums[right];
                    nums[right] = 0;
                    left += 1;
                }
            } else {
                left += 1;
            }

            if (left == right) {
                right += 1;
            }
        }
    }
}