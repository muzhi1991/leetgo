# Created by muzhi1991 at 2025/02/21 11:07
# leetgo: 1.4.11
# https://leetcode.cn/problems/find-the-longest-semi-repetitive-substring/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        res = 0
        ss = 0
        pre = 0
        for i, e in enumerate(s):
            if i == 0:
                res = 1
                continue
            if s[i - 1] == e:
                ss += 1
            while ss > 1:
                if s[pre] == s[pre + 1]:
                    ss -= 1
                pre += 1
            if i - pre + 1 > res:
                res = i - pre + 1
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().longestSemiRepetitiveSubstring(s)
    print("\noutput:", serialize(ans, "integer"))
