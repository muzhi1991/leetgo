# Created by muzhi1991 at 2025/02/21 11:19
# leetgo: 1.4.11
# https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/

from typing import *
from leetgo_py import *

from collections import Counter
# @lc code=begin


"""
这个题目的核心是转换问题，从两侧各拿走 k 个a/b/c，等价于剩下的不定长的最长窗口包含 a/b/c 的n-2个
"""


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        mm = Counter(s)
        for n, v in mm.items():
            if v < k:
                return -1
            mm[n] -= k
        if len(mm) < 3:
            return -1
        # print(mm)
        pre = 0
        res = 0
        buf = Counter()
        for i, e in enumerate(s):
            buf[e] += 1
            while buf[e] > mm[e]:
                buf[s[pre]] -= 1
                pre += 1
                # print(pre, i)
                if pre > i:
                    break
            if i - pre + 1 > res:
                res = i - pre + 1
        return len(s) - res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().takeCharacters(s, k)
    print("\noutput:", serialize(ans, "integer"))
