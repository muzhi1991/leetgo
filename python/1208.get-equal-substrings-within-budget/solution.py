# Created by muzhi1991 at 2025/02/21 10:59
# leetgo: 1.4.11
# https://leetcode.cn/problems/get-equal-substrings-within-budget/

from typing import *
from leetgo_py import *

# @lc code=begin


# 子串是 连续的核心
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        nums = [abs(ord(a) - ord(b)) for a, b in zip(s, t)]
        pre = 0
        ss = 0
        res = 0
        for i, e in enumerate(nums):
            ss += e
            while ss > maxCost:
                ss -= nums[pre]
                pre += 1
            if i - pre + 1 > res:
                res = i - pre + 1
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    maxCost: int = deserialize("int", read_line())
    ans = Solution().equalSubstring(s, t, maxCost)
    print("\noutput:", serialize(ans, "integer"))
