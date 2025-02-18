# Created by muzhi1991 at 2025/02/14 11:11
# leetgo: 1.4.11
# https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        m = {"a", "e", "i", "o", "u"}
        i, j = 0, 0
        res = 0
        t = 0
        while j < len(s):
            while j < len(s) and j - i < k:
                if s[j] in m:
                    t += 1
                # print(i, j, t)
                j += 1
            if t > res:
                res = t
            if s[i] in m:
                t -= 1
            i += 1
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxVowels(s, k)
    print("\noutput:", serialize(ans, "integer"))
