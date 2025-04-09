# 57. Insert Interval
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

# Constraints:

# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105

# Intuition: Segregate intervals into three groups: those completely before the new interval, those overlapping with it, and those completely after it. Merge the overlapping intervals into one.

# Implementation:
# Append non-overlapping intervals before the new interval.
# Update the new interval’s boundaries while merging with any overlapping intervals.
# Append the merged interval and any remaining intervals after it.

# Time Complexity: O(n)
# Space Complexity: O(n) (if we count the output)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        merged_array = []
        i, length = 0, len(intervals)
        start, end = newInterval[0], newInterval[1]

        while i < length and start > intervals[i][1]:
            i += 1

        merged_array.extend(intervals[:i])
            
        while i < length and end >= intervals[i][0]:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        merged_array.append((start, end))

        if i < length:
            merged_array.extend(intervals[i:])
        return merged_array

# '''
# Find the right index of the correct position to insert the interval. 
# check with end of left interval and start of the right interval iteratively and if they are overlapping remove it.
# '''
# start, end = newInterval[0], newInterval[1]
# length = len(intervals)
# l, r = 0, length - 1

# while l < r:
#     mid = (l + r)//2
#     if intervals[mid][0] >= start and intervals[mid][1] :
#         r = mid
#     else:
#         l = mid + 1
# index = r
# start, end = min(start, intervals[index][0]), max(end, intervals[index][1])
# # l -= 1
# r = length - 1
# while l < r:
#     mid = (l+r)//2
#     if intervals[mid][1] <= end:
#         l = mid + 1
#     else:
#         r = mid - 1
# right2 = r if r < length else length - 1

# while l >= 0 and intervals[l][1] <= start:
#     l -= 1
