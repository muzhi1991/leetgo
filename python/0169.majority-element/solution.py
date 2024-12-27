# Created by muzhi1991 at 2024/12/23 10:51
# leetgo: 1.4.11
# https://leetcode.cn/problems/majority-element/

from typing import *
from leetgo_py import *

# @lc code=begin

"""
要实现空间O(1)还是需要点技巧的：
核心还是从众数的概念出发，也就是他比其他的数字都要多
技巧是一个动态的计数器，这个计数器对应的 num，是会改变的，永远对应着可以是得 cnt 大于 0 的那个
"""


class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     r = 0
    #     c = 0
    #     m = {}
    #     for n in nums:
    #         if n not in m:
    #             m[n] = 1
    #         else:
    #             m[n] += 1
    #         if m[n] > c:
    #             c = m[n]
    #             r = n
    #     return r
    def majorityElement(self, nums: List[int]) -> int:
        cur = 0
        cnt = 0
        for n in nums:
            if cur == 0 or cnt == 0:
                cur = n
                cnt = 1
                continue
            if n == cur:
                cnt += 1
            else:
                cnt -= 1
        return cur


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().majorityElement(nums)
    print("\noutput:", serialize(ans, "integer"))
