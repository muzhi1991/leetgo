# Created by muzhi1991 at 2024/12/14 15:53
# leetgo: 1.4.11
# https://leetcode.cn/problems/daily-temperatures/

from typing import *
from leetgo_py import *

from collections import defaultdict

# from bisect import bisect
import bisect
# @lc code=begin

"""
 看题目关键就是值的范围很小，只有 100
思路 1：建立一个 dict，key 是 值，value 是位置的 list，注意 list 是顺序递增的，遍历的时候可以直接用 bisect 查找
思路 2：单调栈：核心的想法就是不是顺心更新找到最大值，而是在过程中不断找
"""


class Solution:
    #     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #         buf = defaultdict(list)
    #         for i, t in enumerate(temperatures):
    #             buf[t].append(i)
    #         res = []
    #         # print(buf)
    #         for i, t in enumerate(temperatures):
    #             r = 1e9
    #             for j in range(t + 1, 101):
    #                 if j in buf:
    #                     ind = bisect.bisect(buf[j], i)
    #                     print(buf[j], i, ind)
    #                     if ind < len(buf[j]):
    #                         diff = buf[j][bisect.bisect(buf[j], i)] - i
    #                         print(j, diff, r)
    #                         if diff < r:
    #                             r = diff
    #                         # 不加过不了。。 会超时
    #                         if r == 1:
    #                             break
    #             if r == 1e9:
    #                 res.append(0)
    #             else:
    #                 res.append(r)
    #         return res

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, e in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < e:
                v = stack.pop()
                # print(stack, i, v)
                res[v] = i - v
            stack.append(i)
        return res


# @lc code=end

if __name__ == "__main__":
    temperatures: List[int] = deserialize("List[int]", read_line())
    ans = Solution().dailyTemperatures(temperatures)
    print("\noutput:", serialize(ans, "integer[]"))
