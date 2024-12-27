# Created by muzhi1991 at 2024/12/16 11:23
# leetgo: 1.4.11
# https://leetcode.cn/problems/kth-largest-element-in-an-array/

from typing import *
from leetgo_py import *
import random

random.seed(10)
# @lc code=begin


class Node:
    def __init__(self, v, left=None, right=None):
        self.v = v
        self.left = left
        self.right = right


class MaxHeap:
    def __init__(self, arr):
        self.heap = []
        for a in arr:
            self.heap.append(a)
            cur = len(self.heap) - 1
            # shift up
            while True:
                parent = cur // 2
                # print(self.heap,parent)
                if self.heap[parent] < self.heap[cur]:
                    # swap
                    v = self.heap[parent]
                    self.heap[parent] = self.heap[cur]
                    self.heap[cur] = v
                cur = parent
                if cur == 0:
                    break
        print(self.heap)
        self.heap_size = len(self.heap)

        # if (len(arr) - 1) % 2 == 0:  # left
        #     silibing = len(arr)
        # else:
        #     sibing = len(arr) - 2
        # if sibing <len(arr):
        #     pass

    def removeTop(self):
        if not self.heap:
            return None
        r = self.heap[0]
        self.heap[0] = -1

        # refresh
        cur = 0
        while cur < self.heap_size:
            left, right = cur * 2 + 1, cur * 2 + 2
            if left >= self.heap_size and right >= self.heap_size:
                break
            if left < self.heap_size and right < self.heap_size:
                if self.heap[left] >= self.heap[right]:
                    self.heap[cur] = self.heap[left]
                    self.heap[left] = -1
                    cur = left
                else:
                    self.heap[cur] = self.heap[right]
                    self.heap[right] = -1
                    cur = right
            else:
                if left < self.heap_size:
                    self.heap[cur] = self.heap[left]
                    self.heap[left] = -1
                    cur = left

                if right < self.heap_size:
                    self.heap[cur] = self.heap[right]
                    self.heap[right] = -1
                    cur = left
        return r


class Solution:
    """
    快速选择算法，这个方法更简单，没那么多边界条件要考虑，适用于第n 大这种问题
    """

    def quickselect(self, nums, k):
        center = random.choice(nums)
        bigger = []
        equal = []
        smaller = []
        for n in nums:
            if n > center:
                bigger.append(n)
            elif n == center:
                equal.append(n)
            else:
                smaller.append(n)
        if len(bigger) >= k:
            return self.quickselect(bigger, k)
        if len(bigger) + len(equal) >= k:
            return equal[0]
        return self.quickselect(equal + smaller, k - len(bigger))

    """
    快排的引用，双指针法，有很多细节
    """

    def func(self, nums, start, end, k):
        if start == end:
            return start
        # tt = random.randint(start, end)
        tt = (start + end) // 2
        # print(tt)
        nums[start], nums[tt] = nums[tt], nums[start]
        p = nums[start]
        left = start  # 要点0；这里不要+1，要不长度为 2，下面的 left<right 都进不去
        right = end
        while left < right:
            while left <= right:
                # 只有当左右同时满足“强”交换条件的时候出发交换
                if nums[left] > p and nums[right] < p:
                    break
                # 要点一：同步更新 left，right，否则相同元素会退化
                if (
                    nums[left] <= p
                ):  # 要点二：这里和下面是否有等号其实都正确，建议加上，快速收敛
                    left += 1
                if nums[right] >= p:
                    right -= 1

            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        # 要点三：使用right，否则长度为2的过不了，这个不好理解，得仔细想想
        nums[start], nums[right] = nums[right], nums[start]  # left-1
        # print(start, end, left, right)
        # print(nums)

        if right < k - 1:
            return self.func(nums, right + 1, end, k)  # 递归条件
        if right > k - 1:
            return self.func(nums, start, right - 1, k)
        return right

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return self.quickselect(nums, k)
        # return nums[self.func(nums, 0, len(nums) - 1, len(nums) - k + 1)]  # should +1 and return number not index
        heap = MaxHeap(nums)
        for i in range(1):
            r = heap.removeTop()
            print(r)

        return r


# @lc code=end

if __name__ == "__main__":
    # nums: List[int] = deserialize("List[int]", read_line())
    # k: int = deserialize("int", read_line())
    nums = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
    ]

    k = 1
    ans = Solution().findKthLargest(nums, k)
    print("\noutput:", serialize(ans, "integer"))
