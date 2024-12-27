# Created by muzhi1991 at 2024/12/23 09:44
# leetgo: 1.4.11
# https://leetcode.cn/problems/house-robber/

from typing import *
from leetgo_py import *

# @lc code=begin


"""
核心想法：间隔的房间的可能性只有两种，一个是间隔 1 个，一个是间隔 2 个( 间隔两个的目的是放弃一些太小的)，不可能是 3 个，因为如果是 3，那么中间比如可以插入一个
因此，这里可以使用 dp，之所以想到 dp 是和状态有关，list 的每个元素当前的状态n由之前的n-2 n-3状态确定（状态这里指的是如果选择这个房间，那么他之前的最大值是什么）
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        if len(nums) == 3:
            a = nums[0] + nums[2]
            if a > nums[1]:
                return a
            else:
                return nums[1]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if i == 1:
                dp[i] = nums[i]
            if i == 2:
                dp[i] = dp[i - 2] + nums[i]
            if i >= 3:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 3] + nums[i])
            # print(i, dp[i])

        return max(dp)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().rob(nums)
    print("\noutput:", serialize(ans, "integer"))
