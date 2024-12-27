# Created by muzhi1991 at 2024/12/25 09:57
# leetgo: 1.4.11
# https://leetcode.cn/problems/maximum-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        res = -1e9

        # res = max(self.maxSubArray(nums[:-1]) + nums[-1], nums[-1])
        for i, e in enumerate(nums):
            if i == 0:
                dp[i] = e
            else:
                dp[i] = max(dp[i - 1] + e, e)
            if dp[i] > res:
                res = dp[i]
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSubArray(nums)
    print("\noutput:", serialize(ans, "integer"))
