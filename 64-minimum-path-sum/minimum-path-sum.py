class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        recurrence = dp[i][j] = mim weight to get to index i,j

        can either move down or right. => can either move up or left. 
        '''
        memo = {}
        memo[(0, 0)] = grid[0][0]


        def dp(i,j):
            if (i,j) not in memo: 
                
                if i < 0 or j < 0: 
                    result =  float('inf') # dont want to choose this....
                else: # case i = j = 0 has been handled
                    result = grid[i][j] + min(dp(i - 1, j), dp(i, j - 1))
                memo[(i,j)] = result
            return memo[(i,j)]

        n = len(grid) - 1
        m = len(grid[0]) - 1

        
        return dp(n, m)

        