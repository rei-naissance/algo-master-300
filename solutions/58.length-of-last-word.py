#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:


        # MY SOLUTION
        # 1. Strip the string of leading and trailing whitespace
        # 2. Split the string into words using whitespace as the delimiter
        # 3. Return the length of the last word
        return len(s.strip().split()[-1])
# @lc code=end

