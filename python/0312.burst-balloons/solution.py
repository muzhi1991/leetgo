# Created by muzhi1991 at 2025/01/08 09:55
# leetgo: 1.4.11
# https://leetcode.cn/problems/burst-balloons/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def f(self, nums: List[int], level) -> int:
        print(level, len(nums))
        ll = len(nums)
        if not nums:
            return 0
        if ll == 1:
            return nums[0]
        if ll == 2:
            return nums[0] * nums[1] + max(nums[0], nums[1])
        if ll == 3:
            v1 = nums[0] * nums[1] * nums[2] + self.f([nums[0], nums[2]], level + 1)
            v2 = nums[0] * nums[1] + self.f([nums[1], nums[2]], level + 1)
            v3 = nums[1] * nums[2] + self.f([nums[0], nums[1]], level + 1)
            return max(v1, v2, v3)
        res = []
        for i, n in enumerate(nums):
            # print(len(nums[:i]), len(nums[i + 1 :]))
            print("iter", level,len(nums), i)
            r = self.f(nums[:i] + nums[i + 1 :], level + 1)
            if i == 0:
                r += nums[0] * nums[1]
            elif i == ll - 1:
                r += nums[-1] * nums[-2]
            else:
                r += nums[i - 1] * nums[i] * nums[i + 1]
            # print(i, r)
            res.append(r)
        # print(max(res))
        return max(res)

    def maxCoins(self, nums: List[int]) -> int:
        return self.f(nums, 0)


# @lc code=end

if __name__ == "__main__":
    # nums: List[int] = deserialize("List[int]", read_line())
    line = "[7,9,8,0,7,1,3,5,5,2,3,3]"
    nums: List[int] = deserialize("List[int]", line)

    ans = Solution().maxCoins(nums)
    print("\noutput:", serialize(ans, "integer"))
