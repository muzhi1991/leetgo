# Created by muzhi1991 at 2024/12/24 11:04
# leetgo: 1.4.11
# https://leetcode.cn/problems/maximum-product-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def f(self, nums, start, end):
        res = -1e9
        cc = 1
        min_pos = 1
        max_neg = -1e9
        for i in range(start, end + 1):
            if cc < 0 and cc > max_neg:
                max_neg = cc
            cc *= nums[i]
            if cc > 0 and cc < min_pos:
                min_pos = cc
            if cc > 0:
                r = cc // min_pos
            else:
                if max_neg == -1e9:
                    r = cc
                else:
                    r = cc // max_neg
            if r > res:
                res = r
        return res

        pass

    def maxProduct(self, nums: List[int]) -> int:
        res = -1e9
        pre = -1
        for i in range(len(nums)):
            if res < 0 and nums[i] == 0:
                res = 0
            if nums[i] == 0:
                if i - pre > 1:
                    r = self.f(nums, pre + 1, i - 1)
                    if r > res:
                        res = r
                pre = i
            elif i == len(nums) - 1:
                r = self.f(nums, pre + 1, i)
                if r > res:
                    res = r
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProduct(nums)
    print("\noutput:", serialize(ans, "integer"))
