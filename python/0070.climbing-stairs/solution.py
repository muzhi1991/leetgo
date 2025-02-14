# Created by muzhi1991 at 2025/02/12 10:30
# leetgo: 1.4.11
# https://leetcode.cn/problems/climbing-stairs/

from typing import *
from leetgo_py import *

# @lc code=begin

buf = {}


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    # def climbStairs(self, n: int) -> int:
    #     """
    #     解法一：记忆化搜索
    #     """
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #     if n == 3:
    #         return 3
    #     if n in buf:
    #         return buf[n]
    #     r = 1 * self.climbStairs(n - 1) + self.climbStairs(n - 2)
    #     buf[n] = r
    #     return r


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().climbStairs(n)
    print("\noutput:", serialize(ans, "integer"))
