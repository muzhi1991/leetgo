# Created by muzhi1991 at 2025/01/02 10:06
# leetgo: 1.4.11
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = {}
        for c in p:
            if c not in d:
                d[c] = 0
            d[c] += 1
        res = []
        tmp = d.copy()
        ss = len(p)
        i = 0
        j = 0
        # fix1: 这里等于号忘记
        while i <= len(s) - len(p) and j < len(s):
            # print(i, j, tmp)
            if s[j] not in tmp:
                j += 1
                i = j
                continue
            else:
                # fix: 这里重置的位置错了
                if i == j:
                    # print(i, j, tmp, ss)
                    tmp = d.copy()
                    ss = len(p)
                    # print(i, j, tmp, ss)

            if tmp[s[j]] > 0:
                tmp[s[j]] -= 1
                ss -= 1
                if ss == 0:
                    res.append(i)
                j += 1
            else:
                i += 1
                tmp[s[i - 1]] += 1
                ss += 1
                # fix： 这里指针交错
                if j < i:
                    j = i
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    p: str = deserialize("str", read_line())
    ans = Solution().findAnagrams(s, p)
    print("\noutput:", serialize(ans, "integer[]"))
