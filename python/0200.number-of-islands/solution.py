# Created by muzhi1991 at 2024/12/20 11:16
# leetgo: 1.4.11
# https://leetcode.cn/problems/number-of-islands/

from typing import *
from leetgo_py import *
from collections import defaultdict

# @lc code=begin


class Solution:
    def dfs(self, grid, i, j, visited):
        if visited[i][j] or grid[i][j] != "1":
            return

        visited[i][j] = 1
        height = len(grid)
        width = len(grid[0])
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for x, y in direction:
            a = i + x
            b = j + y
            if a >= 0 and b >= 0 and a < height and b < width:
                self.dfs(grid, a, b, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        width = len(grid[0])
        height = len(grid)
        visited = [[0] * width for _ in range(height)]
        r = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "1" and not visited[i][j]:
                    r += 1
                    self.dfs(grid, i, j, visited)
                    # print(visited)

        return r


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    grid: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().numIslands(grid)
    print("\noutput:", serialize(ans, "integer"))
