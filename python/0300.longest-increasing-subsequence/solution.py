# Created by muzhi1991 at 2025/02/18 11:08
# leetgo: 1.4.11
# https://leetcode.cn/problems/longest-increasing-subsequence/

from typing import *
from leetgo_py import *

from bisect import bisect_left
# @lc code=begin


"""
 这是一个典型例题 LIS
思路类似 435 题
区别是这里是严格大于，因此 tail 数组优化算法中用的是 bisect_left，目的是查找到等于的数组也要替换掉
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        tail = []
        for i, e in enumerate(nums):
            if i == 0:
                dp[i] = 1
                tail.append(e)
            if e > tail[-1]:
                tail.append(e)
                r = len(tail) - 1
            else:
                pos = bisect_left(tail, e)
                tail[pos] = e
                r = pos
            dp[i] = r + 1
            # print(i, dp, tail)
        return max(dp)

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     dp = [0] * len(nums)
    #     for i, e in enumerate(nums):
    #         if i == 0:
    #             dp[i] = 1
    #         else:
    #             dp[i] = max([dp[i] if nums[i] < e else 0 for i in range(i)]) + 1
    #     return max(dp)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().lengthOfLIS(nums)
    print("\noutput:", serialize(ans, "integer"))
