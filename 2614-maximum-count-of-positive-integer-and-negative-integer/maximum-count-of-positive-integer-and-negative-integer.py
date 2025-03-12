class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        pos = 0
        neg = 0
        if len(nums) == 1:
            if nums[0] != 0:
                return 1

        while l<=r:
            if nums[l] < 0:
                neg+=1
            elif nums[l] > 0:
                pos+=1
            if nums[r] < 0:
                neg+=1
            elif nums[r] > 0:
                pos+=1
            
            if l==r:
                if nums[l] < 0:
                    neg-=1
                elif nums[l] > 0:
                    pos-=1
        
            l+=1
            r-=1
        return max(pos,neg)  