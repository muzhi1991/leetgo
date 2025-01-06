# Created by muzhi1991 at 2025/01/06 09:51
# leetgo: 1.4.11
# https://leetcode.cn/problems/evaluate-division/

from typing import *
from leetgo_py import *
from collections import defaultdict
# @lc code=begin


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []
        vv = {}
        buf = defaultdict(set)
        for (a, b), v in zip(equations, values):
            vv[(a, b)] = v
            vv[(b, a)] = 1 / v
            buf[a].add(b)
            buf[b].add(a)
        while True:
            ll = len(vv)
            for a, cmb in buf.items():
                cmb = list(cmb)
                for i in range(len(cmb)):
                    for j in range(i + 1, len(cmb)):
                        if (cmb[i], cmb[j]) not in vv:
                            vv[(cmb[i], cmb[j])] = vv[(cmb[i], a)] * vv[(a, cmb[j])]
                            vv[(cmb[j], cmb[i])] = vv[(cmb[j], a)] * vv[(a, cmb[i])]
                            buf[cmb[j]].add(cmb[i])
                            buf[cmb[i]].add(cmb[j])
            if len(vv) == ll:
                break
        for a, b in queries:
            if (a, b) in vv:
                res.append(vv[(a, b)])
            elif a in buf and a == b:
                res.append(1.0)
            else:
                res.append(-1.0)

        return res


# @lc code=end

if __name__ == "__main__":
    equations: List[List[str]] = deserialize("List[List[str]]", read_line())
    values: List[float] = deserialize("List[float]", read_line())
    queries: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().calcEquation(equations, values, queries)
    print("\noutput:", serialize(ans, "double[]"))
