# 846. Hand of Straights
# Solved
# Medium
# Topics
# Companies
# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.


# Example 1:

# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
# Example 2:

# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.


# Constraints:

# 1 <= hand.length <= 104
# 0 <= hand[i] <= 109
# 1 <= groupSize <= hand.length


# Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        answer = 0
        i = 0
        currentGroup = []
        while i < len(hand):
            i = 0
            card = hand.pop(i)
            currentGroup.append(card)
            while i < len(hand) and len(currentGroup) < groupSize:
                if card == hand[i]:
                    i += 1

                elif hand[i] == card + 1:
                    card = hand.pop(i)
                    currentGroup.append(card)
                else:
                    return False
            # print("current Group: ", currentGroup)
            if len(currentGroup) == groupSize:
                answer += 1
                currentGroup = []
            else:
                return False
        if hand == []:
            return True
        return False
