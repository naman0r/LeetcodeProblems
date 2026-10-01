class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []
        
        for num in nums: 
            res.append(num**2)

        res.sort()

        return res
