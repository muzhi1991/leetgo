# Created by muzhi1991 at 2025/02/19 11:11
# leetgo: 1.4.11
# https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/

from typing import *
from leetgo_py import *

from collections import Counter
# @lc code=begin


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        res = 0
        cc = Counter()
        s = 0
        for i, e in enumerate(nums):
            cc[e] += 1
            s += e
            if i + 1 < k:
                continue
            # print(i, s, cc)
            if len(cc) >= m and s > res:
                res = s
            start = i - (k - 1)
            cc[nums[start]] -= 1
            s -= nums[start]
            if cc[nums[start]] == 0:
                del cc[nums[start]]
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    m: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxSum(nums, m, k)
    print("\noutput:", serialize(ans, "long"))
