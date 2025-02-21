# Created by muzhi1991 at 2025/02/20 11:11
# leetgo: 1.4.11
# https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# 这题目的难点是把这个问题转为滑动窗口问题，本质上就是求一个窗口内的 1 的数量


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = sum(nums)
        r = 0
        s = 0
        for i in range(len(nums) + n - 1):
            e = nums[i % len(nums)]
            s += e
            if i + 1 < n:
                continue
            if s > r:
                r = s
            s -= nums[i % len(nums) - (n - 1)]
        return n - r


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minSwaps(nums)
    print("\noutput:", serialize(ans, "integer"))
