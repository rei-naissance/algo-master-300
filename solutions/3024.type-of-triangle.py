#
# @lc app=leetcode id=3024 lang=python3
#
# [3024] Type of Triangle
#

# @lc code=start
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        
        if (nums[0] + nums[1] <= nums[2] or nums[1] + nums[2] <= nums[0] or nums[0] + nums[2] <= nums[1]): return "none"
        
        return "equilateral" if len(set(nums)) == 1 else "isosceles" if len(set(nums)) == 2 else "scalene"
# @lc code=end
