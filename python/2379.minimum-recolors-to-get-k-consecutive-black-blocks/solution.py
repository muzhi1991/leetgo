# Created by muzhi1991 at 2025/02/19 10:49
# leetgo: 1.4.11
# https://leetcode.cn/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = 1e9
        s = 0
        for i, e in enumerate(blocks):
            if e == "B":
                s += 1
            # i+1是当前计数的数量
            if i + 1 < k:
                continue
            if k - s < res:
                res = k - s
            s -= 1 if blocks[i - (k - 1)] == "B" else 0
        return res


# @lc code=end

if __name__ == "__main__":
    blocks: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minimumRecolors(blocks, k)
    print("\noutput:", serialize(ans, "integer"))
