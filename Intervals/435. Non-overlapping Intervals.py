# 435. Non-overlapping Intervals
# Solved
# Medium
# Topics
# Companies
# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

 

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

# Constraints:

# 1 <= intervals.length <= 105
# intervals[i].length == 2
# -5 * 104 <= starti < endi <= 5 * 104

# Approach:
# Remove minimum intervals means keep maximum intervals. 
# that means we have to remove the large intervals that overlap with other intervals and keep the smaller ones.
# sort based on end times ==> keep the smaller intervals to the beginning and larger overlapping intervals to the later positions
# In the sorted list, if an interval is overlapping with the previous interval, it will be counted as an overlapping interval
# If not update the previous value.
# The count will be returned as the minimum number of overlapping intervals to be removed.

# Time Complexity: O(nlogn) because of sorting
# Space Complexity: O(1)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals, key= lambda each:each[1])
        # print(intervals)
        prev_end = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                count += 1
            else:
                prev_end = intervals[i][1]
            # print(i, count, prev_end)
        return count
