class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # we need to be able to reach exactly the last index in this array. 

        # bottom up DP? 
        farthest = 0  # farthest index we can reach so far

        for i in range(len(nums)):
            # if we can't even reach i, we are stuck
            if i > farthest:
                return False

            # update farthest reach from this position
            farthest = max(farthest, i + nums[i])

            # early exit if we can reach or pass the end
            if farthest >= len(nums) - 1:
                return True

        return True