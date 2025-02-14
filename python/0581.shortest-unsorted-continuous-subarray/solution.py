# Created by muzhi1991 at 2025/02/12 11:00
# leetgo: 1.4.11
# https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin

"""
思路：使用两次单调栈分别找区间的两端
"""


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        start = len(nums)
        res = 0
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] > n:
                stack.pop()
                if len(stack) < start:
                    start = len(stack)
            stack.append(i)

        stack = []
        end = len(nums)
        for i, n in reversed(list(enumerate(nums))):
            while stack and nums[stack[-1]] < n:
                stack.pop()
                if len(stack) < end:
                    end = len(stack)
            stack.append(i)
        end = len(nums) - 1 - end

        if start >= end:
            return 0
        return end - start + 1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findUnsortedSubarray(nums)
    print("\noutput:", serialize(ans, "integer"))
