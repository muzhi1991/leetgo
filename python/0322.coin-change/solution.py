# Created by muzhi1991 at 2025/01/01 09:22
# leetgo: 1.4.11
# https://leetcode.cn/problems/coin-change/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            rr = []
            for c in coins:
                if i - c >= 0 and dp[i - c] >= 0:
                    rr.append(dp[i - c] + 1)
            if rr:
                # print(i, c, min(rr), dp)
                dp[i] = min(rr)
        return dp[amount]


# @lc code=end

if __name__ == "__main__":
    coins: List[int] = deserialize("List[int]", read_line())
    amount: int = deserialize("int", read_line())
    ans = Solution().coinChange(coins, amount)
    print("\noutput:", serialize(ans, "integer"))
