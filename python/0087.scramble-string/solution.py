# Created by muzhi1991 at 2025/02/08 10:04
# leetgo: 1.4.11
# https://leetcode.cn/problems/scramble-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    ans = Solution().isScramble(s1, s2)
    print("\noutput:", serialize(ans, "boolean"))
