# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入："ab-cd"
# 输出："dc-ba"
#  
# 
#  示例 2： 
# 
#  输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
#  
# 
#  示例 3： 
# 
#  输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
#  
# 
#  
# 
#  提示： 
# 
#  
#  S.length <= 100 
#  33 <= S[i].ASCIIcode <= 122 
#  S 中不包含 \ or " 
#  
#  Related Topics 字符串 
#  👍 63 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        front, end = 0, len(S) - 1
        while front < end:
            if not S[front].isalpha():
                front += 1
            elif not S[end].isalpha():
                end -= 1
            else:
                S[front], S[end] = S[end], S[front]
                front += 1
                end -= 1
        return "".join(S)
        
# leetcode submit region end(Prohibit modification and deletion)
