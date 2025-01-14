# Created by muzhi1991 at 2025/01/08 09:47
# leetgo: 1.4.11
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ll = len(prices)
        m1 = [1e9]
        m2 = [0]
        for i in range(ll):
            m1.append(min(prices[i], m1[-1]))
            m2.append(max(prices[ll - i - 1], m2[-1]))
        res = 0
        for a, b in zip(m1[1:], m2[1:][::-1]):
            if b - a > res:
                res = b - a
        return res


# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)
    print("\noutput:", serialize(ans, "integer"))
