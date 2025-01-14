# Created by muzhi1991 at 2025/01/01 09:53
# leetgo: 1.4.11
# https://leetcode.cn/problems/target-sum/

from typing import *
from leetgo_py import *

from collections import defaultdict
# @lc code=begin


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            if target == 0:
                return 1
            else:
                return 0
        dp = [defaultdict(lambda: 0) for _ in range(len(nums))]
        for i in range(len(nums)):
            n = nums[i]
            if i == 0:
                dp[i][n] += 1
                dp[i][-n] += 1
                # print(i, dp[i])
                continue
            for k, v in list(dp[i - 1].items()):
                dp[i][k + n] += v
                dp[i][k - n] += v
            # print(i, dp[i])
        return dp[len(nums) - 1][target]

        a = self.findTargetSumWays(nums[:-1], target - nums[-1])
        b = self.findTargetSumWays(nums[:-1], target + nums[-1])
        return a + b


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().findTargetSumWays(nums, target)
    print("\noutput:", serialize(ans, "integer"))
