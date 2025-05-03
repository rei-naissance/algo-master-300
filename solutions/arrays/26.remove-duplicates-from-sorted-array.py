#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # MY SOLUTION
        # 1. Check if the list is empty, if so return 0
        if not nums:
            return 0
        
        # 2. Initialize an index variable to 1
        idx = 1

        # 3. Iterate through the list starting from the second element
        for i in range(1, len(nums)):
            # 4. If the current element is not equal to the previous element, update the list at index idx with the current element and increment idx
            if nums[i] != nums[i - 1]:
                nums[idx] = nums[i]
                idx += 1

        return idx

# @lc code=end

