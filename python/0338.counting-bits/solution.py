# Created by muzhi1991 at 2025/01/07 10:05
# leetgo: 1.4.11
# https://leetcode.cn/problems/counting-bits/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            res.append(res[i & (i - 1)] + 1)
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().countBits(n)
    print("\noutput:", serialize(ans, "integer[]"))
