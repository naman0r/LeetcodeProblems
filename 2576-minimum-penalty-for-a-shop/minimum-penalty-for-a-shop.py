class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # if no customers come and shop is open, pen += 1
        # if shop is closed and customers come, pen += 1

        # earliest hour so that shop can incur least penality

        # pick a hour j to open. shop is open 1 - j, and closed j 
        # if shop closes jth hour, shop is closed for j 
        #penalties = [0] * len(customers)

        # if shop is never open, what is the penalty? the Number of Ys in the string.
        #return customers.count('c') # number of charecters
        '''
        close_at = 0
        min_pen = customers.count('Y') # assume we keep it closed from j = 0

    
        # if we choose to have it open in this hour,
        # count the number of Ns before it. 
        # if we decide to close it at exactly this hour, look at the number of 
        # Ys ahead of this index (including this index) + number of Ns before it


        for i in range(len(customers) + 1): 
            # count Ns at 0 < x < i
            # if we close it exactly now: 

            prev_pen = customers[0:i].count('N') # was open, no one came
            forward_pen = customers[i::].count('Y')

            if (prev_pen + forward_pen < min_pen): 
                min_pen = prev_pen + forward_pen
                close_at = i

        
        print(f"best close at {i} with penality {min_pen}")
        return close_at
        '''
        
        penalty = 0
        min_pen = 0
        close_at = 0

        # assume that for every charecter, we will close it now?
        for i, c in enumerate(customers):
            if c == 'Y': 
                penalty -= 1
            elif c =='N':
                penalty += 1

            if penalty < min_pen: 
                close_at = i + 1 # close i after?
                min_pen = penalty

        return close_at
            

