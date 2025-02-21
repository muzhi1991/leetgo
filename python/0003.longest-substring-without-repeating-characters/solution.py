# Created by muzhi1991 at 2025/02/21 10:24
# leetgo: 1.4.11
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        buf = dict()
        pre = -1
        for i, e in enumerate(s):
            # fix 第二次犯这个错，需要判断前置的位置，来移动 pre，不能所有情况都移动
            if e in buf and buf[e] > pre:
                pre = buf[e]
            # print(i, pre)
            if i - pre > res:
                res = i - pre
            buf[e] = i
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().lengthOfLongestSubstring(s)
    print("\noutput:", serialize(ans, "integer"))
