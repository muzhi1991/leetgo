# [399. 除法求值][link] (Medium)

[link]: https://leetcode.cn/problems/evaluate-division/

给你一个变量对数组 `equations` 和一个实数值数组 `values` 作为已知条件，其中 `equations[i] = [Aᵢ, Bᵢ]
` 和 `values[i]` 共同表示等式 `Aᵢ / Bᵢ = values[i]` 。每个 `Aᵢ` 或 `Bᵢ` 是一个表示单个变量的字符串。

另有一些以数组 `queries` 表示的问题，其中 `queries[j] = [Cⱼ, Dⱼ]` 表示第 `j` 个问题，请你根据已知条
件找出 `Cⱼ / Dⱼ = ?` 的结果作为答案。

返回 **所有问题的答案** 。如果存在某个无法确定的答案，则用 `-1.0` 替代这个答案。如果问题中出现了给定
的已知条件中没有出现的字符串，也需要用 `-1.0` 替代这个答案。

**注意：** 输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

**注意：** 未在等式列表中出现的变量是未定义的，因此无法确定它们的答案。

**示例 1：**

```
输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"
],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
注意：x 是未定义的 => -1.0
```

**示例 2：**

```
输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["
c","b"],["bc","cd"],["cd","bc"]]
输出：[3.75000,0.40000,5.00000,0.20000]
```

**示例 3：**

```
输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
输出：[0.50000,2.00000,-1.00000,-1.00000]
```

**提示：**

- `1 <= equations.length <= 20`
- `equations[i].length == 2`
- `1 <= Aᵢ.length, Bᵢ.length <= 5`
- `values.length == equations.length`
- `0.0 < values[i] <= 20.0`
- `1 <= queries.length <= 20`
- `queries[i].length == 2`
- `1 <= Cⱼ.length, Dⱼ.length <= 5`
- `Aᵢ, Bᵢ, Cⱼ, Dⱼ` 由小写英文字母与数字组成
