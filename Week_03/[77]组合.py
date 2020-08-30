# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。 
# 
#  示例: 
# 
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
#  Related Topics 回溯算法 
#  👍 338 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        self.dfs(1, n, k, [], res)
        return res

    def dfs(self, start, n, k, ans, res):
        if len(ans) == k:
            res.append(ans[:])
            return
        for i in range(start, n + 1):
            ans.append(i)
            self.dfs(i + 1, n, k, ans, res)
            ans.pop()

# leetcode submit region end(Prohibit modification and deletion)
