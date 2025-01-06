# Created by muzhi1991 at 2025/01/02 09:49
# leetgo: 1.4.11
# https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for e in nums:
            if e > n:
                e %= n
            nums[e - 1] += n
        res = []
        for i in range(n):
            if nums[i] <= n:
                res.append(i + 1)
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findDisappearedNumbers(nums)
    print("\noutput:", serialize(ans, "integer[]"))
