# Created by muzhi1991 at 2025/02/08 10:04
# leetgo: 1.4.11
# https://leetcode.cn/problems/subsets/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        i = 0
        while i <= pow(2, len(nums)) - 1:
            r = []
            t = i
            c = 0
            while t > 0:
                # print(t)
                if t & 1 > 0:
                    r.append(nums[c])
                t = t >> 1
                c += 1
            res.append(r)
            i += 1
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().subsets(nums)
    print("\noutput:", serialize(ans, "integer[][]"))
