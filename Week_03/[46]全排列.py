# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法 
#  👍 858 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, ans):
            if not nums:
                res.append(ans)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], ans + [nums[i]])
        dfs(nums, [])
        return res
# leetcode submit region end(Prohibit modification and deletion)
