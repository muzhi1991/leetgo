# Created by muzhi1991 at 2025/01/06 11:15
# leetgo: 1.4.11
# https://leetcode.cn/problems/decode-string/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                t = ""
                n = 0
                while True:
                    v = stack.pop()
                    if v == "[":
                        nn = ""
                        while stack and "0" <= stack[-1] <= "9":
                            vv = stack.pop()
                            nn = vv + nn
                        n = int(nn)
                        # print(nn, n)
                        break
                    else:
                        t = v + t
                for _ in range(n):
                    stack.append(t)
        res += "".join(stack)
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().decodeString(s)
    print("\noutput:", serialize(ans, "string"))
