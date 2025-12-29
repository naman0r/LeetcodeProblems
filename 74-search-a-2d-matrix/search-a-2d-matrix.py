class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        '''
        brute force solution: to loop through all values
        - complexity: o(n*m), space complexity = o(n)


        # python code for brute force (somehow beats 100% in speed idfk how)

        for row in matrix: 
            for item in row: 
                if item == target: 
                    return True

        
        return False
        '''

        '''
        Efficient Algorithm: 
        - binary search? how would i do this in a 2d array? 

        1. binary search for what row we should search in (log m complexity)
        2. binary search in what column we should search in (log n complexity)
        '''
        # THIS SOLUTION IS LOG(m) + log(n) time complexity

        top, bottom = 0, len(matrix) - 1 

        # rowr is the first element of the row at index 

        while top<= bottom: 
            row = (top + bottom) // 2

            if target > matrix[row][-1]: # means that the target is too high for the row chosen
                top = row + 1
            elif target < matrix[row][0]: # means we search 0, rowl
                bottom = row - 1
            else: # this means than matrix[][] < target < matrix[row][-1] 
                break

        if not top<=bottom: 
            return False

        row = (top + bottom) // 2
        l, r = 0, len(matrix[0]) - 1

        while l<=r: 
            mid = (l + r) // 2
            if (target > matrix[row][mid]):
                l = mid + 1
            elif (target < matrix[row][mid]):
                r = mid - 1
            else: # equals case
                return True

        return False # end case

        



