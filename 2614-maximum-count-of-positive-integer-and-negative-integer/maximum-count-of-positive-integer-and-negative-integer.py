class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # edge cases:
        # 1. if nums[0] is positive: only positive integers
        # 2. if nums[last element] is negetave: only negative integers
        # 3. if none if the above: can use binary search
        n = len(nums)
        if nums[0] > 0 or nums[n-1] < 0:
            return n
         
        l = 0
        r = n-1
        target = 0
        # find first positive integer
        while l<=r:
            m = l + (r-l) // 2
            if target >= nums[m]:
                l = m+1
            elif target < nums[m]:
                r = m-1
        
        pos = len(nums[l:])
        
        l = 0
        r = n-1
        target = 0
        # find first negative integer
        while l<=r:
            m = l + (r-l) // 2
            if target > nums[m]:
                l = m+1
            elif target <= nums[m]:
                r = m-1
        neg = len(nums[:r+1])
        return max(pos,neg)  