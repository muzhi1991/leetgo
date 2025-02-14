# Created by muzhi1991 at 2025/02/11 09:55
# leetgo: 1.4.11
# https://leetcode.cn/problems/sort-colors/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p1, p2 = 0, 0, len(nums) - 1
        while True:
            while p0 < len(nums) and nums[p0] == 0:
                p0 += 1
            while p2 >= 0 and nums[p2] == 2:
                p2 -= 1

            if p0 >= p2:
                break
            # 1 0 0
            # 1 0 1
            # 2 0 0
            # 2 0 1
            if nums[p0] == 1 and nums[p2] == 1:
                if p1 <= p0:
                    p1 = p0 + 1
                while p1 < len(nums) and nums[p1] == 1:
                    p1 += 1
                if p1 >= p2:
                    break
                if nums[p1] == 0:
                    nums[p0], nums[p1] = nums[p1], nums[p0]
                if nums[p1] == 2:
                    nums[p2], nums[p1] = nums[p1], nums[p2]

            else:
                # 这里有几种情况，不管什么情况交换后都是可以的
                nums[p0], nums[p2] = nums[p2], nums[p0]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    Solution().sortColors(nums)
    ans = nums
    print("\noutput:", serialize(ans, "List[int]"))
