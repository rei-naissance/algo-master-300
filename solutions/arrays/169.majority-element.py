#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # MY SOLUTION

        # 1. Create a dictionary to store the count of each number
        return_map = {}
        
        # 2. Iterate through the list and count the occurrences of each number
        for i in range(len(nums)):
            # 3. If the number is already in the dictionary, increment its count
            if nums[i] in return_map:
                return_map[nums[i]] += 1
            # 4. If the number is not in the dictionary, add it with a count of 1
            if nums[i] not in return_map:
                return_map[nums[i]] = 1

        # print(return_map)

        # 5. Find the number with the maximum count in the dictionary and return
        return max(return_map, key=return_map.get) 
    
        # OTHER SOLUTIONS

        # a. Boyer-Moore Voting Algorithm
        # This algorithm works by maintaining a count of the current candidate for the majority element.
        # 1. Initialize a count variable to 0 and a candidate variable to None.

        # count = 0
        # candidate = None

        # 2. Iterate through the list of numbers.
        # for num in nums:
        #     -- If count is 0, set the current number as the candidate.
        #     if count == 0:
        #         candidate = num
        #     -- Increment or decrement the count based on whether the current number is equal to the candidate.
        #     count += (1 if num == candidate else -1)

        # return candidate

        # b. Sort the list and return the middle element
        # return sorted(nums)[len(nums) // 2]

# @lc code=end

