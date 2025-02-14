# Created by muzhi1991 at 2025/02/13 10:23
# leetgo: 1.4.11
# https://leetcode.cn/problems/merge-intervals/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda e: e[0])
        res = [intervals[0]]
        # print(intervals)
        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                pre = res.pop()
                # merge
                # print(pre)
                #  错误：第二个元素注意要处理好，选择最大值
                res.append([pre[0], max(pre[1], intervals[i][1])])
            else:
                res.append(intervals[i])
            # print(res)
        return res


# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().merge(intervals)
    print("\noutput:", serialize(ans, "integer[][]"))
