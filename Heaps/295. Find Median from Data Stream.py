# 295. Find Median from Data Stream
# Solved
# Hard
# Topics
# Companies
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
 

# Constraints:

# -105 <= num <= 105
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 104 calls will be made to addNum and findMedian.
 

# Follow up:

# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

# Time Complexity:
# AddNum - O(logn) where n is the size of the stream
# median: O(1)

# Approach:
# Use two heaps to maintain the first half and second half number of elements of the stream

# While addng a number:
# Add the number to heap1. 
# To ensure that the order is intact, pop the highest element from heap1 and add that to heap2.
# If heap2 size is greater, we will pop from heap2 and push to heap1. 

# For finding the median:
# If there are odd number of elements, heap1 would be having that middle element. so return the max element from heap1.
# Else, take highest from heap1 and lowest from heap 2 and return the average of them.


class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []
        self.size1 = 0
        self.size2 = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap1, -num)
        hi = -heapq.heappop(self.heap1)
        heapq.heappush(self.heap2, hi)
        self.size2 += 1
        
        if self.size2 > self.size1:
            lo = heapq.heappop(self.heap2)
            heapq.heappush(self.heap1, -lo)
            self.size2 -= 1
            self.size1 += 1  

    def findMedian(self) -> float:
        total = self.size1 + self.size2
        if total%2:
            # odd number of elements
            return -self.heap1[0]
        return (-self.heap1[0] + self.heap2[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
