# 1046. Last Stone Weight
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is :

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.


# Example 1:

# Input: stones = [2, 7, 4, 1, 8, 1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to[2, 4, 1, 1, 1] then,
# we combine 2 and 4 to get 2 so the array converts to[2, 1, 1, 1] then,
# we combine 2 and 1 to get 1 so the array converts to[1, 1, 1] then,
# we combine 1 and 1 to get 0 so the array converts to[1] then that's the value of the last stone.
# Example 2:

# Input: stones = [1]
# Output: 1


# Constraints:

# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000

# Time complexity: O(nlogn)
# Space Complexity: O(1)
# Approach: heapify the array, be mindful that the default heapify creates min heap in Python. To get maxHeap, negate the elements and then heapify
# iterate through the heap till its length is greater than 1, in each iteration pop two elements(and negate them) y and x.
#  if y!= x, then update the y value as mentioned in the problem description and push it again to the heap
# Finally if the array is empty return 0 else return the only element(negate)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while (len(stones) > 1):
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if x != y:
                y = -y + x
                heapq.heappush(stones, y)
            # if len(stones) == 0:
            #     heapq.heappush(stones, y)
        return -stones[0] if stones else 0
