# 207. Course Schedule
# Medium

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.


# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.

# reference: https://www.interviewkickstart.com/problems/course-schedule-ii


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Forming adjacency list and simultaneously calculating the number of prerequistes for each course
        nPrereq = [0 for i in range(numCourses)]
        aList = {}
        for each in prerequisites:
            if each[1] in aList:
                aList[each[1]].append(each[0])
            else:
                aList[each[1]] = [each[0]]
            nPrereq[each[0]] += 1

        zeroPreReqCourses = [course for course in range(
            numCourses) if nPrereq[course] == 0]

        if not zeroPreReqCourses:
            #cycle is present
            return False

        while zeroPreReqCourses:
            course = zeroPreReqCourses.pop(0)
            depCourses = aList[course] if course in aList else []
            print(course, depCourses)
            for dep in depCourses:
                nPrereq[dep] -= 1
                if nPrereq[dep] == 0:
                    zeroPreReqCourses.append(dep)

        if any(nPrereq):
            return False
        return True
