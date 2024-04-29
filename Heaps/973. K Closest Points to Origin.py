# 973. K Closest Points to Origin
# Solved
# Medium
# Topics
# Companies
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).


# Example 1:


# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.


# Constraints:

# 1 <= k <= points.length <= 104
# -104 <= xi, yi <= 104

# Time Complexity: O(klogn) but if k is approximately equal to n, then it is O(nlogn)
# Space complexity: O(n) extra space for storing the distance from origin to each point.

# Approach: for each point, calculate the distance from itself to origin and append it to the front of the element.
# heapify the array, for comparision, the first element will be used which is the distance, so the min heap will be created based on the distance.
# pop for k times and add it to the result to return the k closest points.

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return sqrt(x**2 + y**2)
        for each in points:
            each.insert(0, distance(each[0], each[1]))
        answer = []
        heapq.heapify(points)
        for _ in range(k):
            point = heapq.heappop(points)
            point.pop(0)
            answer.append(point)
        return answer
