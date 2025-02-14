# Created by muzhi1991 at 2025/02/12 09:48
# leetgo: 1.4.11
# https://leetcode.cn/problems/edit-distance/

from typing import *
from leetgo_py import *

# @lc code=begin

"""
我使用记忆法来递归暴力求解的
应该可以用动态规划
"""

buf = {}


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0
        if word1 == word2:
            return 0
        if (word1, word2) in buf:
            return buf[(word1, word2)]

        res = max(len(word1), len(word2))
        if not word1 or not word2:
            return res
        m1, m2 = (word1, word2)
        # del
        r = self.minDistance(m1[1:], m2) + 1
        if r < res:
            res = r
        # insert
        r = self.minDistance(m1, m2[1:]) + 1
        if r < res:
            res = r
        if m1[0] == m2[0]:
            # not change
            r = self.minDistance(m1[1:], m2[1:])
            if r < res:
                res = r
        else:
            # replace
            r = self.minDistance(m1[1:], m2[1:]) + 1
            if r < res:
                res = r
        buf[(word1, word2)] = res
        return res


# @lc code=end

if __name__ == "__main__":
    word1: str = deserialize("str", read_line())
    word2: str = deserialize("str", read_line())
    ans = Solution().minDistance(word1, word2)
    print("\noutput:", serialize(ans, "integer"))
