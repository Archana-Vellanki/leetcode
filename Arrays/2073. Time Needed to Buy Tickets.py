# 2073. Time Needed to Buy Tickets
# Solved
# Easy
# Topics
# Companies
# Hint
# There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

# You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].

# Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

# Return the time taken for the person at position k (0-indexed) to finish buying tickets.


# Example 1:

# Input: tickets = [2,3,2], k = 2
# Output: 6
# Explanation:
# - In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
# - In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0].
# The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.
# Example 2:

# Input: tickets = [5,1,1,1], k = 0
# Output: 8
# Explanation:
# - In the first pass, everyone in the line buys a ticket and the line becomes [4, 0, 0, 0].
# - In the next 4 passes, only the person in position 0 is buying tickets.
# The person at position 0 has successfully bought 5 tickets and it took 4 + 1 + 1 + 1 + 1 = 8 seconds.


# Constraints:

# n == tickets.length
# 1 <= n <= 100
# 1 <= tickets[i] <= 100
# 0 <= k < n

# Time complexity: O(n)
# Space Complexity: O(1)

# Approach: Updating the number of tickets in-place in tickets array. So for the first iteration, the number of tickets of person at 0th index reduces by 1 and time increase by 1 second.
# For the second iteration, the number of tickets of the 1st index person decreases by 1 and time increases by 1 second.
# Once we reach the end of the loop, we will iterate from the 0th index again.
# This repeats till the number of tickets of k-th person is not 0.
# If during this process, any person's tickets becomes 0, it means he will leave the queue.
# if the index == k, return time.
# else, pop the person at that index.
# but we have to be careful to update the k value, if the popped index is less than k,, we have to decrement k by 1 because its updated index is reduced by 1
# Example: Suppose, at one point, the tickets = [2, 3, 0, 7], k = 3 since i=2 has 0 tickets, it will be popped. then the array becomes => [2,3,7] so the k should be updated to 2.

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        while (tickets[k] > 0):
            i = 0
            length = len(tickets)
            while i < length:
                tickets[i] -= 1
                time += 1
                if tickets[i] == 0:
                    if i == k:
                        return time
                    elif i < k:
                        tickets.pop(i)
                        k -= 1
                        length -= 1
                    else:
                        tickets.pop(i)
                        length -= 1
                        # i += 1
                else:
                    i += 1
        return time
