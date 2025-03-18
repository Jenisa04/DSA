class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        numsSet = set(nums)
        maxCount = 0

        for num in numsSet:
            if num-1 not in numsSet:
                l = 1
                while (l+num) in numsSet:
                    l+=1
                maxCount = max(maxCount, l)
        return maxCount