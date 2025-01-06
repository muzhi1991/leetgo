# Created by muzhi1991 at 2024/12/31 10:23
# leetgo: 1.4.11
# https://leetcode.cn/problems/longest-consecutive-sequence/

from typing import *
from leetgo_py import *
import heapq

# @lc code=begin


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heapq.heapify((nums))
        n = len(nums)
        res = 0
        pre = None
        cc = 0
        while n > 0:
            v = heapq.heappop(nums)
            if pre is None:
                pre = v
                cc = 1
            else:
                if v - pre == 1:
                    cc += 1
                elif v - pre == 0:
                    pass
                else:
                    cc = 1
                pre = v
            if cc > res:
                res = cc
            n -= 1
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestConsecutive(nums)
    print("\noutput:", serialize(ans, "integer"))
