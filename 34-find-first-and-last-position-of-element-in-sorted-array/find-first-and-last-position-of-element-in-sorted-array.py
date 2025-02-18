class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        
        def binSearch(nums, target, searchLeft):

            l = 0
            r = len(nums) - 1
            idx = -1
            
            while l<=r:
                m = l + (r-l)//2
                if nums[m] < target:
                    l = m+1
                elif nums[m] > target:
                    r = m-1
                else:
                    idx = m
                    if searchLeft:
                        r = m-1
                    else:
                        l = m+1
            return idx
            
        left = binSearch(nums, target, True)
        right = binSearch(nums, target, False)

        return [left, right]