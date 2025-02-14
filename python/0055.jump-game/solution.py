# Created by muzhi1991 at 2025/02/13 10:33
# leetgo: 1.4.11
# https://leetcode.cn/problems/jump-game/

from typing import *
from leetgo_py import *

# @lc code=begin


# 解题思路
# 最简单的方法就是记录可以向后跳转到的最大位置，下面的 mm（这题特殊性就是0-mm 的位置都是可以到达的）
# 还有一种更通用的思路是，可以记录区间，再合并区间（好像过于复杂了）
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # buf = [False] * len(nums)
        # 记录可以跳转的最大值
        mm = 0
        for i in range(len(nums)):
            if i <= mm:
                m = i + nums[i]
                if m >= len(nums) - 1:
                    return True
                if m > mm:
                    mm = m
        return False


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canJump(nums)
    print("\noutput:", serialize(ans, "boolean"))
