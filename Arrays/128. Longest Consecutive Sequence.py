# 128. Longest Consecutive Sequence
# Solved
# Medium
# Topics
# Companies
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109



# Intuition:
    # Convert the list to a hash set for constant-time lookups. For each number, expand downward and upward to find its consecutive sequence, removing numbers as they're encountered to avoid duplicates.

# Implementation Explanation:
    # Initialization:
        # Create a set from the list.
        # Initialize max_length to track the longest sequence.

    # Expansion:
        # For each number, decrement to find the lower bound until a number is missing.
        # Increment from one above the original number to find the upper bound.
        # The sequence length is end - start - 1.

    # Update Result:
        # Update max_length with the maximum sequence length found.

# Time Complexity: O(n) – Each element is processed once.
# Space Complexity: O(n) – The hash set stores all elements.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Thought process:
        idea 1:
        can we create an arr of size max(arr) - min(arr) and add elements to it but the time complexity would be O(max-min)
        
        idea 2:

        can we use doubly linkedlist
        each node contains:
        prev, next, length of the consecutive elements till now
        knowledge gap:How and where should we define node??
        drawbacks: where should we insert a new node? it takes O(n^2)

        solution: hashmap(value:node)
        while inserting a new node, check if its neighbours are in the hashmap, if so append the current node to that node.
        '''
        # implementing hashtable approach
        max_length = 0
        num_set = set(nums)
        for each in nums:
            start = each
            # expanding lower limits
            while start in num_set:
                num_set.remove(start)
                start = start -1
            
            end = each + 1
            # expanding upper limits
            while end in num_set:
                num_set.remove(end)
                end = end + 1

            max_length = max(end - start -1, max_length)

        return max_length
