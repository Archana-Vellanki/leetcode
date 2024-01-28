// 56. Merge Intervals
// Solved
// Medium
// Topics
// Companies
// Given an array of intervals where intervals[i] = [starti, endi], merge all
// overlapping intervals, and return an array of the non-overlapping intervals
// that cover all the intervals in the input.

// Example 1:

// Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
// Output: [[1,6],[8,10],[15,18]]
// Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
// Example 2:

// Input: intervals = [[1,4],[4,5]]
// Output: [[1,5]]
// Explanation: Intervals [1,4] and [4,5] are considered overlapping.

// Constraints:

// 1 <= intervals.length <= 104
// intervals[i].length == 2
// 0 <= starti <= endi <= 104

// Time complexity: O(nlogn)
// Space Complexity: O(n)
// Approach: For every interval check if its overlapping with the previous interval. 
// If so take the minimum lower bound and maximum upper bound for creating the new interval and add it to the result.
// We require two loops because if there is an overlap, we have to continue to check if the next interval is also an overlap and continue further.
import java.util.*;

class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) {
            return intervals;
        }
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        int len = intervals.length;
        int i = 0;
        int k = 0;
        int[][] result = new int[len][];
        while (i < len) {
            i++;
            int low = intervals[i - 1][0];
            int high = intervals[i - 1][1];
            while (i < len && intervals[i][0] <= high) {
                low = Math.min(intervals[i][0], low);
                high = Math.max(intervals[i][1], high);
                i += 1;
            }
            result[k++] = new int[] { low, high };
        }
        return Arrays.copyOfRange(result, 0, k);

    }
}