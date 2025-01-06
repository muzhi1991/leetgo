# Created by muzhi1991 at 2024/12/31 10:02
# leetgo: 1.4.11
# https://leetcode.cn/problems/palindromic-substrings/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = {}
        for span in range(len(s)):
            for i in range(span, len(s)):
                if span == 0:
                    dp[i] = {i}
                    continue
                a = i - span
                b = i
                if b - a == 1 and s[a] == s[b]:
                    dp[i].add(a)
                if b - a > 1 and s[a] == s[b] and (a + 1 in dp[b - 1]):
                    dp[i].add(a)
        res = 0
        for k, v in dp.items():
            res += len(v)
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().countSubstrings(s)
    print("\noutput:", serialize(ans, "integer"))
