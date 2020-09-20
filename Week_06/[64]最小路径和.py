# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。 
# 
#  说明：每次只能向下或者向右移动一步。 
# 
#  示例: 
# 
#  输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
#  
#  Related Topics 数组 动态规划 
#  👍 675 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minPathSum(self, grid: List[List[int]])-> int:
        d = {}
        nr = len(grid)
        nc = len(grid[0])
        def dfs(x, y):
            if (x, y) in d:
                return d[(x, y)]
            if x == nr or y == nc:
                return float('inf')
            p = min(dfs(x + 1, y), dfs(x, y + 1))
            d[(x, y)] = grid[x][y] + (0 if p == float('inf') else p)
            return d[(x, y)]
        return dfs(0 ,0)
# leetcode submit region end(Prohibit modification and deletion)
