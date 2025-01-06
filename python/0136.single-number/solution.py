# Created by muzhi1991 at 2024/12/31 09:45
# leetgo: 1.4.11
# https://leetcode.cn/problems/single-number/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = 0
        for n in nums:
            s ^= n
        return s


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().singleNumber(nums)
    print("\noutput:", serialize(ans, "integer"))
