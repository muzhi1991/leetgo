# Created by muzhi1991 at 2025/01/10 14:04
# leetgo: 1.4.11
# https://leetcode.cn/problems/generate-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def gen(self, l1, l2, s):
        # print(l1, l2, s)
        if l1 == 0 and l2 == 0:
            return [s]
        res = []
        if l1 > 0:
            r = self.gen(l1 - 1, l2, s + "(")
            if r:
                res.extend(r)
        if l1 < l2 and l2 > 0:  ## here
            r = self.gen(l1, l2 - 1, s + ")")
            if r:
                res.extend(r)
        return res

    def generateParenthesis(self, n: int) -> List[str]:
        return self.gen(n, n, "")


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().generateParenthesis(n)
    print("\noutput:", serialize(ans, "string[]"))
