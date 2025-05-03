#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # MY SOLUTION
        # 1. Initialize a variable ret to the first element of the list nums
        ret = nums[0]

        # 2. Iterate through the rest of the list nums, XORing each element with ret
        for i in range(1, len(nums)):
            # 3. XOR operation will cancel out the duplicate numbers (because it's commutative),
            # leaving only the single number
            ret ^= nums[i]

        # 4. Return the result
        return ret
# @lc code=end

