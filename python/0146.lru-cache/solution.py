# Created by muzhi1991 at 2024/12/27 09:47
# leetgo: 1.4.11
# https://leetcode.cn/problems/lru-cache/

from typing import *
from leetgo_py import *

from collections import OrderedDict
# @lc code=begin

"""
Linked Array + Hash Map
hashmap 负责检索存储 k，v，以及关键的是指向 list 的 pointer
linked list 是一个双向的链表，方便插入删除
Python 上更简单的办法是用 OrderedDict 作为父类，实现 LRU 的算法
"""


class Node:
    def __init__(self, pre, key, val, next) -> None:
        self.pre = pre
        self.key = key
        self.val = val
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cnt = 0
        self.map = {}
        self.head = None
        self.tail = None

    def _remove_tail(self):
        # popitem
        if self.tail is not None:
            if self.tail.pre is not None:
                self.tail.pre.next = None
            old = self.tail
            self.tail = self.tail.pre
            old.pre = None
            return old

    def get(self, key: int) -> int:
        print("get")
        if key in self.map:
            node = self.map[key]
            if node.pre is not None:
                if self.tail is node:
                    self._remove_tail()
                else:
                    node.pre.next = node.next
                    node.next.pre = node.pre  # fix
                self.head.pre = node
                node.next = self.head
                self.head = node
                node.pre = None
            return node.val
        return -1  # fix

    def _put_ahead(self, node):
        # remove_to_end
        if self.head is None:
            self.head = node
            self.tail = node  # fix
            return
        node.next = self.head
        self.head.pre = node
        self.head = node
        if self.tail is None:
            self.tail = node

    def put(self, key: int, value: int) -> None:
        print("put")

        if key in self.map:  # fix
            self.get(key)
            self.map[key].val = value
        elif self.cnt < self.capacity:
            node = Node(pre=None, key=key, val=value, next=None)
            self._put_ahead(node)
            self.cnt += 1
            self.map[key] = node
        else:
            node = Node(pre=None, key=key, val=value, next=None)
            n = self._remove_tail()
            del self.map[n.key]
            self._put_ahead(node)
            self.map[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# @lc code=end

if __name__ == "__main__":
    # ops: List[str] = deserialize("List[str]", read_line())
    # params = split_array(read_line())
    output = ["null"]
    ops = ["LRUCache", "put", "put", "put", "put", "get", "get", "get", "get", "put", "get", "get", "get", "get", "get"]
    params = [
        "[3]",
        "[1,1]",
        "[2,2]",
        "[3,3]",
        "[4,4]",
        "[4]",
        "[3]",
        "[2]",
        "[1]",
        "[5,5]",
        "[1]",
        "[2]",
        "[3]",
        "[4]",
        "[5]",
    ]
    constructor_params = split_array(params[0])
    capacity: int = deserialize("int", constructor_params[0])
    obj = LRUCache(capacity)

    for i in range(1, len(ops)):
        match ops[i]:
            case "get":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                ans = serialize(obj.get(key))
                output.append(ans)
            case "put":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                value: int = deserialize("int", method_params[1])
                obj.put(key, value)
                output.append("null")

    print("\noutput:", join_array(output))
