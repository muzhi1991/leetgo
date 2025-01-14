# Created by muzhi1991 at 2025/01/10 10:25
# leetgo: 1.4.11
# https://leetcode.cn/problems/remove-invalid-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def f(self, s):
        res = []
        stack = []
        for i, c in enumerate(s):
            if c != ")":
                stack.append(i)
            else:
                if not stack:
                    stack.append(i)
                else:
                    while s[stack[-1]] != "(" and s[stack[-1]] != ")":
                        v = stack.pop()
                        if not stack:
                            break
                    if stack and s[stack[-1]] == "(":
                        stack.pop()
        ss = set(stack)
        res.append("".join([c for i, c in enumerate(s) if i not in ss]))

        stack = []
        for i in range(len(s)):
            ii = len(s) - i - 1
            c = s[ii]
            if c != "(":
                stack.append(ii)
            else:
                if not stack:
                    stack.append(ii)
                else:
                    while s[stack[-1]] != "(" and s[stack[-1]] != ")":
                        v = stack.pop()
                        if not stack:
                            break
                    if stack and s[stack[-1]] == ")":
                        stack.pop()
        res.append("".join([c for i, c in enumerate(s) if i not in ss]))
        return res

    def removeInvalidParentheses(self, s: str) -> List[str]:
        return self.f(s)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().removeInvalidParentheses(s)
    print("\noutput:", serialize(ans, "string[]"))
