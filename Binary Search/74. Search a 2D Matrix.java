// 74. Search a 2D Matrix

// You are given an m x n integer matrix matrix with the following two
// properties:

// Each row is sorted in non-decreasing order.
// The first integer of each row is greater than the last integer of the
// previous row.
// Given an integer target, return true if target is in matrix or false
// otherwise.

// You must write a solution in O(log(m * n)) time complexity.

// Example 1:

// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
// Output: true
// Example 2:

// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
// Output: false

// Constraints:

// m == matrix.length
// n == matrix[i].length
// 1 <= m, n <= 100
// -104 <= matrix[i][j], target <= 104

// Approach: Binary Search for finding the row and then inside the row binary search again to find the column. 
// time complexity: O(logM + logN)
// Space Complexity: O(1)
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        if (rows == 1 && cols == 1) {
            return matrix[0][0] == target;
        }
        int lo_ro = 0, lo_col = 0, hi_ro = rows - 1, hi_col = cols - 1;

        // Binary search for finding the row
        int mid_ro = (lo_ro + hi_ro) / 2;
        while (lo_ro < hi_ro) {
            if (target < matrix[mid_ro][0]) {
                hi_ro = mid_ro - 1;
            } else if (target > matrix[mid_ro][cols - 1]) {
                lo_ro = mid_ro + 1;
            } else {
                break;
            }
            mid_ro = (lo_ro + hi_ro) / 2;
        }
        if (lo_ro > hi_ro) {
            return false;
        }

        // Binary search for finding the col
        int mid_col = (lo_col + hi_col) / 2;
        while (lo_col < hi_col) {

            if (target < matrix[mid_ro][mid_col]) {
                hi_col = mid_col - 1;
            } else if (target > matrix[mid_ro][mid_col]) {
                lo_col = mid_col + 1;
            } else {
                return true;
            }
            mid_col = (lo_col + hi_col) / 2;
        }
        if (lo_ro > hi_ro || lo_col > hi_col) {
            return false;
        } else {
            return matrix[mid_ro][mid_col] == target;
        }
    }
}