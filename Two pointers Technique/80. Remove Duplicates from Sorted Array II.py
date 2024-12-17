# 80. Remove Duplicates from Sorted Array II
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.


# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# Constraints:

# 1 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.


# My solution:
# Check Optimised solution as well


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 2:
            return length
        i, j, k = 0, 0, 1
        while j < length:
            while k < length and nums[j] == nums[k]:
                k += 1
            freq = min(k - j, 2)
            element = nums[j]
            while freq > 0:
                nums[i] = element
                i += 1
                freq -= 1
            j = k
            k += 1
        return i


# Optimized Solution:
# Approach
# The solution approach involves iterating through the input array nums and maintaining two pointers, index and occurrence. The index pointer represents the length of the modified array, and the occurrence pointer tracks the number of occurrences of the current element.


# Initialize index to 1 (for the first element) and occurrence to 1.
# Iterate through the array, starting from index 1.
# If the current element is equal to the previous one, increment occurrence.
# If not, reset occurrence to 1.
# If occurrence is less than or equal to 2, update nums[index] with the current element and increment index.
# Continue until the end of the array.
# Complexity
# Time complexity: O(n)
# Space complexity: O(1)
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        index = 1
        occurance = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                occurance += 1
            else:
                occurance = 1

            if occurance <= 2:
                nums[index] = nums[i]
                index += 1

        return index
