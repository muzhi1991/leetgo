# Created by muzhi1991 at 2025/02/20 10:51
# leetgo: 1.4.11
# https://leetcode.cn/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = pow(2, k)
        if len(s) - k + 1 < n:
            return False
        buf = set()
        ss = 0
        for i, e in enumerate(s):
            # 结合优先级问题
            ss = (ss << 1) + int(e)
            if i + 1 < k:
                continue
            # print(i, ss)
            buf.add(ss)
            # fix移位数量的应该是 k-1
            ss = ss & ~(1 << (k - 1))
            # print(buf)
        return len(buf) == n


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().hasAllCodes(s, k)
    print("\noutput:", serialize(ans, "boolean"))
