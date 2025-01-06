# Created by muzhi1991 at 2025/01/03 09:45
# leetgo: 1.4.11
# https://leetcode.cn/problems/partition-equal-subset-sum/

from typing import *
from leetgo_py import *

# @lc code=begin


"""
 背包问题 子集满足某个条件
 dp 公式的定义
"""


class Solution:
    def f(self, nums, v, buf):
        if v < 0:
            return False
        # print(v, nums)
        for i in buf:
            if nums[i] == v:
                return True
            buf.remove(i)
            r = self.f(nums, v - nums[i], buf)
            buf.add(i)
            if r:
                return r
        return False

    def canPartition(self, nums: List[int]) -> bool:
        v = sum(nums)
        mn = max(nums)
        if v % 2 != 0:
            return False
        v = v // 2
        if mn > v:
            return False
        # dp = [[0] * (v + 1) for _ in range(len(nums))]
        # dp[i][j] 0到 i 是否存在和等于 j 的数字和

        dp = [0] * (v + 1)
        dp[0] = 1
        # print(v, len(nums), dp[v - 10 : v + 10])

        for i in range(len(nums)):
            if i == 0:
                # dp[i][nums[i]] = 1
                dp[nums[i]] = 1
            else:
                # fix bug 这里需要从大到小的遍历 j，因为他需要使用上一轮的值
                # 如果反过来，会出现某个值利用的值是这一轮更新的值（相当于被用了两次 nums[i]）
                for j in range(v, nums[i] - 1, -1):
                    dp[j] = dp[j] or dp[j - nums[i]]
                # 下面是错误的！！
                # for j in range(v + 1):
                #     dp[j] = dp[j] or (dp[j - nums[i]] if j - nums[i] >= 0 else 0)
                # 使用二维数组就没这个问题，反正上一轮的值存着呢
                # for j in range(v + 1):
                #     dp[i][j] = dp[i - 1][j] or (dp[i - 1][j - nums[i]] if j - nums[i] >= 0 else 0)
        return True if dp[v] else False
        for i in range(len(nums)):
            if dp[i][v]:
                return True
        return False
        # i=1
        # dp=[[] for _ in range(len(nums)+1)]
        # while i<=len(nums):
        #     for n in nums:
        #     for v in dp[i-1]:
        #         dp[i].append(v+n)
        #
        #     i+=1
        buf = {i for i in range(len(nums))}

        print(v)
        return self.f(nums, v, buf)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canPartition(nums)
    print("\noutput:", serialize(ans, "boolean"))
