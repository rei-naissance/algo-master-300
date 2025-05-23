#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(openN, closedN, path):
            if openN == closedN == n:
                res.append(path)
                return
            
            if openN < n:
                backtrack(openN + 1, closedN, path + '(')
            if closedN < openN:
                backtrack(openN, closedN + 1, path + ')')
        
        res = []
        backtrack(0, 0, '')
        return res
# @lc code=end

