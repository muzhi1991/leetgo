# Created by muzhi1991 at 2025/02/19 11:00
# leetgo: 1.4.11
# https://leetcode.cn/problems/grumpy-bookstore-owner/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        s1 = 0
        s2 = 0
        res = 0
        for i, e in enumerate(customers):
            if grumpy[i] == 0:
                s1 += e
            if grumpy[i] == 1:
                s2 += e
            # 注意点：i+1 的含义是已经计数的数量，如果不足 min，就继续
            if i + 1 < minutes:
                continue
            if s2 > res:
                res = s2
            # 注意点：head 是当前的 index -（数量-1）
            head = i - (minutes - 1)
            s2 -= customers[head] if grumpy[head] == 1 else 0
        return res + s1


# @lc code=end

if __name__ == "__main__":
    customers: List[int] = deserialize("List[int]", read_line())
    grumpy: List[int] = deserialize("List[int]", read_line())
    minutes: int = deserialize("int", read_line())
    ans = Solution().maxSatisfied(customers, grumpy, minutes)
    print("\noutput:", serialize(ans, "integer"))
