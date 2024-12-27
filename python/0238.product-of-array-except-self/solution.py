# Created by muzhi1991 at 2024/12/24 09:53
# leetgo: 1.4.11
# https://leetcode.cn/problems/product-of-array-except-self/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     if len(nums) == 2:
    #         return [nums[-1], nums[-2]]
    #     answer = []
    #     buf1 = [1] * len(nums)
    #     buf2 = [1] * len(nums)
    #     for i, n in enumerate(nums):
    #         if i == 0:
    #             buf1[0] = n
    #             buf2[len(nums) - 1] = nums[len(nums) - 1]
    #         else:
    #             buf1[i] = buf1[i - 1] * nums[i]
    #             buf2[len(nums) - 1 - i] = buf2[len(nums) - i] * nums[len(nums) - 1 - i]
    #         # print(i, buf1, buf2)
    #     for i in range(len(nums)):
    #         if i == 0:
    #             answer.append((buf2[1]))
    #         elif i == len(nums) - 1:
    #             answer.append((buf1[-2]))
    #         else:
    #             answer.append(buf1[i - 1] * buf2[i + 1])
    #     return answer
    #

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                answer[0] = 1
            else:
                answer[i] = answer[i - 1] * nums[i - 1]
        tmp = 1
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                continue
            tmp = tmp * nums[i + 1]
            answer[i] = tmp * answer[i]
        return answer


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().productExceptSelf(nums)
    print("\noutput:", serialize(ans, "integer[]"))
