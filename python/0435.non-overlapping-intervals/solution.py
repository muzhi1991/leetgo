# Created by muzhi1991 at 2025/02/17 10:15
# leetgo: 1.4.11
# https://leetcode.cn/problems/non-overlapping-intervals/

from typing import *
from leetgo_py import *
from bisect import bisect_right

# @lc code=begin


"""
思路：
本题有两个思路
1. dp：定义状态是“以 i 位置区间结尾的最大不重叠数量”（区分：包含 i 的不重叠区间数量），即没有区间和 i 重叠! 还有一个要点是使用 tail 数组(表示长度为 pos+1 的最小 right 值)结合二分查找优化查询

2. 这个思路最简单，就是先对右端点排序，此时我们只要“贪心”选择满足不重叠要求的左端点区间就行
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 按照右侧端点排序
        intervals.sort(key=lambda e: e[1])
        buf = []

        for i, e in enumerate(intervals):
            if i == 0:
                buf.append(e)
            else:
                # 左侧端点是否满足条件可以放入
                if e[0] >= buf[-1][1]:
                    buf.append(e)
        # print(buf)
        return len(intervals) - len(buf)

    # def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    #     intervals.sort(key=lambda e: e[0])
    #     dp = [0] * len(intervals)
    #     tail = []
    #     for i, e in enumerate(intervals):
    #         if i == 0:
    #             dp[0] = 1
    #             tail.append((e[1]))
    #         else:
    #             r = 0
    #             left = intervals[i][0]
    #             right = intervals[i][1]
    #             # print(tail[-1], left)
    #             if tail[-1] <= left:
    #                 tail.append(right)
    #                 r = len(tail) - 1
    #             else:
    #                 # pos表示 k==pos+1 位置的最右端点
    #                 # fix: 使用 bisect_right而不是 bisect_left: 原因是要找到比他严格大的（等于的时候要找下一个位置）
    #                 pos = bisect_right(tail, left)
    #                 # fix: 这里注意，查询的是左端点，写入的是右端点，判断右端点是不是比他小，再放入，表示“最小”范围
    #                 if right < tail[pos]:
    #                     tail[pos] = right
    #                 r = pos
    #
    #             # for j in range(i):
    #             #     if intervals[j][1] <= intervals[i][0] and dp[j] > r:
    #             #         r = dp[j]
    #             dp[i] = r + 1
    #         # print(i, dp, tail)
    #     return len(intervals) - max(dp)
    #


# def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#     intervals.sort(key=lambda e: e[0])
#     print(intervals)
#     dp = {}
#     dp[0] = (1, intervals[0][1])
#     for i in range(1, len(intervals)):
#         tmp = None
#         for j in range(0, i):
#             if dp[j][1] <= intervals[i][0]:
#                 # 可以+1的区间数量
#                 if tmp == None or dp[j][0] + 1 > tmp[0]:
#                     tmp = (dp[j][0] + 1, intervals[i][1])
#             else:
#                 # 保持原来的区间数量
#                 if tmp == None or (dp[j][0] > tmp[0]):
#                     tmp = (dp[j][0], min(intervals[i][1], dp[j][1]))
#                 elif dp[j][0] == tmp[0] and dp[j][1] < tmp[1]:
#                     tmp = (dp[j][0], min(intervals[i][1], dp[j][1]))
#         if tmp:
#             dp[i] = tmp
#         # print(i, dp)
#
#     return len(intervals) - dp[len(intervals) - 1][0]


# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().eraseOverlapIntervals(intervals)
    print("\noutput:", serialize(ans, "integer"))
