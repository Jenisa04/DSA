from decimal import Decimal, getcontext
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        getcontext().prec = 10
        if len(nums) == k:
            res = Decimal(sum(nums)) / Decimal(len(nums))
            return res
        

        winSum = sum(nums[:k])
        maxVal = Decimal(winSum)
        for i in range(k, len(nums)) :
            winSum += (nums[i] - nums[i-k])
            maxVal = max(maxVal, Decimal(winSum))
        return float(round(maxVal/k,5))