# Created by muzhi1991 at 2025/01/01 10:29
# leetgo: 1.4.11
# https://leetcode.cn/problems/hamming-distance/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        res = 0
        while z > 0:
            if z % 2 == 1:
                res += 1
            z = z // 2
        return res


# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    y: int = deserialize("int", read_line())
    ans = Solution().hammingDistance(x, y)
    print("\noutput:", serialize(ans, "integer"))
