# Created by muzhi1991 at 2024/12/30 14:03
# leetgo: 1.4.11
# https://leetcode.cn/problems/word-break/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}
        cur = trie
        for word in wordDict:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["$"] = {}
        print(trie)
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(len(s)):
            if s[i] not in trie or dp[i] != 1:  # 快速跳过
                continue
            cur = trie
            for j in range(i, len(s)):
                if "$" in cur:  # 边界条件，判断j-1前一个字符是不是结尾
                    print(i, j, s[i:j])
                    if dp[i] == 1:
                        dp[j] = 1
                if s[j] in cur:
                    cur = cur[s[j]]
                else:
                    break
                if j == len(s) - 1 and "$" in cur:  # 特殊边界条件，判断当前字符串-最后一个是否结尾
                    if dp[i] == 1:
                        print(i, j + 1, s[i : j + 1])
                        dp[j + 1] = 1
            print(i, dp)
        return False if dp[-1] == 0 else True


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    wordDict: List[str] = deserialize("List[str]", read_line())
    ans = Solution().wordBreak(s, wordDict)
    print("\noutput:", serialize(ans, "boolean"))
