# Created by muzhi1991 at 2024/12/05 01:25
# leetgo: 1.4.11
# https://leetcode.cn/problems/two-sum/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, n in enumerate(nums):
            m[n] = i
        for i, n in enumerate(nums):
            t = target - n
            if t in m and m[t] != i:
                return [i, m[t]]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().twoSum(nums, target)
    print("\noutput:", serialize(ans, "integer[]"))
