# Created by muzhi1991 at 2025/02/07 10:07
# leetgo: 1.4.11
# https://leetcode.cn/problems/maximal-rectangle/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxRec(self, buf):
        res = 0
        tmp = [0] * len(buf)
        stack = []
        for i in reversed(range(len(buf))):
            while stack and buf[stack[-1]] >= buf[i]:
                stack.pop()
            pos = stack[-1] if stack else len(buf)
            # print(pos, i, pos - i - 1)
            tmp[i] = pos - i - 1
            stack.append(i)
        # print("tmp", tmp)
        stack = []
        for i in range(len(buf)):
            while stack and buf[stack[-1]] >= buf[i]:
                stack.pop()
            pos = stack[-1] if stack else -1
            v = (i - pos - 1 + tmp[i] + 1) * buf[i]
            if v > res:
                res = v
            stack.append(i)
        return res

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        buf = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        # buf2 = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0:
                    buf[i][j] = 1 if matrix[i][j] == "1" else 0
                else:
                    buf[i][j] = (buf[i][j - 1] + 1) if matrix[i][j] == "1" else 0
                # if i == 0:
                #     buf2[i][j] = 1 if matrix[i][j] == "1" else 0
                # else:
                #     buf2[i][j] = (buf2[i - 1][j] + 1) if matrix[i][j] == "1" else 0
        # print(buf)
        # print(buf2)
        res = 0
        # for e in buf:
        #     r = self.maxRec((e))
        #     print(e, r)
        #     if r > res:
        #         res = r
        for j in range(len(buf[0])):
            b = []
            for i in range(len(buf)):
                b.append(buf[i][j])
            r = self.maxRec(b)
            # print(b, r)
            if r > res:
                res = r
        return res


# @lc code=end

if __name__ == "__main__":
    matrix: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().maximalRectangle(matrix)
    print("\noutput:", serialize(ans, "integer"))
