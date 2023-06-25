# 904. Fruit Into Baskets
# Medium

# You are visiting a farm that has a single row of fruit trees arranged from left to right.
# The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree(including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.


# Example 1:

# Input: fruits = [1, 2, 1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:

# Input: fruits = [0, 1, 2, 2]
# Output: 3
# Explanation: We can pick from trees[1, 2, 2].
# If we had started at the first tree, we would only pick from trees[0, 1].
# Example 3:

# Input: fruits = [1, 2, 3, 2, 2]
# Output: 4
# Explanation: We can pick from trees[2, 3, 2, 2].
# If we had started at the first tree, we would only pick from trees[1, 2].


# Constraints:

# 1 <= fruits.length <= 105
# 0 <= fruits[i] < fruits.length


# Time complexity: O(n)traversal only once
# Space complexity: O(1) constant extra space
# Approach: Sliding window technique to findout the longest subarray with just two types of fruits.
# initialize a hashmap representing the basket. and maintain a sliding window with left and right pointers.
# At each iteration:
#   Add the right fruit to the basket and check if the number of types is greater than 2.
#       If yes eliminate the fruit at left index from the basket and increase the left index by 1 and proceed with the next right item.
#   Update the maximum picked at every iteration
# return the max_picked

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        # longest subarray with max frequency

        basket = {}
        max_picked = 0
        left = 0

        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1

            if len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            else:
                max_picked = max(max_picked, sum(basket.values()))

        return max_picked
