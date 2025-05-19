#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # MY SOLUTION
        
        # 1. Check if the input string s is empty
        if not s:
            return True

        # 2. Iterate through each character in the input string t
        i = 0
        for char in t:
            # 3. If the index i is equal to the length of s, break the loop
            if i == len(s):
                break
            # 4. If the current character in t is equal to the character at index i in s, increment i
            if char == s[i]:
                i += 1    

        # 5. Return True if i is equal to the length of s
        return i == len(s)
        
        # OTHER SOLUTIONS

        sp = tp = 0

        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        
        return sp == len(s)
# @lc code=end

