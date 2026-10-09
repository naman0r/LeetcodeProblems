class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:

        acc_tax = 0

        prev = 0

        for upper, percentage in brackets: 
            if income <= prev: 
                break

            taxable = min(income, upper) # choose the lower number
            # need the previous upper bound, use prev

            #print(f"{taxable}, {prev}, percentage: {percentage}")

            added = (taxable - prev) * (percentage / 100)
            acc_tax += added

            print(f"{taxable}, {prev}, percentage: {percentage}, taxed: {added}, total: {acc_tax}")
            prev = upper


        return acc_tax
        
        