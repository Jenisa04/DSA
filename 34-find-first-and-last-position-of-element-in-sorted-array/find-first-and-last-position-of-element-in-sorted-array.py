class Solution:
    # Jenisa
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        # Approach:
        # perform binary search twice
        # first to find first index
        # second to find last index
        l = 0
        r = len(nums) - 1
        res = [-1, -1]
        
        while l<=r:
            m = l + (r-l)//2
            if nums[m] >= target:
                r = m-1
            else:
                l = m+1
        
        if l<len(nums) and nums[l] == target:
            res[0] = l

        l = 0
        r = len(nums)-1
        while l<=r:
            m = l + (r-l)//2
            if nums[m]>target:
                r = m-1
            else:
                l = m+1
        
        if r>=0 and nums[r]==target:
            res[1] = r

        return res


        return [left, right]