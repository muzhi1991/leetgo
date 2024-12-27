# Created by muzhi1991 at 2024/12/19 14:54
# leetgo: 1.4.11
# https://leetcode.cn/problems/implement-trie-prefix-tree/

from typing import *
from leetgo_py import *

# @lc code=begin


class Node:
    def __init__(self, v, children=set()) -> None:
        self.v = v
        self.children = children


class Trie:
    def __init__(self):
        self.root = {}
        pass

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur:
                cur[w] = {}
                cur = cur[w]
            else:
                cur = cur[w]
        cur["$"] = {}
        # print(self.root)

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word + "$":
            if w in cur:
                cur = cur[w]
            else:
                return False
        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w in cur:
                cur = cur[w]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = Trie()

    for i in range(1, len(ops)):
        match ops[i]:
            case "insert":
                method_params = split_array(params[i])
                word: str = deserialize("str", method_params[0])
                obj.insert(word)
                output.append("null")
            case "search":
                method_params = split_array(params[i])
                word: str = deserialize("str", method_params[0])
                ans = serialize(obj.search(word))
                output.append(ans)
            case "startsWith":
                method_params = split_array(params[i])
                prefix: str = deserialize("str", method_params[0])
                ans = serialize(obj.startsWith(prefix))
                output.append(ans)

    print("\noutput:", join_array(output))
