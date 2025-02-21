# Created by muzhi1991 at 2025/02/20 10:30
# leetgo: 1.4.11
# https://leetcode.cn/problems/defuse-the-bomb/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = []
        if k < 0:
            s = sum(code[k:])
            res.append(s)
            for i in range(len(code) - 1):
                s -= code[i + k]
                s += code[i]
                res.append(s)
        elif k == 0:
            res = [0] * len(code)
        else:
            s = sum(code[1 : k + 1])
            res.append(s)
            for i in range(1, len(code)):
                s -= code[i]
                s += code[(i + k) % len(code)]
                res.append(s)
        return res


# @lc code=end

if __name__ == "__main__":
    code: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().decrypt(code, k)
    print("\noutput:", serialize(ans, "integer[]"))
