class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = k%len(nums)
        if idx!=0:
            nums[:idx], nums[idx:] = nums[-idx:], nums[:-idx]
