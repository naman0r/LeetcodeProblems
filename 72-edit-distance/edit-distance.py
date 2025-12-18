class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        '''
        3 things I can do: 
        - add a ch
        '''

        cache = {} # (m,n) => res

        # standord CS221 first lecture same problem
        def dp(m, n): 
            if (m,n) not in cache: 

                if m == 0: 
                    result = n

                elif n == 0: 
                    result = m

                elif word1[m - 1] ==  word2[n - 1]: 
                    result = dp(m - 1, n - 1) # no change required for this letter

                else: 
                    subcost = 1 + dp(m - 1, n - 1)
                    delcost = 1+ dp(m - 1, n)
                    incost = 1 + dp(m, n-1)
                    result = min(subcost, delcost, incost)
                    
                cache[(m,n)] = result

            return cache[(m,n)]

        return dp(len(word1), len(word2))
