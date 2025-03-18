class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        rec = {}
        for index, num in enumerate(nums):
            ans = target - num
            if ans in rec:
                return [rec[ans], index]
            rec[num] = index
        return