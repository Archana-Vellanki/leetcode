# 1306. Jump Game III
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

# Notice that you can not jump outside of the array at any time.

 

# Example 1:

# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation: 
# All possible ways to reach at index 3 with value 0 are: 
# index 5 -> index 4 -> index 1 -> index 3 
# index 5 -> index 6 -> index 4 -> index 1 -> index 3 
# Example 2:

# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true 
# Explanation: 
# One possible way to reach at index 3 with value 0 is: 
# index 0 -> index 4 -> index 1 -> index 3
# Example 3:

# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.
 

# Constraints:

# 1 <= arr.length <= 5 * 104
# 0 <= arr[i] < arr.length
# 0 <= start < arr.length

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        visited = set()
        l = len(arr)
        while q:
            i = q.popleft()
            if i in visited:
                continue
            visited.add(i)
            forward = i + arr[i]
            if forward < l:
                if arr[forward] == 0:
                    return True
                # if forward not in visited:
                q.append(forward)
            back = i - arr[i]
            if back >= 0:
                if arr[back] == 0:
                    return True
                # if back not in visited:
                q.append(back)
        return False

# Modify the arr in place to mark the visited indices. Saves extra space
# Time complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        while q:
            i = q.popleft()
            if i < 0 or i >= len(arr) or arr[i] < 0:
                continue
            if arr[i] == 0:
                return True

            jump = arr[i]
            arr[i] = -1  # mark visited

            q.append(i + jump)
            q.append(i - jump)

        return False
