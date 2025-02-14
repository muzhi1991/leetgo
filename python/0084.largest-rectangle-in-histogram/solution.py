# Created by muzhi1991 at 2025/02/06 10:34
# leetgo: 1.4.11
# https://leetcode.cn/problems/largest-rectangle-in-histogram/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
# @lc code=begin


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        buf = [0] * len(heights)
        for i in reversed(range(len(heights))):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            pos = stack[-1] if stack else len(heights)
            buf[i] = pos - i - 1
            stack.append(i)

        res = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            pos = stack[-1] if stack else -1
            ll = i - pos - 1 + buf[i] + 1
            v = ll * heights[i]
            # print(i - pos - 1, buf[i], pos, v)
            if v > res:
                res = v
            stack.append(i)
        return res

    # def largestRectangleArea(self, heights: List[int]) -> int:

    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     stack = []
    #     res = 0
    #     prej = -1
    #     for i, h in enumerate(heights):
    #         while stack and heights[stack[-1]] >= h:
    #             stack.pop()
    #         stack.append(i)
    #
    #         if 0 <= prej < len(stack) - 1:
    #             res += heights[stack[prej]]
    #         else:
    #             prej = -1
    #
    #         print(i, prej, len(stack), stack, res)
    #         for j in range(max(prej, 0), len(stack)):
    #             e = stack[j]
    #             start = stack[j - 1] if j > 0 else -1
    #             r = heights[e] * (i - start)
    #             if r > res:
    #                 res = r
    #                 prej = j
    #
    #         # j = 0
    #         # while j <= i:
    #         #     pos = bisect_left(stack, j)
    #         #     v = stack[pos]
    #         #     # print(j, i, v)
    #         #     # print(heights[v])
    #         #     r = heights[v] * (i - j + 1)
    #         #     if r > res:
    #         #         res = r
    #         #     j = v + 1
    #     return res


# @lc code=end

if __name__ == "__main__":
    heights: List[int] = deserialize("List[int]", read_line())
    ans = Solution().largestRectangleArea(heights)
    print("\noutput:", serialize(ans, "integer"))
