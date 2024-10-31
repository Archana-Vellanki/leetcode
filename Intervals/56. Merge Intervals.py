# 56. Merge Intervals
# Solved
# Medium
# Topics
# Companies
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

# Approach:sort the intervals based on the start times. 
# Iterate through the intervals
# if you find an interval that is overalping with the previous one, 
#   update the end to be max(end, current interval end) - To merge all the small overlapping intervals to one big interval 
# if the current interval is not overlapping, begin a new interval with the start and end values.

# Time complexity: O(nlogn)
# space Complexity: O(n) including the result. else O(1)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals = sorted(intervals, key=lambda x:x[0])
        start, end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(intervals[i][1], end)
            else:
                result.append((start, end))
                start = intervals[i][0]
                end = intervals[i][1]
        result.append((start, end))
        return result
