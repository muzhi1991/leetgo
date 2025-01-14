# Created by muzhi1991 at 2025/01/07 09:49
# leetgo: 1.4.11
# https://leetcode.cn/problems/top-k-frequent-elements/

from typing import *
from leetgo_py import *

import heapq
# @lc code=begin


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cc = 0
        pre = None
        res = []

        nums.sort()
        # print(nums)
        for n in nums:
            if n != pre:
                res.append((pre, cc))
                cc = 0
            cc += 1
            pre = n
        if cc != 0:
            res.append((nums[-1], cc))
        return [a for a, b in sorted(res, key=lambda k: k[1], reverse=True)[:k]]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().topKFrequent(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
