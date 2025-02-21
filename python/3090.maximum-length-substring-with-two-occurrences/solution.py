# Created by muzhi1991 at 2025/02/21 10:38
# leetgo: 1.4.11
# https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/

from typing import *
from leetgo_py import *
from collections import defaultdict

# @lc code=begin

"""
思路：不定长窗口满足某个条件的问题，
我之前解决无重复子串（题号 3）思路是是用dict记录的跳跃下个点，在这里记录每个点就麻烦了
这里更像是双指针，和固定长度窗口问题的思路一样，就是多个指针（固定长度的 pre 指针只用i-(k-1) 就行）

"""


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = 0
        pre = -1
        buf = defaultdict(int)
        for i, e in enumerate(s):
            buf[e] += 1
            while buf[e] > 2:
                pre += 1
                buf[s[pre]] -= 1
            if i - pre > res:
                res = i - pre
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maximumLengthSubstring(s)
    print("\noutput:", serialize(ans, "integer"))
