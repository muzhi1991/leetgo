# Created by muzhi1991 at 2025/01/03 10:46
# leetgo: 1.4.11
# https://leetcode.cn/problems/queue-reconstruction-by-height/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p: (-p[0], p[1]))
        # print(people)
        res = []
        for h, k in people:
            res.insert(k, (h, k))

        return res


# @lc code=end

if __name__ == "__main__":
    people: List[List[int]] = deserialize("List[List[int]]", read_line())
    # people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    # people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
    ans = Solution().reconstructQueue(people)
    print("\noutput:", serialize(ans, "integer[][]"))
