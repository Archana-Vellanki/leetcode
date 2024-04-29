# 215. Kth Largest Element in an Array
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?


# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4


# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

# Time Complexity: O(klogn)
# Space Complexity: O(1)

# Approach: heapify the array(since python creates min heap as default, but we need max heap, we negate all the elements), then pop k times,return the last popped item(negate) as it is the kth largest element.
# We can also use sorting to get O(nlogn) time complexity


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return sorted(nums)[-k]
        nums = [-i for i in nums]
        heapq.heapify(nums)
        for _ in range(k-1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)
