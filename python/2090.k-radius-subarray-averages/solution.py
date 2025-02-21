# Created by muzhi1991 at 2025/02/19 10:30
# leetgo: 1.4.11
# https://leetcode.cn/problems/k-radius-subarray-averages/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        s = 0
        for i, e in enumerate(nums):
            s += e
            if i < k * 2:
                continue
            res.append(int(s / (k * 2 + 1)))
            s -= nums[i - k * 2]
        if len(nums) - (2 * k + 1) >= 0:
            res = [-1] * k + res + [-1] * k
        else:
            res = [-1] * len(nums)
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().getAverages(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
