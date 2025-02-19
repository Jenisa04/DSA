class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()  
        i = 1
        j = 0
        while j < len(nums):
            if nums[j]>0 and nums[j]==i:
                i+=1
            elif nums[j] > i:
                return i
            j+=1
        return i