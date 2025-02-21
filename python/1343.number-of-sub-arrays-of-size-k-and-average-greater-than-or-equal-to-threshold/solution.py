# Created by muzhi1991 at 2025/02/19 10:08
# leetgo: 1.4.11
# https://leetcode.cn/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        i = 0
        j = 0
        s = 0
        while j < len(arr):
            s += arr[j]
            j += 1
            if j - i < k:
                continue
            # print(i, j, s, k)
            if s / k >= threshold:
                res += 1
            s -= arr[i]
            i += 1
        return res


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    threshold: int = deserialize("int", read_line())
    ans = Solution().numOfSubarrays(arr, k, threshold)
    print("\noutput:", serialize(ans, "integer"))
