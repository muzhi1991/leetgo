# Created by muzhi1991 at 2024/12/24 10:20
# leetgo: 1.4.11
# https://leetcode.cn/problems/min-stack/

from typing import *
from leetgo_py import *

import heapq
# @lc code=begin


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_val = 2**31

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min_val:
            self.min_val = val
        self.min_stack.append(self.min_val)

    def pop(self) -> None:
        self.stack.pop()
        v = self.min_stack.pop()
        if len(self.min_stack) > 0:
            self.min_val = self.min_stack[-1]
        else:
            self.min_val = 2**31

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.counts = {}
#         self.heap = []
#
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if val not in self.counts:
#             heapq.heappush(self.heap, val)
#             self.counts[val] = 1
#         else:
#             self.counts[val] += 1
#
#     def pop(self) -> None:
#         v = self.stack.pop()
#         self.counts[v] -= 1
#         if self.counts[v] == 0:
#             del self.counts[v]
#
#     def top(self) -> int:
#         return self.stack[-1]
#
#     def getMin(self) -> int:
#         v = self.heap[0]
#         while v not in self.counts:
#             heapq.heappop((self.heap))
#             v = self.heap[0]
#         return v


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MinStack()

    for i in range(1, len(ops)):
        match ops[i]:
            case "push":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                obj.push(val)
                output.append("null")
            case "pop":
                obj.pop()
                output.append("null")
            case "top":
                ans = serialize(obj.top())
                output.append(ans)
            case "getMin":
                ans = serialize(obj.getMin())
                output.append(ans)

    print("\noutput:", join_array(output))
