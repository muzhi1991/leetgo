# Created by muzhi1991 at 2025/02/14 11:31
# leetgo: 1.4.11
# https://leetcode.cn/problems/maximum-average-subarray-i/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, j = 0, 0
        res = -1e9
        s = 0
        while j < len(nums):
            while j < len(nums) and j - i < k:
                s += nums[j]
                j += 1
            # print(i, j, s)
            v = s / k
            if v > res:
                res = v
            s -= nums[i]
            i += 1
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findMaxAverage(nums, k)
    print("\noutput:", serialize(ans, "double"))
