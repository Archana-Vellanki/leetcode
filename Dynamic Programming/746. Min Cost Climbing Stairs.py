# 746. Min Cost Climbing Stairs
# Solved
# Easy
# Topics
# Companies
# Hint
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.


# Example 1:

# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
# Example 2:

# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.


# Constraints:

# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

# Approach: Maintain an array minCost to store the minimum cost required from the current step to the top of the floor.
# since we can climb upto 2 stairs at once, the minimum cost for last 2 stairs is same as the cost.
# we iterate from last but second step onwards to the beginning.
# In each iteration we update the minimum cost to be sum of the current cost at that index i.e. cost[i] and minimum of minCost[i+1] and minCost[i+2].
# By the end of the loop we will have the minimum cost to be paid at each index to reach the top of the floor.
# Since we can start from index 0 or 1, we will return minimum of minCost[0], minCost[1]

# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        minCost = [999000 for i in range(length)]
        minCost[length-1] = cost[length-1]
        minCost[length-2] = cost[length-2]
        for i in range(length-3, -1, -1):
            minCost[i] = cost[i] + min(minCost[i+1], minCost[i+2])
        return min(minCost[0], minCost[1])
