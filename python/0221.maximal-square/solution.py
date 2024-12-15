# Created by muzhi1991 at 2024/12/15 11:14
# leetgo: 1.4.11
# https://leetcode.cn/problems/maximal-square/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def dfs(self, matrix, i, j, visited):
        # print(i, j, len(matrix), len(matrix[0]), visited)
        if i >= len(matrix) or j >= len(matrix[0]):
            return
        if visited[i][j] == 1:
            return
        print(i, j, matrix[i][j])
        visited[i][j] = 1
        self.dfs(matrix, i + 1, j, visited)
        self.dfs(matrix, i, j + 1, visited)
        self.dfs(matrix, i + 1, j + 1, visited)
        return

    def func(self, matrix, i, j, buf):
        if i == 0 or j == 0:
            return 1 if matrix[i][j] == "1" else 0
        # if matrix[i][i] == "0":
        #     return 0

        if buf[i - 1][j - 1] >= 0:
            nn = buf[i - 1][j - 1]
        else:
            nn = self.func(matrix, i - 1, j - 1, buf)
            buf[i - 1][j - 1] = nn
            # print(buf[i - 1][j - 1])

        # print(i, j, nn)
        if nn == 0:
            return 1 if matrix[i][j] == "1" else 0
        n = 0
        for diff in range(min(min(i, j) + 1, nn + 1)):
            if matrix[i - diff][j] == "1" and matrix[i][j - diff] == "1":
                n += 1
            else:
                break
        return n

    def bfs(self, matrix, i, j, visited):
        from collections import deque

        queue = deque()
        queue.append(((i, j)))
        # queue = []
        # queue.append((i, j))
        while len(queue) > 0:
            a, b = queue.popleft()
            print(a, b, matrix[a][b])
            visited[a][b] = 1
            if a + 1 < len(matrix) and not visited[a + 1][b]:
                queue.append((a + 1, b))
            if b + 1 < len(matrix[0]) and not visited[a][b + 1]:
                queue.append((a, b + 1))
            if a + 1 < len(matrix) and b + 1 < len(matrix[0]) and not visited[a + 1][b + 1]:
                queue.append((a + 1, b + 1))

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # visited = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        # self.bfs(matrix, 0, 0, visited)
        buf = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        # print(buf)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                buf[i][j] = self.func(matrix, i, j, buf)
        # print(buf)
        r = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if buf[i][j] > r:
                    r = buf[i][j]
        return r * r


# @lc code=end

if __name__ == "__main__":
    matrix: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().maximalSquare(matrix)
    print("\noutput:", serialize(ans, "integer"))
