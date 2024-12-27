# Created by muzhi1991 at 2024/12/19 15:30
# leetgo: 1.4.11
# https://leetcode.cn/problems/course-schedule/

from typing import *
from leetgo_py import *

from collections import defaultdict
# @lc code=begin

"""
主要是思想是查找有向图的循环节点，如果存在就不能完成
这里主要是两个做法，
* 递归 dfs： 关键点是维护一个 visited 字典，里面的含义是节点是不是正在被访问 -1（不能被再次访问），节点是不是已经访问完成（可以被再次方法）1，不存在-没有被访问过。通过在递归函数前后设置不同的值实现功能
* 栈 dfs：其实就是 dfs 的另外一个实现，但是需要注意的是记录入栈和出栈（模拟上面的 dfs 函数的访问前后的情况）而不是直接 pop 就丢掉
"""


class Solution:
    def dfs(self, graph, root, visited):
        if root in visited and visited[root] == -1:
            # print(root)
            return False
        if root in visited and visited[root] == 1:
            # visited[root] = -1
            return True
        if root not in visited:
            visited[root] = -1
        for n in graph[root]:
            r = self.dfs(graph, n, visited)
            visited[n] = 1
            if r is False:
                # print(root, "-->", n)
                return r
        return True

    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     if not prerequisites:
    #         return True
    #     buf = defaultdict(list)
    #     s = set()
    #     for a, b in prerequisites:
    #         buf[b].append(a)
    #         s.add(a)
    #
    #     roots = [r for r in list(buf.keys())]
    #     if not roots:
    #         return False
    #
    #     visited = {}
    #     for k in roots:
    #         # print(k, buf[k])
    #         r = self.dfs(buf, k, visited)
    #         if r is False:
    #             return False
    #         visited[k] = 1
    #     return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        visited = {}
        for n in list(graph.keys()):
            if n in visited and visited[n] == 1:
                continue
            stack = [(n, "enter")]
            while stack:
                cur, action = stack.pop()
                # print(cur, action)
                if action == "enter":
                    visited[cur] = -1
                    stack.append((cur, "pop"))
                    for next in graph[cur]:
                        if next in visited and visited[next] == -1:
                            return False
                        if next in visited and visited[next] == 1:
                            continue
                        stack.append((next, "enter"))
                if action == "pop":
                    visited[cur] = 1
        return True


# @lc code=end

if __name__ == "__main__":
    numCourses: int = deserialize("int", read_line())
    prerequisites: List[List[int]] = deserialize("List[List[int]]", read_line())
    # numCourses = 2
    # prerequisites = [[1, 0]]
    ans = Solution().canFinish(numCourses, prerequisites)
    print("\noutput:", serialize(ans, "boolean"))
