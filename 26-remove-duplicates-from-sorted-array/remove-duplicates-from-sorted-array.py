class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 0 : return 0
        ptr1 = 0
        
        for ptr2 in range(1,len(nums)):
            if nums[ptr1] != nums[ptr2]:
                ptr1 += 1
                nums[ptr1] = nums[ptr2]
                
        return ptr1 + 1