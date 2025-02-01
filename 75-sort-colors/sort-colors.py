class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # cannot use built-in sort function
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        l = 0 
        r = len(nums) - 1
        m = 0
        while m <= r:
            if nums[m] == 0:
                swap(l,m)
                m+=1
                l+=1
            elif nums[m] == 2:
                swap(r,m)
                r-=1
            else:
                m+=1