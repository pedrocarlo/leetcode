# 210. Course Schedule II

from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        queue = deque()
        ret = []

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        # get 0 in degree nodes to add to queue
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        

        while queue:
            curr = queue.popleft()
            ret.append(curr)
            for course in adj[curr]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        
        return ret if len(ret) == numCourses else []


sol = Solution()
res = sol.findOrder(3, [[1, 0], [1, 2], [0, 1]])
print(res)
