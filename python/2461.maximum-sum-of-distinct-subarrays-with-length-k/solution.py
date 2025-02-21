# Created by muzhi1991 at 2025/02/20 09:59
# leetgo: 1.4.11
# https://leetcode.cn/problems/maximum-sum-of-distinct-subarrays-with-length-k/

from typing import *
from leetgo_py import *

from collections import Counter
# @lc code=begin


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        s = 0
        buf = dict()
        left = 0
        for i, e in enumerate(nums):
            # fix 判断条件还要满足 left 指针的位置
            if e in buf and left <= buf[e]:
                for j in range(left, buf[e] + 1):
                    s -= nums[j]
                left = buf[e] + 1
            elif i - left > k - 1:
                for j in range(left, i - k + 1):
                    s -= nums[j]
                left = i - k + 1
            buf[e] = i
            s += e
            # print(left, i, s)
            if s > res and i - left == k - 1:
                res = s
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumSubarraySum(nums, k)
    print("\noutput:", serialize(ans, "long"))
