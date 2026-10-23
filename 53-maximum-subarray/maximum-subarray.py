class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        if not nums: 
            return 0

        elif len(nums) == 1: 
            return nums[0]

        maxxum = float('-inf')
        current = 0

        for num in nums: 
            current = max(current + num, num)
            maxxum = max(current, maxxum)

        return maxxum

        

        

