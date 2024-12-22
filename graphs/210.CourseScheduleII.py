# 210. Course Schedule II
# Medium

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.


# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]


# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.

# Learn Kahn's Algorithm and its implementation
# Time Complexity: O(V+E)
# Space Complexity: O(V)


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not numCourses:
            return []
        if not prerequisites:
            return [i for i in range(numCourses)]
        indegree = [0]*numCourses
        adjList = {each:[] for each in range(numCourses)}
        for each in prerequisites:
            adjList[each[1]] = adjList.get(each[1], [])
            adjList[each[1]].append(each[0])
            indegree[each[0]] += 1
        result = []
        q = []
        for course, prereq in enumerate(indegree):
            if prereq == 0:
                q.append(course)
        number_of_completed_courses = 0
        while q:
            course = q.pop(0)
            result.append(course)
            number_of_completed_courses += 1
            for adv_course in adjList[course]:
                indegree[adv_course] -= 1
                if indegree[adv_course] == 0:
                    q.append(adv_course)
        if number_of_completed_courses != numCourses:
            return []
        return result

# Same approach

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
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
        print("zero pre req courses", zeroPreReqCourses)

        if not zeroPreReqCourses:
            #cycle is present
            return []

        q = []
        while zeroPreReqCourses:
            course = zeroPreReqCourses.pop(0)
            q.append(course)
            depCourses = aList[course] if course in aList else []
            for dep in depCourses:
                nPrereq[dep] -= 1
                if nPrereq[dep] == 0:
                    zeroPreReqCourses.append(dep)

        if any(nPrereq):
            return []
        return q
