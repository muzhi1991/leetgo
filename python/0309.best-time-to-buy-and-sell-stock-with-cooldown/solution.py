# Created by muzhi1991 at 2025/01/10 09:43
# leetgo: 1.4.11
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            for j in range(0, i):
                if j >= 2:
                    p = dp[j - 2] + prices[i] - prices[j]
                else:
                    p = prices[i] - prices[j]
                dp[i] = max(dp[i], dp[j], p)
            print(i, dp)
        return dp[-1]


# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)
    print("\noutput:", serialize(ans, "integer"))
