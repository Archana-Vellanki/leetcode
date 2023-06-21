# 322. Coin Change
# Medium

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.


# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0


# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104


# Time Complexity: O(n*m) where n is the amount and m is the number of coins
# Space Complexity: O(n)
# Approach: Dynamic Programming approach- To avoid recalculation of the same amount, we will use memoization to store the minimum coins required for each amount calculated.
# create an array of length equal to amount.
# Then, we iterate over the amounts from 1 to amount and for each amount, iterate over the available coins.
# If the coin value is less than or equal to the current amount (coin <= i),
# we update dp[i] by taking the minimum between its current value and dp[i - coin] + 1,
# which represents the minimum number of coins needed to reach the remaining amount after using the current coin.
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        mem = [float('inf')]*(amount + 1)
        mem[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    mem[i] = min(mem[i], mem[i - coin] + 1)
        return mem[amount] if mem[amount] != float('inf') else -1
