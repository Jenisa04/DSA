import math

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:   
        products = dict() 
        # dictionary of product and tuple of numbers  
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                prod = nums[i] * nums[j]
                if prod not in products:
                    products[prod] = [(nums[i], nums[j])]
                else:
                    products[prod].append((nums[i], nums[j]))
        
        # now find products that have more than 1 tuple i.e. len(val)>1
        res = 0
        for key, val in products.items():
            if len(val) > 1:
                comb = math.comb(len(val), 2)
                res += 8*comb

        return res