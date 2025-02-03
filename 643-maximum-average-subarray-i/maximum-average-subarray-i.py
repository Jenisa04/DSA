from decimal import Decimal, getcontext
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        getcontext().prec = 20
        if len(nums) == k:
            res = Decimal(sum(nums)) / Decimal(len(nums))
            return res
        

        winSum = sum(nums[:k])
        maxVal = Decimal(winSum) / Decimal(k)
        for i in range(k, len(nums)) :
            winSum += (nums[i] - nums[i-k])
            maxVal = max(maxVal, Decimal(winSum)/Decimal(k))
        return float(round(maxVal,5))