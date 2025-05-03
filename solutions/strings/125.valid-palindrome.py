#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # MY SOLUTION

        # 1. Initialize an empty string to store the filtered characters
        ret = ""

        # 2. Iterate through each character in the input string
        for char in s:
            # 3. Check if the character is alphanumeric (a-z, A-Z, 0-9)
            if char.isalpha() or char.isdigit():
                # 4. If it is, append it to the filtered string
                ret += char

        # 5. Convert the filtered string to lowercase
        ret = ret.lower()
        
        # print(ret)

        # 6. Check if the filtered string is equal to its reverse
        return ret == ret[::-1]
        
# @lc code=end

