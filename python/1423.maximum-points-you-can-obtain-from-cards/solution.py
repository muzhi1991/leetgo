# Created by muzhi1991 at 2025/02/20 10:22
# leetgo: 1.4.11
# https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # fix 特殊情况，全部拿卡
        if len(cardPoints) == k:
            return sum(cardPoints)
        res = 1e9
        m = len(cardPoints) - k
        s = 0
        for i, e in enumerate(cardPoints):
            s += e
            if i + 1 < m:
                continue
            if s < res:
                res = s

            s -= cardPoints[i - (m - 1)]
        return sum(cardPoints) - res


# @lc code=end

if __name__ == "__main__":
    cardPoints: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxScore(cardPoints, k)
    print("\noutput:", serialize(ans, "integer"))
