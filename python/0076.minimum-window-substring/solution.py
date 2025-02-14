# Created by muzhi1991 at 2025/02/08 10:37
# leetgo: 1.4.11
# https://leetcode.cn/problems/minimum-window-substring/

from typing import *
from leetgo_py import *
from collections import Counter

# @lc code=begin
# 双指针，用一个 dict 统计出现次数


class Solution:
    def check(self, a, b):
        if len(a) != len(b):
            return False
        for k, v in a.items():
            if v < b[k]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 1:
            if t in s:
                return t
            else:
                return ""
        res = ""
        targets = Counter()
        for c in t:
            targets[c] += 1

        buf = Counter()
        q = []
        i = 0
        # for ii, c in enumerate(s):
        #     if c in targets:
        #         i = ii
        #         q.append(i)
        #         buf[c] += 1
        #         break
        # if not buf:
        #     return ""
        # print(targets)
        j = i
        while True:
            while j < len(s):
                if s[j] in targets:
                    buf[s[j]] += 1
                    q.append(j)
                # print(i, j, s[i : j + 1], q, buf)
                if self.check(buf, targets):
                    # if len(res) == 0 or j + 1 - i < len(res):
                    #     res = s[i : j + 1]
                    # j = j + 1
                    # print("break")
                    break
                j += 1

            if j >= len(s):
                break

            while self.check(buf, targets):
                # print("here", i, j, s[i : j + 1], q, buf)
                if len(res) == 0 or j - i + 1 < len(res):
                    res = s[i : j + 1]

                if s[i] in buf and i not in q:
                    buf[s[i]] -= 1
                if not q:
                    break
                t = q.pop(0)
                # print(t)
                i = t
            if i >= len(s) - 1:
                break
            j = j + 1
            # print(j)

        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().minWindow(s, t)
    print("\noutput:", serialize(ans, "string"))
