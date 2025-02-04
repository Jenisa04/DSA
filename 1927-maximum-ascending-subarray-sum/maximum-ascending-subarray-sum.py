class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # first find ascending subarray in nums
        res = nums[0]
        finalRes = nums[0]
        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx-1]:
                res+=nums[idx]
            else:
                res = nums[idx]
            finalRes = max(finalRes, res)
        
        return finalRes