# Created by muzhi1991 at 2025/02/21 10:50
# leetgo: 1.4.11
# https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        ss = 0
        pre = 0
        for i, e in enumerate(nums):
            if nums[i] == 0:
                ss += 1
            while ss > 1:
                if nums[pre] == 0:
                    ss -= 1
                pre += 1
            # print(pre, i)
            if i - pre + 1 > res:
                res = i - pre + 1
        return res - 1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestSubarray(nums)
    print("\noutput:", serialize(ans, "integer"))
