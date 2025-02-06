import math

# optimizing: instead of saving tuples of the numbers I could just keep a count; more memory + runtime efficient
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:   
        products = dict() 
        # dictionary of product and tuple of numbers  
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                prod = nums[i] * nums[j]
                if prod not in products:
                    products[prod] = 1
                else:
                    products[prod] += 1
        
        # now find products that have more than 1 tuple i.e. len(val)>1
        res = 0
        for key, val in products.items():
            if val > 1:
                comb = math.comb(val, 2)
                res += 8*comb

        return res