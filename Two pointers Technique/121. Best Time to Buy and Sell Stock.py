# 121. Best Time to Buy and Sell Stock
# Easy

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/1735550/python-javascript-easy-solution-with-very-clear-explanation/

# Time complexity: O(n)
# Space complexity: O(1)

# Approach:
# diff = right - left
# if we want maximum diff, right should be max and left should be min
# that means we should try for minimum left but instead of trying to find the maximum right value, we will iterate through the array for different values of right. At each iteration update the maximum diff.
# IF at any position, right < Left it means that we have found a new minimum at right index. Hence reassign left = right and right = right + 1. starting from that index again.
# Time complexity: O(n)
# Space complexity: O(1)


# Simpler approach
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        left = 0
        right = 1
        max_profit = 0
        while right < length:
            if prices[right] < prices[left]:
                left = right
            max_profit = max(max_profit, prices[right] - prices[left])
            right += 1
        return max_profit
        
# Step-by-step procedure:
# Maintain two pointers left and right and max_profit to store the maximum profit
# the left pointer indicates the day to buy the stock, the right indicates the day to sell the stock
# so (right - left) should be maximum to get maximum profit
# start with left as 0 and right as 1 and run the loop till right < length
# At each step, check if left < right
# if true, it means we will get some non-zero profit. update the maximum profit if current profit is greater than the maximum profit and just move the right pointer by 1
# (do not move the left pointer, since it is the minimum value)
# if False, it means we wont get any profit hence ignore calculating and updating the max_profit,
# and also it means that we have found new minimum value at right position, hence update left = right and increase the right value by 1

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        left = 0
        right = 1
        max_profit = 0
        while right < length:
            if prices[left] < prices[right]:
                # we get profit
                profit = prices[right] - prices[left]
                if profit > max_profit:
                    max_profit = profit
            else:
                left = right
            right += 1
        return max_profit
