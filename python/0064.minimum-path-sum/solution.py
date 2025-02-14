# Created by muzhi1991 at 2025/02/13 09:59
# leetgo: 1.4.11
# https://leetcode.cn/problems/minimum-path-sum/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
                # print(i, j, dp)
        return dp[-1][-1]


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minPathSum(grid)
    print("\noutput:", serialize(ans, "integer"))
